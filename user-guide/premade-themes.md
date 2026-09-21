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
#uvqzgeyjim table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uvqzgeyjim thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uvqzgeyjim p { margin: 0; padding: 0; }
 #uvqzgeyjim .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uvqzgeyjim .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uvqzgeyjim .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uvqzgeyjim .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uvqzgeyjim .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uvqzgeyjim .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvqzgeyjim .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uvqzgeyjim .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uvqzgeyjim .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uvqzgeyjim .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uvqzgeyjim .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uvqzgeyjim .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uvqzgeyjim .gt_spanner_row { border-bottom-style: hidden; }
 #uvqzgeyjim .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uvqzgeyjim .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uvqzgeyjim .gt_from_md> :first-child { margin-top: 0; }
 #uvqzgeyjim .gt_from_md> :last-child { margin-bottom: 0; }
 #uvqzgeyjim .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uvqzgeyjim .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uvqzgeyjim .gt_indent_1 { text-indent: 5px; }
 #uvqzgeyjim .gt_indent_2 { text-indent: calc(5px * 2); }
 #uvqzgeyjim .gt_indent_3 { text-indent: calc(5px * 3); }
 #uvqzgeyjim .gt_indent_4 { text-indent: calc(5px * 4); }
 #uvqzgeyjim .gt_indent_5 { text-indent: calc(5px * 5); }
 #uvqzgeyjim .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uvqzgeyjim .gt_row_group_first td { border-top-width: 2px; }
 #uvqzgeyjim .gt_row_group_first th { border-top-width: 2px; }
 #uvqzgeyjim .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uvqzgeyjim .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvqzgeyjim .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uvqzgeyjim .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uvqzgeyjim .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvqzgeyjim .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uvqzgeyjim .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uvqzgeyjim .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uvqzgeyjim .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvqzgeyjim .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uvqzgeyjim .gt_left { text-align: left; }
 #uvqzgeyjim .gt_center { text-align: center; }
 #uvqzgeyjim .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uvqzgeyjim .gt_font_normal { font-weight: normal; }
 #uvqzgeyjim .gt_font_bold { font-weight: bold; }
 #uvqzgeyjim .gt_font_italic { font-style: italic; }
 #uvqzgeyjim .gt_super { font-size: 65%; }
 #uvqzgeyjim .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvqzgeyjim .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uvqzgeyjim .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvqzgeyjim .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uvqzgeyjim .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uvqzgeyjim .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
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
#ejjgjjndru table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ejjgjjndru thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ejjgjjndru p { margin: 0; padding: 0; }
 #ejjgjjndru .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ejjgjjndru .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ejjgjjndru .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ejjgjjndru .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ejjgjjndru .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ejjgjjndru .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #ejjgjjndru .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ejjgjjndru .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ejjgjjndru .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ejjgjjndru .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ejjgjjndru .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ejjgjjndru .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ejjgjjndru .gt_spanner_row { border-bottom-style: hidden; }
 #ejjgjjndru .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ejjgjjndru .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #ejjgjjndru .gt_from_md> :first-child { margin-top: 0; }
 #ejjgjjndru .gt_from_md> :last-child { margin-bottom: 0; }
 #ejjgjjndru .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #ejjgjjndru .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #ejjgjjndru .gt_indent_1 { text-indent: 5px; }
 #ejjgjjndru .gt_indent_2 { text-indent: calc(5px * 2); }
 #ejjgjjndru .gt_indent_3 { text-indent: calc(5px * 3); }
 #ejjgjjndru .gt_indent_4 { text-indent: calc(5px * 4); }
 #ejjgjjndru .gt_indent_5 { text-indent: calc(5px * 5); }
 #ejjgjjndru .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ejjgjjndru .gt_row_group_first td { border-top-width: 2px; }
 #ejjgjjndru .gt_row_group_first th { border-top-width: 2px; }
 #ejjgjjndru .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ejjgjjndru .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #ejjgjjndru .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ejjgjjndru .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ejjgjjndru .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ejjgjjndru .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ejjgjjndru .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ejjgjjndru .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ejjgjjndru .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ejjgjjndru .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ejjgjjndru .gt_left { text-align: left; }
 #ejjgjjndru .gt_center { text-align: center; }
 #ejjgjjndru .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ejjgjjndru .gt_font_normal { font-weight: normal; }
 #ejjgjjndru .gt_font_bold { font-weight: bold; }
 #ejjgjjndru .gt_font_italic { font-style: italic; }
 #ejjgjjndru .gt_super { font-size: 65%; }
 #ejjgjjndru .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ejjgjjndru .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ejjgjjndru .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ejjgjjndru .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ejjgjjndru .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ejjgjjndru .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
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
#ctarfpjicf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ctarfpjicf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ctarfpjicf p { margin: 0; padding: 0; }
 #ctarfpjicf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #ctarfpjicf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ctarfpjicf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ctarfpjicf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ctarfpjicf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ctarfpjicf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #ctarfpjicf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ctarfpjicf .gt_col_heading { color: #FFFFFF; background-color: #A81600; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ctarfpjicf .gt_column_spanner_outer { color: #FFFFFF; background-color: #A81600; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ctarfpjicf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ctarfpjicf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ctarfpjicf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ctarfpjicf .gt_spanner_row { border-bottom-style: hidden; }
 #ctarfpjicf .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ctarfpjicf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #ctarfpjicf .gt_from_md> :first-child { margin-top: 0; }
 #ctarfpjicf .gt_from_md> :last-child { margin-bottom: 0; }
 #ctarfpjicf .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #FFCCC7; border-left-style: solid; border-left-width: 1px; border-left-color: #FFCCC7; border-right-style: solid; border-right-width: 1px; border-right-color: #FFCCC7; vertical-align: middle; overflow-x: hidden; }
 #ctarfpjicf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #ctarfpjicf .gt_indent_1 { text-indent: 5px; }
 #ctarfpjicf .gt_indent_2 { text-indent: calc(5px * 2); }
 #ctarfpjicf .gt_indent_3 { text-indent: calc(5px * 3); }
 #ctarfpjicf .gt_indent_4 { text-indent: calc(5px * 4); }
 #ctarfpjicf .gt_indent_5 { text-indent: calc(5px * 5); }
 #ctarfpjicf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ctarfpjicf .gt_row_group_first td { border-top-width: 2px; }
 #ctarfpjicf .gt_row_group_first th { border-top-width: 2px; }
 #ctarfpjicf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ctarfpjicf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #ctarfpjicf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ctarfpjicf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ctarfpjicf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ctarfpjicf .gt_grand_summary_row { color: #333333; background-color: #FF644E; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ctarfpjicf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ctarfpjicf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ctarfpjicf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ctarfpjicf .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ctarfpjicf .gt_left { text-align: left; }
 #ctarfpjicf .gt_center { text-align: center; }
 #ctarfpjicf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ctarfpjicf .gt_font_normal { font-weight: normal; }
 #ctarfpjicf .gt_font_bold { font-weight: bold; }
 #ctarfpjicf .gt_font_italic { font-style: italic; }
 #ctarfpjicf .gt_super { font-size: 65%; }
 #ctarfpjicf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ctarfpjicf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ctarfpjicf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ctarfpjicf .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ctarfpjicf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ctarfpjicf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
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
#rrmyxtiocb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rrmyxtiocb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rrmyxtiocb p { margin: 0; padding: 0; }
 #rrmyxtiocb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rrmyxtiocb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rrmyxtiocb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rrmyxtiocb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rrmyxtiocb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rrmyxtiocb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #rrmyxtiocb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rrmyxtiocb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rrmyxtiocb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rrmyxtiocb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rrmyxtiocb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rrmyxtiocb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rrmyxtiocb .gt_spanner_row { border-bottom-style: hidden; }
 #rrmyxtiocb .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rrmyxtiocb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #rrmyxtiocb .gt_from_md> :first-child { margin-top: 0; }
 #rrmyxtiocb .gt_from_md> :last-child { margin-bottom: 0; }
 #rrmyxtiocb .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #rrmyxtiocb .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #rrmyxtiocb .gt_indent_1 { text-indent: 5px; }
 #rrmyxtiocb .gt_indent_2 { text-indent: calc(5px * 2); }
 #rrmyxtiocb .gt_indent_3 { text-indent: calc(5px * 3); }
 #rrmyxtiocb .gt_indent_4 { text-indent: calc(5px * 4); }
 #rrmyxtiocb .gt_indent_5 { text-indent: calc(5px * 5); }
 #rrmyxtiocb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rrmyxtiocb .gt_row_group_first td { border-top-width: 2px; }
 #rrmyxtiocb .gt_row_group_first th { border-top-width: 2px; }
 #rrmyxtiocb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rrmyxtiocb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #rrmyxtiocb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rrmyxtiocb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rrmyxtiocb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rrmyxtiocb .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rrmyxtiocb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rrmyxtiocb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rrmyxtiocb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rrmyxtiocb .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rrmyxtiocb .gt_left { text-align: left; }
 #rrmyxtiocb .gt_center { text-align: center; }
 #rrmyxtiocb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rrmyxtiocb .gt_font_normal { font-weight: normal; }
 #rrmyxtiocb .gt_font_bold { font-weight: bold; }
 #rrmyxtiocb .gt_font_italic { font-style: italic; }
 #rrmyxtiocb .gt_super { font-size: 65%; }
 #rrmyxtiocb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rrmyxtiocb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rrmyxtiocb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rrmyxtiocb .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rrmyxtiocb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rrmyxtiocb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


2


<style>
#kmdwpzwbst table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kmdwpzwbst thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kmdwpzwbst p { margin: 0; padding: 0; }
 #kmdwpzwbst .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #kmdwpzwbst .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kmdwpzwbst .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kmdwpzwbst .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kmdwpzwbst .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kmdwpzwbst .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #kmdwpzwbst .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kmdwpzwbst .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kmdwpzwbst .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kmdwpzwbst .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kmdwpzwbst .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kmdwpzwbst .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kmdwpzwbst .gt_spanner_row { border-bottom-style: hidden; }
 #kmdwpzwbst .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kmdwpzwbst .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #kmdwpzwbst .gt_from_md> :first-child { margin-top: 0; }
 #kmdwpzwbst .gt_from_md> :last-child { margin-bottom: 0; }
 #kmdwpzwbst .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: solid; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: solid; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #kmdwpzwbst .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #kmdwpzwbst .gt_indent_1 { text-indent: 5px; }
 #kmdwpzwbst .gt_indent_2 { text-indent: calc(5px * 2); }
 #kmdwpzwbst .gt_indent_3 { text-indent: calc(5px * 3); }
 #kmdwpzwbst .gt_indent_4 { text-indent: calc(5px * 4); }
 #kmdwpzwbst .gt_indent_5 { text-indent: calc(5px * 5); }
 #kmdwpzwbst .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kmdwpzwbst .gt_row_group_first td { border-top-width: 2px; }
 #kmdwpzwbst .gt_row_group_first th { border-top-width: 2px; }
 #kmdwpzwbst .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kmdwpzwbst .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #kmdwpzwbst .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kmdwpzwbst .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kmdwpzwbst .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kmdwpzwbst .gt_grand_summary_row { color: #333333; background-color: #00A1FF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kmdwpzwbst .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kmdwpzwbst .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kmdwpzwbst .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kmdwpzwbst .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kmdwpzwbst .gt_left { text-align: left; }
 #kmdwpzwbst .gt_center { text-align: center; }
 #kmdwpzwbst .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kmdwpzwbst .gt_font_normal { font-weight: normal; }
 #kmdwpzwbst .gt_font_bold { font-weight: bold; }
 #kmdwpzwbst .gt_font_italic { font-style: italic; }
 #kmdwpzwbst .gt_super { font-size: 65%; }
 #kmdwpzwbst .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kmdwpzwbst .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kmdwpzwbst .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kmdwpzwbst .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kmdwpzwbst .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kmdwpzwbst .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


3


<style>
#rtitqsyclb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rtitqsyclb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rtitqsyclb p { margin: 0; padding: 0; }
 #rtitqsyclb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rtitqsyclb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rtitqsyclb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rtitqsyclb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rtitqsyclb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rtitqsyclb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; }
 #rtitqsyclb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rtitqsyclb .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rtitqsyclb .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rtitqsyclb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rtitqsyclb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rtitqsyclb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rtitqsyclb .gt_spanner_row { border-bottom-style: hidden; }
 #rtitqsyclb .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rtitqsyclb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; vertical-align: middle; }
 #rtitqsyclb .gt_from_md> :first-child { margin-top: 0; }
 #rtitqsyclb .gt_from_md> :last-child { margin-bottom: 0; }
 #rtitqsyclb .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 1px; border-top-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #929292; border-right-style: none; border-right-width: 1px; border-right-color: #929292; vertical-align: middle; overflow-x: hidden; }
 #rtitqsyclb .gt_stub { color: #333333; background-color: #D5D5D5; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: none; border-right-width: 2px; border-right-color: #FFFFFF; padding-left: 5px; padding-right: 5px; }
 #rtitqsyclb .gt_indent_1 { text-indent: 5px; }
 #rtitqsyclb .gt_indent_2 { text-indent: calc(5px * 2); }
 #rtitqsyclb .gt_indent_3 { text-indent: calc(5px * 3); }
 #rtitqsyclb .gt_indent_4 { text-indent: calc(5px * 4); }
 #rtitqsyclb .gt_indent_5 { text-indent: calc(5px * 5); }
 #rtitqsyclb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rtitqsyclb .gt_row_group_first td { border-top-width: 2px; }
 #rtitqsyclb .gt_row_group_first th { border-top-width: 2px; }
 #rtitqsyclb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rtitqsyclb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; }
 #rtitqsyclb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rtitqsyclb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rtitqsyclb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rtitqsyclb .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rtitqsyclb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rtitqsyclb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rtitqsyclb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rtitqsyclb .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rtitqsyclb .gt_left { text-align: left; }
 #rtitqsyclb .gt_center { text-align: center; }
 #rtitqsyclb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rtitqsyclb .gt_font_normal { font-weight: normal; }
 #rtitqsyclb .gt_font_bold { font-weight: bold; }
 #rtitqsyclb .gt_font_italic { font-style: italic; }
 #rtitqsyclb .gt_super { font-size: 65%; }
 #rtitqsyclb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rtitqsyclb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rtitqsyclb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rtitqsyclb .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rtitqsyclb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rtitqsyclb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


4


<style>
#bafiakjdum table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bafiakjdum thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bafiakjdum p { margin: 0; padding: 0; }
 #bafiakjdum .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #bafiakjdum .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bafiakjdum .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bafiakjdum .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bafiakjdum .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bafiakjdum .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #bafiakjdum .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bafiakjdum .gt_col_heading { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bafiakjdum .gt_column_spanner_outer { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bafiakjdum .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bafiakjdum .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bafiakjdum .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bafiakjdum .gt_spanner_row { border-bottom-style: hidden; }
 #bafiakjdum .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bafiakjdum .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #bafiakjdum .gt_from_md> :first-child { margin-top: 0; }
 #bafiakjdum .gt_from_md> :last-child { margin-bottom: 0; }
 #bafiakjdum .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: dashed; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: dashed; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #bafiakjdum .gt_stub { color: #333333; background-color: #929292; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: dashed; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #bafiakjdum .gt_indent_1 { text-indent: 5px; }
 #bafiakjdum .gt_indent_2 { text-indent: calc(5px * 2); }
 #bafiakjdum .gt_indent_3 { text-indent: calc(5px * 3); }
 #bafiakjdum .gt_indent_4 { text-indent: calc(5px * 4); }
 #bafiakjdum .gt_indent_5 { text-indent: calc(5px * 5); }
 #bafiakjdum .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bafiakjdum .gt_row_group_first td { border-top-width: 2px; }
 #bafiakjdum .gt_row_group_first th { border-top-width: 2px; }
 #bafiakjdum .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bafiakjdum .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #bafiakjdum .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bafiakjdum .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bafiakjdum .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bafiakjdum .gt_grand_summary_row { color: #FFFFFF; background-color: #0076BA; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bafiakjdum .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bafiakjdum .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bafiakjdum .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bafiakjdum .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bafiakjdum .gt_left { text-align: left; }
 #bafiakjdum .gt_center { text-align: center; }
 #bafiakjdum .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bafiakjdum .gt_font_normal { font-weight: normal; }
 #bafiakjdum .gt_font_bold { font-weight: bold; }
 #bafiakjdum .gt_font_italic { font-style: italic; }
 #bafiakjdum .gt_super { font-size: 65%; }
 #bafiakjdum .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bafiakjdum .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bafiakjdum .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bafiakjdum .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bafiakjdum .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bafiakjdum .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


5


<style>
#jfwfesnnbt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jfwfesnnbt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jfwfesnnbt p { margin: 0; padding: 0; }
 #jfwfesnnbt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #jfwfesnnbt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jfwfesnnbt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jfwfesnnbt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jfwfesnnbt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jfwfesnnbt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #jfwfesnnbt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jfwfesnnbt .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jfwfesnnbt .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jfwfesnnbt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jfwfesnnbt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jfwfesnnbt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jfwfesnnbt .gt_spanner_row { border-bottom-style: hidden; }
 #jfwfesnnbt .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jfwfesnnbt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #jfwfesnnbt .gt_from_md> :first-child { margin-top: 0; }
 #jfwfesnnbt .gt_from_md> :last-child { margin-bottom: 0; }
 #jfwfesnnbt .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: solid; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: solid; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #jfwfesnnbt .gt_stub { color: #333333; background-color: #929292; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #jfwfesnnbt .gt_indent_1 { text-indent: 5px; }
 #jfwfesnnbt .gt_indent_2 { text-indent: calc(5px * 2); }
 #jfwfesnnbt .gt_indent_3 { text-indent: calc(5px * 3); }
 #jfwfesnnbt .gt_indent_4 { text-indent: calc(5px * 4); }
 #jfwfesnnbt .gt_indent_5 { text-indent: calc(5px * 5); }
 #jfwfesnnbt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jfwfesnnbt .gt_row_group_first td { border-top-width: 2px; }
 #jfwfesnnbt .gt_row_group_first th { border-top-width: 2px; }
 #jfwfesnnbt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jfwfesnnbt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #jfwfesnnbt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jfwfesnnbt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jfwfesnnbt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jfwfesnnbt .gt_grand_summary_row { color: #333333; background-color: #929292; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jfwfesnnbt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jfwfesnnbt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jfwfesnnbt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jfwfesnnbt .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jfwfesnnbt .gt_left { text-align: left; }
 #jfwfesnnbt .gt_center { text-align: center; }
 #jfwfesnnbt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jfwfesnnbt .gt_font_normal { font-weight: normal; }
 #jfwfesnnbt .gt_font_bold { font-weight: bold; }
 #jfwfesnnbt .gt_font_italic { font-style: italic; }
 #jfwfesnnbt .gt_super { font-size: 65%; }
 #jfwfesnnbt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jfwfesnnbt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jfwfesnnbt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jfwfesnnbt .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jfwfesnnbt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jfwfesnnbt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


6


<style>
#sbnuvpwbvq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sbnuvpwbvq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sbnuvpwbvq p { margin: 0; padding: 0; }
 #sbnuvpwbvq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sbnuvpwbvq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sbnuvpwbvq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sbnuvpwbvq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sbnuvpwbvq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sbnuvpwbvq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #sbnuvpwbvq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sbnuvpwbvq .gt_col_heading { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sbnuvpwbvq .gt_column_spanner_outer { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sbnuvpwbvq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sbnuvpwbvq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sbnuvpwbvq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sbnuvpwbvq .gt_spanner_row { border-bottom-style: hidden; }
 #sbnuvpwbvq .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sbnuvpwbvq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: middle; }
 #sbnuvpwbvq .gt_from_md> :first-child { margin-top: 0; }
 #sbnuvpwbvq .gt_from_md> :last-child { margin-bottom: 0; }
 #sbnuvpwbvq .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: none; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #sbnuvpwbvq .gt_stub { color: #333333; background-color: #89D3FE; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #sbnuvpwbvq .gt_indent_1 { text-indent: 5px; }
 #sbnuvpwbvq .gt_indent_2 { text-indent: calc(5px * 2); }
 #sbnuvpwbvq .gt_indent_3 { text-indent: calc(5px * 3); }
 #sbnuvpwbvq .gt_indent_4 { text-indent: calc(5px * 4); }
 #sbnuvpwbvq .gt_indent_5 { text-indent: calc(5px * 5); }
 #sbnuvpwbvq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sbnuvpwbvq .gt_row_group_first td { border-top-width: 2px; }
 #sbnuvpwbvq .gt_row_group_first th { border-top-width: 2px; }
 #sbnuvpwbvq .gt_striped { color: #333333; background-color: #EDF7FC; }
 #sbnuvpwbvq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #sbnuvpwbvq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sbnuvpwbvq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sbnuvpwbvq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sbnuvpwbvq .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sbnuvpwbvq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sbnuvpwbvq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sbnuvpwbvq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbnuvpwbvq .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sbnuvpwbvq .gt_left { text-align: left; }
 #sbnuvpwbvq .gt_center { text-align: center; }
 #sbnuvpwbvq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sbnuvpwbvq .gt_font_normal { font-weight: normal; }
 #sbnuvpwbvq .gt_font_bold { font-weight: bold; }
 #sbnuvpwbvq .gt_font_italic { font-style: italic; }
 #sbnuvpwbvq .gt_super { font-size: 65%; }
 #sbnuvpwbvq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbnuvpwbvq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sbnuvpwbvq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbnuvpwbvq .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sbnuvpwbvq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sbnuvpwbvq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
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
#zxphwyhbqj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zxphwyhbqj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zxphwyhbqj p { margin: 0; padding: 0; }
 #zxphwyhbqj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zxphwyhbqj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zxphwyhbqj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zxphwyhbqj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zxphwyhbqj .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zxphwyhbqj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxphwyhbqj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zxphwyhbqj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zxphwyhbqj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zxphwyhbqj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zxphwyhbqj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zxphwyhbqj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zxphwyhbqj .gt_spanner_row { border-bottom-style: hidden; }
 #zxphwyhbqj .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zxphwyhbqj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zxphwyhbqj .gt_from_md> :first-child { margin-top: 0; }
 #zxphwyhbqj .gt_from_md> :last-child { margin-bottom: 0; }
 #zxphwyhbqj .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zxphwyhbqj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zxphwyhbqj .gt_indent_1 { text-indent: 5px; }
 #zxphwyhbqj .gt_indent_2 { text-indent: calc(5px * 2); }
 #zxphwyhbqj .gt_indent_3 { text-indent: calc(5px * 3); }
 #zxphwyhbqj .gt_indent_4 { text-indent: calc(5px * 4); }
 #zxphwyhbqj .gt_indent_5 { text-indent: calc(5px * 5); }
 #zxphwyhbqj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zxphwyhbqj .gt_row_group_first td { border-top-width: 2px; }
 #zxphwyhbqj .gt_row_group_first th { border-top-width: 2px; }
 #zxphwyhbqj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zxphwyhbqj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxphwyhbqj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zxphwyhbqj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zxphwyhbqj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxphwyhbqj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zxphwyhbqj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zxphwyhbqj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zxphwyhbqj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxphwyhbqj .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zxphwyhbqj .gt_left { text-align: left; }
 #zxphwyhbqj .gt_center { text-align: center; }
 #zxphwyhbqj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zxphwyhbqj .gt_font_normal { font-weight: normal; }
 #zxphwyhbqj .gt_font_bold { font-weight: bold; }
 #zxphwyhbqj .gt_font_italic { font-style: italic; }
 #zxphwyhbqj .gt_super { font-size: 65%; }
 #zxphwyhbqj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxphwyhbqj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zxphwyhbqj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxphwyhbqj .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zxphwyhbqj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zxphwyhbqj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
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
#unvljhrfcq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#unvljhrfcq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#unvljhrfcq p { margin: 0; padding: 0; }
 #unvljhrfcq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #unvljhrfcq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #unvljhrfcq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #unvljhrfcq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #unvljhrfcq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #unvljhrfcq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #unvljhrfcq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #unvljhrfcq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #unvljhrfcq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #unvljhrfcq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #unvljhrfcq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #unvljhrfcq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #unvljhrfcq .gt_spanner_row { border-bottom-style: hidden; }
 #unvljhrfcq .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #unvljhrfcq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #unvljhrfcq .gt_from_md> :first-child { margin-top: 0; }
 #unvljhrfcq .gt_from_md> :last-child { margin-bottom: 0; }
 #unvljhrfcq .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #unvljhrfcq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #unvljhrfcq .gt_indent_1 { text-indent: 5px; }
 #unvljhrfcq .gt_indent_2 { text-indent: calc(5px * 2); }
 #unvljhrfcq .gt_indent_3 { text-indent: calc(5px * 3); }
 #unvljhrfcq .gt_indent_4 { text-indent: calc(5px * 4); }
 #unvljhrfcq .gt_indent_5 { text-indent: calc(5px * 5); }
 #unvljhrfcq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #unvljhrfcq .gt_row_group_first td { border-top-width: 2px; }
 #unvljhrfcq .gt_row_group_first th { border-top-width: 2px; }
 #unvljhrfcq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #unvljhrfcq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #unvljhrfcq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #unvljhrfcq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #unvljhrfcq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #unvljhrfcq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #unvljhrfcq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #unvljhrfcq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #unvljhrfcq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #unvljhrfcq .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #unvljhrfcq .gt_left { text-align: left; }
 #unvljhrfcq .gt_center { text-align: center; }
 #unvljhrfcq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #unvljhrfcq .gt_font_normal { font-weight: normal; }
 #unvljhrfcq .gt_font_bold { font-weight: bold; }
 #unvljhrfcq .gt_font_italic { font-style: italic; }
 #unvljhrfcq .gt_super { font-size: 65%; }
 #unvljhrfcq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #unvljhrfcq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #unvljhrfcq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #unvljhrfcq .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #unvljhrfcq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #unvljhrfcq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
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
#daxlbqbvjx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#daxlbqbvjx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#daxlbqbvjx p { margin: 0; padding: 0; }
 #daxlbqbvjx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #daxlbqbvjx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #daxlbqbvjx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #daxlbqbvjx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: -0.4px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #daxlbqbvjx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #daxlbqbvjx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #daxlbqbvjx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #daxlbqbvjx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 0.75px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #daxlbqbvjx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #daxlbqbvjx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #daxlbqbvjx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #daxlbqbvjx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 0.75px; padding-bottom: 0.75px; overflow-x: hidden; display: inline-block; width: 100%; }
 #daxlbqbvjx .gt_spanner_row { border-bottom-style: hidden; }
 #daxlbqbvjx .gt_group_heading { padding-top: 1.2px; padding-bottom: 1.2px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #daxlbqbvjx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #daxlbqbvjx .gt_from_md> :first-child { margin-top: 0; }
 #daxlbqbvjx .gt_from_md> :last-child { margin-bottom: 0; }
 #daxlbqbvjx .gt_row { padding-top: 1.2px; padding-bottom: 1.2px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #daxlbqbvjx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #daxlbqbvjx .gt_indent_1 { text-indent: 5px; }
 #daxlbqbvjx .gt_indent_2 { text-indent: calc(5px * 2); }
 #daxlbqbvjx .gt_indent_3 { text-indent: calc(5px * 3); }
 #daxlbqbvjx .gt_indent_4 { text-indent: calc(5px * 4); }
 #daxlbqbvjx .gt_indent_5 { text-indent: calc(5px * 5); }
 #daxlbqbvjx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #daxlbqbvjx .gt_row_group_first td { border-top-width: 2px; }
 #daxlbqbvjx .gt_row_group_first th { border-top-width: 2px; }
 #daxlbqbvjx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #daxlbqbvjx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #daxlbqbvjx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #daxlbqbvjx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #daxlbqbvjx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #daxlbqbvjx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #daxlbqbvjx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #daxlbqbvjx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #daxlbqbvjx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #daxlbqbvjx .gt_sourcenote { font-size: 90%; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #daxlbqbvjx .gt_left { text-align: left; }
 #daxlbqbvjx .gt_center { text-align: center; }
 #daxlbqbvjx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #daxlbqbvjx .gt_font_normal { font-weight: normal; }
 #daxlbqbvjx .gt_font_bold { font-weight: bold; }
 #daxlbqbvjx .gt_font_italic { font-style: italic; }
 #daxlbqbvjx .gt_super { font-size: 65%; }
 #daxlbqbvjx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #daxlbqbvjx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #daxlbqbvjx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #daxlbqbvjx .gt_sourcenote { font-size: 90%; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #daxlbqbvjx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #daxlbqbvjx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
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
#zhmhobnznu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zhmhobnznu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zhmhobnznu p { margin: 0; padding: 0; }
 #zhmhobnznu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zhmhobnznu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zhmhobnznu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zhmhobnznu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 15px; padding-right: 15px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zhmhobnznu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zhmhobnznu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zhmhobnznu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zhmhobnznu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 15px; padding-right: 15px; overflow-x: hidden; }
 #zhmhobnznu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zhmhobnznu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zhmhobnznu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zhmhobnznu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zhmhobnznu .gt_spanner_row { border-bottom-style: hidden; }
 #zhmhobnznu .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zhmhobnznu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zhmhobnznu .gt_from_md> :first-child { margin-top: 0; }
 #zhmhobnznu .gt_from_md> :last-child { margin-bottom: 0; }
 #zhmhobnznu .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zhmhobnznu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; }
 #zhmhobnznu .gt_indent_1 { text-indent: 5px; }
 #zhmhobnznu .gt_indent_2 { text-indent: calc(5px * 2); }
 #zhmhobnznu .gt_indent_3 { text-indent: calc(5px * 3); }
 #zhmhobnznu .gt_indent_4 { text-indent: calc(5px * 4); }
 #zhmhobnznu .gt_indent_5 { text-indent: calc(5px * 5); }
 #zhmhobnznu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; vertical-align: top; }
 #zhmhobnznu .gt_row_group_first td { border-top-width: 2px; }
 #zhmhobnznu .gt_row_group_first th { border-top-width: 2px; }
 #zhmhobnznu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zhmhobnznu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zhmhobnznu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zhmhobnznu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zhmhobnznu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zhmhobnznu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zhmhobnznu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zhmhobnznu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zhmhobnznu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zhmhobnznu .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #zhmhobnznu .gt_left { text-align: left; }
 #zhmhobnznu .gt_center { text-align: center; }
 #zhmhobnznu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zhmhobnznu .gt_font_normal { font-weight: normal; }
 #zhmhobnznu .gt_font_bold { font-weight: bold; }
 #zhmhobnznu .gt_font_italic { font-style: italic; }
 #zhmhobnznu .gt_super { font-size: 65%; }
 #zhmhobnznu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zhmhobnznu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zhmhobnznu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zhmhobnznu .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #zhmhobnznu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zhmhobnznu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
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
#jehvcgxhes table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jehvcgxhes thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jehvcgxhes p { margin: 0; padding: 0; }
 #jehvcgxhes .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D3D3D3; border-right-style: solid; border-right-width: 3px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D3D3D3; border-left-style: solid; border-left-width: 3px; border-left-color: #D3D3D3; }
 #jehvcgxhes .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jehvcgxhes .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jehvcgxhes .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jehvcgxhes .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jehvcgxhes .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jehvcgxhes .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jehvcgxhes .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jehvcgxhes .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jehvcgxhes .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jehvcgxhes .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jehvcgxhes .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jehvcgxhes .gt_spanner_row { border-bottom-style: hidden; }
 #jehvcgxhes .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jehvcgxhes .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jehvcgxhes .gt_from_md> :first-child { margin-top: 0; }
 #jehvcgxhes .gt_from_md> :last-child { margin-bottom: 0; }
 #jehvcgxhes .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jehvcgxhes .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jehvcgxhes .gt_indent_1 { text-indent: 5px; }
 #jehvcgxhes .gt_indent_2 { text-indent: calc(5px * 2); }
 #jehvcgxhes .gt_indent_3 { text-indent: calc(5px * 3); }
 #jehvcgxhes .gt_indent_4 { text-indent: calc(5px * 4); }
 #jehvcgxhes .gt_indent_5 { text-indent: calc(5px * 5); }
 #jehvcgxhes .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jehvcgxhes .gt_row_group_first td { border-top-width: 2px; }
 #jehvcgxhes .gt_row_group_first th { border-top-width: 2px; }
 #jehvcgxhes .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jehvcgxhes .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jehvcgxhes .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jehvcgxhes .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jehvcgxhes .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jehvcgxhes .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jehvcgxhes .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jehvcgxhes .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jehvcgxhes .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jehvcgxhes .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jehvcgxhes .gt_left { text-align: left; }
 #jehvcgxhes .gt_center { text-align: center; }
 #jehvcgxhes .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jehvcgxhes .gt_font_normal { font-weight: normal; }
 #jehvcgxhes .gt_font_bold { font-weight: bold; }
 #jehvcgxhes .gt_font_italic { font-style: italic; }
 #jehvcgxhes .gt_super { font-size: 65%; }
 #jehvcgxhes .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jehvcgxhes .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jehvcgxhes .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jehvcgxhes .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jehvcgxhes .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jehvcgxhes .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left"></td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


The `opt_*()` methods give you quick access to common styling patterns without needing to remember the specific [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) argument names. For full control, you can always drop down to [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) directly, but these convenience methods cover the most frequent customization needs in just a single method call.
