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
#pxhrsrredi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pxhrsrredi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pxhrsrredi p { margin: 0; padding: 0; }
 #pxhrsrredi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pxhrsrredi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pxhrsrredi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pxhrsrredi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pxhrsrredi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pxhrsrredi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pxhrsrredi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pxhrsrredi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pxhrsrredi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pxhrsrredi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pxhrsrredi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pxhrsrredi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pxhrsrredi .gt_spanner_row { border-bottom-style: hidden; }
 #pxhrsrredi .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pxhrsrredi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pxhrsrredi .gt_from_md> :first-child { margin-top: 0; }
 #pxhrsrredi .gt_from_md> :last-child { margin-bottom: 0; }
 #pxhrsrredi .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pxhrsrredi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pxhrsrredi .gt_indent_1 { text-indent: 5px; }
 #pxhrsrredi .gt_indent_2 { text-indent: calc(5px * 2); }
 #pxhrsrredi .gt_indent_3 { text-indent: calc(5px * 3); }
 #pxhrsrredi .gt_indent_4 { text-indent: calc(5px * 4); }
 #pxhrsrredi .gt_indent_5 { text-indent: calc(5px * 5); }
 #pxhrsrredi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pxhrsrredi .gt_row_group_first td { border-top-width: 2px; }
 #pxhrsrredi .gt_row_group_first th { border-top-width: 2px; }
 #pxhrsrredi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pxhrsrredi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pxhrsrredi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pxhrsrredi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pxhrsrredi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pxhrsrredi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pxhrsrredi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pxhrsrredi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pxhrsrredi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pxhrsrredi .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pxhrsrredi .gt_left { text-align: left; }
 #pxhrsrredi .gt_center { text-align: center; }
 #pxhrsrredi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pxhrsrredi .gt_font_normal { font-weight: normal; }
 #pxhrsrredi .gt_font_bold { font-weight: bold; }
 #pxhrsrredi .gt_font_italic { font-style: italic; }
 #pxhrsrredi .gt_super { font-size: 65%; }
 #pxhrsrredi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pxhrsrredi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pxhrsrredi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pxhrsrredi .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pxhrsrredi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pxhrsrredi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#otpicvpgah table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#otpicvpgah thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#otpicvpgah p { margin: 0; padding: 0; }
 #otpicvpgah .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #otpicvpgah .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #otpicvpgah .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #otpicvpgah .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #otpicvpgah .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #otpicvpgah .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #otpicvpgah .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #otpicvpgah .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #otpicvpgah .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #otpicvpgah .gt_column_spanner_outer:first-child { padding-left: 0; }
 #otpicvpgah .gt_column_spanner_outer:last-child { padding-right: 0; }
 #otpicvpgah .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #otpicvpgah .gt_spanner_row { border-bottom-style: hidden; }
 #otpicvpgah .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #otpicvpgah .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #otpicvpgah .gt_from_md> :first-child { margin-top: 0; }
 #otpicvpgah .gt_from_md> :last-child { margin-bottom: 0; }
 #otpicvpgah .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #otpicvpgah .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #otpicvpgah .gt_indent_1 { text-indent: 5px; }
 #otpicvpgah .gt_indent_2 { text-indent: calc(5px * 2); }
 #otpicvpgah .gt_indent_3 { text-indent: calc(5px * 3); }
 #otpicvpgah .gt_indent_4 { text-indent: calc(5px * 4); }
 #otpicvpgah .gt_indent_5 { text-indent: calc(5px * 5); }
 #otpicvpgah .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #otpicvpgah .gt_row_group_first td { border-top-width: 2px; }
 #otpicvpgah .gt_row_group_first th { border-top-width: 2px; }
 #otpicvpgah .gt_striped { color: #333333; background-color: #F4F4F4; }
 #otpicvpgah .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #otpicvpgah .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #otpicvpgah .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #otpicvpgah .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #otpicvpgah .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #otpicvpgah .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #otpicvpgah .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #otpicvpgah .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #otpicvpgah .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #otpicvpgah .gt_left { text-align: left; }
 #otpicvpgah .gt_center { text-align: center; }
 #otpicvpgah .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #otpicvpgah .gt_font_normal { font-weight: normal; }
 #otpicvpgah .gt_font_bold { font-weight: bold; }
 #otpicvpgah .gt_font_italic { font-style: italic; }
 #otpicvpgah .gt_super { font-size: 65%; }
 #otpicvpgah .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #otpicvpgah .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #otpicvpgah .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #otpicvpgah .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #otpicvpgah .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #otpicvpgah .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tnfkkdfoll table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tnfkkdfoll thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tnfkkdfoll p { margin: 0; padding: 0; }
 #tnfkkdfoll .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #tnfkkdfoll .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tnfkkdfoll .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tnfkkdfoll .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tnfkkdfoll .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tnfkkdfoll .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #tnfkkdfoll .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tnfkkdfoll .gt_col_heading { color: #FFFFFF; background-color: #A81600; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tnfkkdfoll .gt_column_spanner_outer { color: #FFFFFF; background-color: #A81600; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tnfkkdfoll .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tnfkkdfoll .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tnfkkdfoll .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tnfkkdfoll .gt_spanner_row { border-bottom-style: hidden; }
 #tnfkkdfoll .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tnfkkdfoll .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #tnfkkdfoll .gt_from_md> :first-child { margin-top: 0; }
 #tnfkkdfoll .gt_from_md> :last-child { margin-bottom: 0; }
 #tnfkkdfoll .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #FFCCC7; border-left-style: solid; border-left-width: 1px; border-left-color: #FFCCC7; border-right-style: solid; border-right-width: 1px; border-right-color: #FFCCC7; vertical-align: middle; overflow-x: hidden; }
 #tnfkkdfoll .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #tnfkkdfoll .gt_indent_1 { text-indent: 5px; }
 #tnfkkdfoll .gt_indent_2 { text-indent: calc(5px * 2); }
 #tnfkkdfoll .gt_indent_3 { text-indent: calc(5px * 3); }
 #tnfkkdfoll .gt_indent_4 { text-indent: calc(5px * 4); }
 #tnfkkdfoll .gt_indent_5 { text-indent: calc(5px * 5); }
 #tnfkkdfoll .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tnfkkdfoll .gt_row_group_first td { border-top-width: 2px; }
 #tnfkkdfoll .gt_row_group_first th { border-top-width: 2px; }
 #tnfkkdfoll .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tnfkkdfoll .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #tnfkkdfoll .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tnfkkdfoll .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tnfkkdfoll .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tnfkkdfoll .gt_grand_summary_row { color: #FFFFFF; background-color: #FF644E; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tnfkkdfoll .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tnfkkdfoll .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tnfkkdfoll .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tnfkkdfoll .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tnfkkdfoll .gt_left { text-align: left; }
 #tnfkkdfoll .gt_center { text-align: center; }
 #tnfkkdfoll .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tnfkkdfoll .gt_font_normal { font-weight: normal; }
 #tnfkkdfoll .gt_font_bold { font-weight: bold; }
 #tnfkkdfoll .gt_font_italic { font-style: italic; }
 #tnfkkdfoll .gt_super { font-size: 65%; }
 #tnfkkdfoll .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tnfkkdfoll .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tnfkkdfoll .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tnfkkdfoll .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tnfkkdfoll .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tnfkkdfoll .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rbauyxpsou table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rbauyxpsou thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rbauyxpsou p { margin: 0; padding: 0; }
 #rbauyxpsou .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rbauyxpsou .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rbauyxpsou .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rbauyxpsou .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rbauyxpsou .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rbauyxpsou .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #rbauyxpsou .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rbauyxpsou .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rbauyxpsou .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rbauyxpsou .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rbauyxpsou .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rbauyxpsou .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rbauyxpsou .gt_spanner_row { border-bottom-style: hidden; }
 #rbauyxpsou .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rbauyxpsou .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #rbauyxpsou .gt_from_md> :first-child { margin-top: 0; }
 #rbauyxpsou .gt_from_md> :last-child { margin-bottom: 0; }
 #rbauyxpsou .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #rbauyxpsou .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #rbauyxpsou .gt_indent_1 { text-indent: 5px; }
 #rbauyxpsou .gt_indent_2 { text-indent: calc(5px * 2); }
 #rbauyxpsou .gt_indent_3 { text-indent: calc(5px * 3); }
 #rbauyxpsou .gt_indent_4 { text-indent: calc(5px * 4); }
 #rbauyxpsou .gt_indent_5 { text-indent: calc(5px * 5); }
 #rbauyxpsou .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rbauyxpsou .gt_row_group_first td { border-top-width: 2px; }
 #rbauyxpsou .gt_row_group_first th { border-top-width: 2px; }
 #rbauyxpsou .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rbauyxpsou .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #rbauyxpsou .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rbauyxpsou .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rbauyxpsou .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rbauyxpsou .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rbauyxpsou .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rbauyxpsou .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rbauyxpsou .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rbauyxpsou .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rbauyxpsou .gt_left { text-align: left; }
 #rbauyxpsou .gt_center { text-align: center; }
 #rbauyxpsou .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rbauyxpsou .gt_font_normal { font-weight: normal; }
 #rbauyxpsou .gt_font_bold { font-weight: bold; }
 #rbauyxpsou .gt_font_italic { font-style: italic; }
 #rbauyxpsou .gt_super { font-size: 65%; }
 #rbauyxpsou .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rbauyxpsou .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rbauyxpsou .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rbauyxpsou .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rbauyxpsou .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rbauyxpsou .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rxmvgfrycd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rxmvgfrycd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rxmvgfrycd p { margin: 0; padding: 0; }
 #rxmvgfrycd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #rxmvgfrycd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rxmvgfrycd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rxmvgfrycd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rxmvgfrycd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rxmvgfrycd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #rxmvgfrycd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rxmvgfrycd .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rxmvgfrycd .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rxmvgfrycd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rxmvgfrycd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rxmvgfrycd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rxmvgfrycd .gt_spanner_row { border-bottom-style: hidden; }
 #rxmvgfrycd .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rxmvgfrycd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #rxmvgfrycd .gt_from_md> :first-child { margin-top: 0; }
 #rxmvgfrycd .gt_from_md> :last-child { margin-bottom: 0; }
 #rxmvgfrycd .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: solid; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: solid; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #rxmvgfrycd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #rxmvgfrycd .gt_indent_1 { text-indent: 5px; }
 #rxmvgfrycd .gt_indent_2 { text-indent: calc(5px * 2); }
 #rxmvgfrycd .gt_indent_3 { text-indent: calc(5px * 3); }
 #rxmvgfrycd .gt_indent_4 { text-indent: calc(5px * 4); }
 #rxmvgfrycd .gt_indent_5 { text-indent: calc(5px * 5); }
 #rxmvgfrycd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rxmvgfrycd .gt_row_group_first td { border-top-width: 2px; }
 #rxmvgfrycd .gt_row_group_first th { border-top-width: 2px; }
 #rxmvgfrycd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rxmvgfrycd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #rxmvgfrycd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rxmvgfrycd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rxmvgfrycd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rxmvgfrycd .gt_grand_summary_row { color: #FFFFFF; background-color: #00A1FF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rxmvgfrycd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rxmvgfrycd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rxmvgfrycd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rxmvgfrycd .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rxmvgfrycd .gt_left { text-align: left; }
 #rxmvgfrycd .gt_center { text-align: center; }
 #rxmvgfrycd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rxmvgfrycd .gt_font_normal { font-weight: normal; }
 #rxmvgfrycd .gt_font_bold { font-weight: bold; }
 #rxmvgfrycd .gt_font_italic { font-style: italic; }
 #rxmvgfrycd .gt_super { font-size: 65%; }
 #rxmvgfrycd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rxmvgfrycd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rxmvgfrycd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rxmvgfrycd .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rxmvgfrycd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rxmvgfrycd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#duyjqpudhr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#duyjqpudhr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#duyjqpudhr p { margin: 0; padding: 0; }
 #duyjqpudhr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #duyjqpudhr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #duyjqpudhr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #duyjqpudhr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #duyjqpudhr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #duyjqpudhr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; }
 #duyjqpudhr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #duyjqpudhr .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #duyjqpudhr .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #duyjqpudhr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #duyjqpudhr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #duyjqpudhr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #duyjqpudhr .gt_spanner_row { border-bottom-style: hidden; }
 #duyjqpudhr .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #duyjqpudhr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; vertical-align: middle; }
 #duyjqpudhr .gt_from_md> :first-child { margin-top: 0; }
 #duyjqpudhr .gt_from_md> :last-child { margin-bottom: 0; }
 #duyjqpudhr .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 1px; border-top-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #929292; border-right-style: none; border-right-width: 1px; border-right-color: #929292; vertical-align: middle; overflow-x: hidden; }
 #duyjqpudhr .gt_stub { color: #333333; background-color: #D5D5D5; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: none; border-right-width: 2px; border-right-color: #FFFFFF; padding-left: 5px; padding-right: 5px; }
 #duyjqpudhr .gt_indent_1 { text-indent: 5px; }
 #duyjqpudhr .gt_indent_2 { text-indent: calc(5px * 2); }
 #duyjqpudhr .gt_indent_3 { text-indent: calc(5px * 3); }
 #duyjqpudhr .gt_indent_4 { text-indent: calc(5px * 4); }
 #duyjqpudhr .gt_indent_5 { text-indent: calc(5px * 5); }
 #duyjqpudhr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #duyjqpudhr .gt_row_group_first td { border-top-width: 2px; }
 #duyjqpudhr .gt_row_group_first th { border-top-width: 2px; }
 #duyjqpudhr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #duyjqpudhr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; }
 #duyjqpudhr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #duyjqpudhr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #duyjqpudhr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #duyjqpudhr .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #duyjqpudhr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #duyjqpudhr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #duyjqpudhr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #duyjqpudhr .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #duyjqpudhr .gt_left { text-align: left; }
 #duyjqpudhr .gt_center { text-align: center; }
 #duyjqpudhr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #duyjqpudhr .gt_font_normal { font-weight: normal; }
 #duyjqpudhr .gt_font_bold { font-weight: bold; }
 #duyjqpudhr .gt_font_italic { font-style: italic; }
 #duyjqpudhr .gt_super { font-size: 65%; }
 #duyjqpudhr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #duyjqpudhr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #duyjqpudhr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #duyjqpudhr .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #duyjqpudhr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #duyjqpudhr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qhzlmbglgs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qhzlmbglgs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qhzlmbglgs p { margin: 0; padding: 0; }
 #qhzlmbglgs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #qhzlmbglgs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qhzlmbglgs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qhzlmbglgs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qhzlmbglgs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qhzlmbglgs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #qhzlmbglgs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qhzlmbglgs .gt_col_heading { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qhzlmbglgs .gt_column_spanner_outer { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qhzlmbglgs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qhzlmbglgs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qhzlmbglgs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qhzlmbglgs .gt_spanner_row { border-bottom-style: hidden; }
 #qhzlmbglgs .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qhzlmbglgs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #qhzlmbglgs .gt_from_md> :first-child { margin-top: 0; }
 #qhzlmbglgs .gt_from_md> :last-child { margin-bottom: 0; }
 #qhzlmbglgs .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: dashed; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: dashed; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #qhzlmbglgs .gt_stub { color: #FFFFFF; background-color: #929292; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: dashed; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #qhzlmbglgs .gt_indent_1 { text-indent: 5px; }
 #qhzlmbglgs .gt_indent_2 { text-indent: calc(5px * 2); }
 #qhzlmbglgs .gt_indent_3 { text-indent: calc(5px * 3); }
 #qhzlmbglgs .gt_indent_4 { text-indent: calc(5px * 4); }
 #qhzlmbglgs .gt_indent_5 { text-indent: calc(5px * 5); }
 #qhzlmbglgs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qhzlmbglgs .gt_row_group_first td { border-top-width: 2px; }
 #qhzlmbglgs .gt_row_group_first th { border-top-width: 2px; }
 #qhzlmbglgs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qhzlmbglgs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #qhzlmbglgs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qhzlmbglgs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qhzlmbglgs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qhzlmbglgs .gt_grand_summary_row { color: #FFFFFF; background-color: #0076BA; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qhzlmbglgs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qhzlmbglgs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qhzlmbglgs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qhzlmbglgs .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qhzlmbglgs .gt_left { text-align: left; }
 #qhzlmbglgs .gt_center { text-align: center; }
 #qhzlmbglgs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qhzlmbglgs .gt_font_normal { font-weight: normal; }
 #qhzlmbglgs .gt_font_bold { font-weight: bold; }
 #qhzlmbglgs .gt_font_italic { font-style: italic; }
 #qhzlmbglgs .gt_super { font-size: 65%; }
 #qhzlmbglgs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qhzlmbglgs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qhzlmbglgs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qhzlmbglgs .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qhzlmbglgs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qhzlmbglgs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bmacanegkm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bmacanegkm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bmacanegkm p { margin: 0; padding: 0; }
 #bmacanegkm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #bmacanegkm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bmacanegkm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bmacanegkm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bmacanegkm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bmacanegkm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #bmacanegkm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bmacanegkm .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bmacanegkm .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bmacanegkm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bmacanegkm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bmacanegkm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bmacanegkm .gt_spanner_row { border-bottom-style: hidden; }
 #bmacanegkm .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bmacanegkm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #bmacanegkm .gt_from_md> :first-child { margin-top: 0; }
 #bmacanegkm .gt_from_md> :last-child { margin-bottom: 0; }
 #bmacanegkm .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: solid; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: solid; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #bmacanegkm .gt_stub { color: #FFFFFF; background-color: #929292; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #bmacanegkm .gt_indent_1 { text-indent: 5px; }
 #bmacanegkm .gt_indent_2 { text-indent: calc(5px * 2); }
 #bmacanegkm .gt_indent_3 { text-indent: calc(5px * 3); }
 #bmacanegkm .gt_indent_4 { text-indent: calc(5px * 4); }
 #bmacanegkm .gt_indent_5 { text-indent: calc(5px * 5); }
 #bmacanegkm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bmacanegkm .gt_row_group_first td { border-top-width: 2px; }
 #bmacanegkm .gt_row_group_first th { border-top-width: 2px; }
 #bmacanegkm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bmacanegkm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #bmacanegkm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bmacanegkm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bmacanegkm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bmacanegkm .gt_grand_summary_row { color: #FFFFFF; background-color: #929292; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bmacanegkm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bmacanegkm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bmacanegkm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bmacanegkm .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bmacanegkm .gt_left { text-align: left; }
 #bmacanegkm .gt_center { text-align: center; }
 #bmacanegkm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bmacanegkm .gt_font_normal { font-weight: normal; }
 #bmacanegkm .gt_font_bold { font-weight: bold; }
 #bmacanegkm .gt_font_italic { font-style: italic; }
 #bmacanegkm .gt_super { font-size: 65%; }
 #bmacanegkm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bmacanegkm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bmacanegkm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bmacanegkm .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bmacanegkm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bmacanegkm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cmokyzpqgl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cmokyzpqgl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cmokyzpqgl p { margin: 0; padding: 0; }
 #cmokyzpqgl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cmokyzpqgl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cmokyzpqgl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cmokyzpqgl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cmokyzpqgl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cmokyzpqgl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #cmokyzpqgl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cmokyzpqgl .gt_col_heading { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cmokyzpqgl .gt_column_spanner_outer { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cmokyzpqgl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cmokyzpqgl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cmokyzpqgl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cmokyzpqgl .gt_spanner_row { border-bottom-style: hidden; }
 #cmokyzpqgl .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cmokyzpqgl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: middle; }
 #cmokyzpqgl .gt_from_md> :first-child { margin-top: 0; }
 #cmokyzpqgl .gt_from_md> :last-child { margin-bottom: 0; }
 #cmokyzpqgl .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: none; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #cmokyzpqgl .gt_stub { color: #333333; background-color: #89D3FE; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #cmokyzpqgl .gt_indent_1 { text-indent: 5px; }
 #cmokyzpqgl .gt_indent_2 { text-indent: calc(5px * 2); }
 #cmokyzpqgl .gt_indent_3 { text-indent: calc(5px * 3); }
 #cmokyzpqgl .gt_indent_4 { text-indent: calc(5px * 4); }
 #cmokyzpqgl .gt_indent_5 { text-indent: calc(5px * 5); }
 #cmokyzpqgl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cmokyzpqgl .gt_row_group_first td { border-top-width: 2px; }
 #cmokyzpqgl .gt_row_group_first th { border-top-width: 2px; }
 #cmokyzpqgl .gt_striped { color: #333333; background-color: #EDF7FC; }
 #cmokyzpqgl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #cmokyzpqgl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cmokyzpqgl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cmokyzpqgl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cmokyzpqgl .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cmokyzpqgl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cmokyzpqgl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cmokyzpqgl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cmokyzpqgl .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cmokyzpqgl .gt_left { text-align: left; }
 #cmokyzpqgl .gt_center { text-align: center; }
 #cmokyzpqgl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cmokyzpqgl .gt_font_normal { font-weight: normal; }
 #cmokyzpqgl .gt_font_bold { font-weight: bold; }
 #cmokyzpqgl .gt_font_italic { font-style: italic; }
 #cmokyzpqgl .gt_super { font-size: 65%; }
 #cmokyzpqgl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cmokyzpqgl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cmokyzpqgl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cmokyzpqgl .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cmokyzpqgl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cmokyzpqgl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ztqrvtcbdz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ztqrvtcbdz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ztqrvtcbdz p { margin: 0; padding: 0; }
 #ztqrvtcbdz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ztqrvtcbdz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ztqrvtcbdz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ztqrvtcbdz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ztqrvtcbdz .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ztqrvtcbdz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ztqrvtcbdz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ztqrvtcbdz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ztqrvtcbdz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ztqrvtcbdz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ztqrvtcbdz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ztqrvtcbdz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ztqrvtcbdz .gt_spanner_row { border-bottom-style: hidden; }
 #ztqrvtcbdz .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ztqrvtcbdz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ztqrvtcbdz .gt_from_md> :first-child { margin-top: 0; }
 #ztqrvtcbdz .gt_from_md> :last-child { margin-bottom: 0; }
 #ztqrvtcbdz .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ztqrvtcbdz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ztqrvtcbdz .gt_indent_1 { text-indent: 5px; }
 #ztqrvtcbdz .gt_indent_2 { text-indent: calc(5px * 2); }
 #ztqrvtcbdz .gt_indent_3 { text-indent: calc(5px * 3); }
 #ztqrvtcbdz .gt_indent_4 { text-indent: calc(5px * 4); }
 #ztqrvtcbdz .gt_indent_5 { text-indent: calc(5px * 5); }
 #ztqrvtcbdz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ztqrvtcbdz .gt_row_group_first td { border-top-width: 2px; }
 #ztqrvtcbdz .gt_row_group_first th { border-top-width: 2px; }
 #ztqrvtcbdz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ztqrvtcbdz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ztqrvtcbdz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ztqrvtcbdz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ztqrvtcbdz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ztqrvtcbdz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ztqrvtcbdz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ztqrvtcbdz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ztqrvtcbdz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ztqrvtcbdz .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ztqrvtcbdz .gt_left { text-align: left; }
 #ztqrvtcbdz .gt_center { text-align: center; }
 #ztqrvtcbdz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ztqrvtcbdz .gt_font_normal { font-weight: normal; }
 #ztqrvtcbdz .gt_font_bold { font-weight: bold; }
 #ztqrvtcbdz .gt_font_italic { font-style: italic; }
 #ztqrvtcbdz .gt_super { font-size: 65%; }
 #ztqrvtcbdz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ztqrvtcbdz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ztqrvtcbdz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ztqrvtcbdz .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ztqrvtcbdz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ztqrvtcbdz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vabndnpeil table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vabndnpeil thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vabndnpeil p { margin: 0; padding: 0; }
 #vabndnpeil .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vabndnpeil .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vabndnpeil .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vabndnpeil .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vabndnpeil .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vabndnpeil .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vabndnpeil .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vabndnpeil .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vabndnpeil .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vabndnpeil .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vabndnpeil .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vabndnpeil .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vabndnpeil .gt_spanner_row { border-bottom-style: hidden; }
 #vabndnpeil .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vabndnpeil .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vabndnpeil .gt_from_md> :first-child { margin-top: 0; }
 #vabndnpeil .gt_from_md> :last-child { margin-bottom: 0; }
 #vabndnpeil .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vabndnpeil .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vabndnpeil .gt_indent_1 { text-indent: 5px; }
 #vabndnpeil .gt_indent_2 { text-indent: calc(5px * 2); }
 #vabndnpeil .gt_indent_3 { text-indent: calc(5px * 3); }
 #vabndnpeil .gt_indent_4 { text-indent: calc(5px * 4); }
 #vabndnpeil .gt_indent_5 { text-indent: calc(5px * 5); }
 #vabndnpeil .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vabndnpeil .gt_row_group_first td { border-top-width: 2px; }
 #vabndnpeil .gt_row_group_first th { border-top-width: 2px; }
 #vabndnpeil .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vabndnpeil .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vabndnpeil .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vabndnpeil .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vabndnpeil .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vabndnpeil .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vabndnpeil .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vabndnpeil .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vabndnpeil .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vabndnpeil .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vabndnpeil .gt_left { text-align: left; }
 #vabndnpeil .gt_center { text-align: center; }
 #vabndnpeil .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vabndnpeil .gt_font_normal { font-weight: normal; }
 #vabndnpeil .gt_font_bold { font-weight: bold; }
 #vabndnpeil .gt_font_italic { font-style: italic; }
 #vabndnpeil .gt_super { font-size: 65%; }
 #vabndnpeil .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vabndnpeil .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vabndnpeil .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vabndnpeil .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vabndnpeil .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vabndnpeil .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xqamwylihs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xqamwylihs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xqamwylihs p { margin: 0; padding: 0; }
 #xqamwylihs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xqamwylihs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xqamwylihs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xqamwylihs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: -0.4px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xqamwylihs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xqamwylihs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xqamwylihs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xqamwylihs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 0.75px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xqamwylihs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xqamwylihs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xqamwylihs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xqamwylihs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 0.75px; padding-bottom: 0.75px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xqamwylihs .gt_spanner_row { border-bottom-style: hidden; }
 #xqamwylihs .gt_group_heading { padding-top: 1.2px; padding-bottom: 1.2px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xqamwylihs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xqamwylihs .gt_from_md> :first-child { margin-top: 0; }
 #xqamwylihs .gt_from_md> :last-child { margin-bottom: 0; }
 #xqamwylihs .gt_row { padding-top: 1.2px; padding-bottom: 1.2px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xqamwylihs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xqamwylihs .gt_indent_1 { text-indent: 5px; }
 #xqamwylihs .gt_indent_2 { text-indent: calc(5px * 2); }
 #xqamwylihs .gt_indent_3 { text-indent: calc(5px * 3); }
 #xqamwylihs .gt_indent_4 { text-indent: calc(5px * 4); }
 #xqamwylihs .gt_indent_5 { text-indent: calc(5px * 5); }
 #xqamwylihs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xqamwylihs .gt_row_group_first td { border-top-width: 2px; }
 #xqamwylihs .gt_row_group_first th { border-top-width: 2px; }
 #xqamwylihs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xqamwylihs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xqamwylihs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xqamwylihs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xqamwylihs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xqamwylihs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xqamwylihs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xqamwylihs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xqamwylihs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xqamwylihs .gt_sourcenote { font-size: 90%; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xqamwylihs .gt_left { text-align: left; }
 #xqamwylihs .gt_center { text-align: center; }
 #xqamwylihs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xqamwylihs .gt_font_normal { font-weight: normal; }
 #xqamwylihs .gt_font_bold { font-weight: bold; }
 #xqamwylihs .gt_font_italic { font-style: italic; }
 #xqamwylihs .gt_super { font-size: 65%; }
 #xqamwylihs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xqamwylihs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xqamwylihs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xqamwylihs .gt_sourcenote { font-size: 90%; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xqamwylihs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xqamwylihs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zkwwekzqzu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zkwwekzqzu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zkwwekzqzu p { margin: 0; padding: 0; }
 #zkwwekzqzu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zkwwekzqzu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zkwwekzqzu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zkwwekzqzu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 15px; padding-right: 15px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zkwwekzqzu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zkwwekzqzu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zkwwekzqzu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zkwwekzqzu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 15px; padding-right: 15px; overflow-x: hidden; }
 #zkwwekzqzu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zkwwekzqzu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zkwwekzqzu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zkwwekzqzu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zkwwekzqzu .gt_spanner_row { border-bottom-style: hidden; }
 #zkwwekzqzu .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zkwwekzqzu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zkwwekzqzu .gt_from_md> :first-child { margin-top: 0; }
 #zkwwekzqzu .gt_from_md> :last-child { margin-bottom: 0; }
 #zkwwekzqzu .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zkwwekzqzu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; }
 #zkwwekzqzu .gt_indent_1 { text-indent: 5px; }
 #zkwwekzqzu .gt_indent_2 { text-indent: calc(5px * 2); }
 #zkwwekzqzu .gt_indent_3 { text-indent: calc(5px * 3); }
 #zkwwekzqzu .gt_indent_4 { text-indent: calc(5px * 4); }
 #zkwwekzqzu .gt_indent_5 { text-indent: calc(5px * 5); }
 #zkwwekzqzu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; vertical-align: top; }
 #zkwwekzqzu .gt_row_group_first td { border-top-width: 2px; }
 #zkwwekzqzu .gt_row_group_first th { border-top-width: 2px; }
 #zkwwekzqzu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zkwwekzqzu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zkwwekzqzu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zkwwekzqzu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zkwwekzqzu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zkwwekzqzu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zkwwekzqzu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zkwwekzqzu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zkwwekzqzu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zkwwekzqzu .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #zkwwekzqzu .gt_left { text-align: left; }
 #zkwwekzqzu .gt_center { text-align: center; }
 #zkwwekzqzu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zkwwekzqzu .gt_font_normal { font-weight: normal; }
 #zkwwekzqzu .gt_font_bold { font-weight: bold; }
 #zkwwekzqzu .gt_font_italic { font-style: italic; }
 #zkwwekzqzu .gt_super { font-size: 65%; }
 #zkwwekzqzu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zkwwekzqzu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zkwwekzqzu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zkwwekzqzu .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #zkwwekzqzu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zkwwekzqzu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qfbnkfyipu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qfbnkfyipu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qfbnkfyipu p { margin: 0; padding: 0; }
 #qfbnkfyipu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D3D3D3; border-right-style: solid; border-right-width: 3px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D3D3D3; border-left-style: solid; border-left-width: 3px; border-left-color: #D3D3D3; }
 #qfbnkfyipu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qfbnkfyipu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qfbnkfyipu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qfbnkfyipu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qfbnkfyipu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qfbnkfyipu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qfbnkfyipu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qfbnkfyipu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qfbnkfyipu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qfbnkfyipu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qfbnkfyipu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qfbnkfyipu .gt_spanner_row { border-bottom-style: hidden; }
 #qfbnkfyipu .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qfbnkfyipu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qfbnkfyipu .gt_from_md> :first-child { margin-top: 0; }
 #qfbnkfyipu .gt_from_md> :last-child { margin-bottom: 0; }
 #qfbnkfyipu .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qfbnkfyipu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qfbnkfyipu .gt_indent_1 { text-indent: 5px; }
 #qfbnkfyipu .gt_indent_2 { text-indent: calc(5px * 2); }
 #qfbnkfyipu .gt_indent_3 { text-indent: calc(5px * 3); }
 #qfbnkfyipu .gt_indent_4 { text-indent: calc(5px * 4); }
 #qfbnkfyipu .gt_indent_5 { text-indent: calc(5px * 5); }
 #qfbnkfyipu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qfbnkfyipu .gt_row_group_first td { border-top-width: 2px; }
 #qfbnkfyipu .gt_row_group_first th { border-top-width: 2px; }
 #qfbnkfyipu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qfbnkfyipu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qfbnkfyipu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qfbnkfyipu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qfbnkfyipu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qfbnkfyipu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qfbnkfyipu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qfbnkfyipu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qfbnkfyipu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qfbnkfyipu .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qfbnkfyipu .gt_left { text-align: left; }
 #qfbnkfyipu .gt_center { text-align: center; }
 #qfbnkfyipu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qfbnkfyipu .gt_font_normal { font-weight: normal; }
 #qfbnkfyipu .gt_font_bold { font-weight: bold; }
 #qfbnkfyipu .gt_font_italic { font-style: italic; }
 #qfbnkfyipu .gt_super { font-size: 65%; }
 #qfbnkfyipu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qfbnkfyipu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qfbnkfyipu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qfbnkfyipu .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qfbnkfyipu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qfbnkfyipu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
