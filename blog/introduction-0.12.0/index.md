# Great Tables `v0.12.0`: Google Fonts and zebra stripes

In Great Tables `0.12.0` we focused on adding options for customizing the appearance of a table. In this post, we'll present two new features:

- using typefaces from Google Fonts via [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) and [opt_table_font()](../../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font)
- adding table striping via [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options) and [opt_row_striping()](../../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping)

Let's have a look at how these new features can be used!


## Using fonts from Google Fonts

Google Fonts is a free service that allows use of hosted typefaces in your own websites. In Great Tables, we added the [google_font()](../../reference/google_font.md#great_tables.google_font) helper function to easily incorporate such fonts in your tables. There are two ways to go about this:

1.  use [google_font()](../../reference/google_font.md#great_tables.google_font) with [opt_table_font()](../../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font) to set a Google Font for the entire table
2.  invoke [google_font()](../../reference/google_font.md#great_tables.google_font) within `tab_style(styles=style.text(font=...))` to set the font within a location

Let's start with this small table that uses the default set of fonts for the entire table.


Show the code

``` python
from great_tables import GT, exibble, style, loc

gt_tbl = (
    GT(exibble.head(), rowname_col="row", groupname_col="group")
    .cols_hide(columns=["char", "fctr", "date", "time"])
    .tab_header(
        title="A small piece of the exibble dataset",
        subtitle="Displaying the first five rows (of eight)",
    )
    .tab_source_note(
        source_note="This dataset is included in Great Tables."
    )
)

gt_tbl
```


<style>
#ksxcejirrl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ksxcejirrl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ksxcejirrl p { margin: 0; padding: 0; }
 #ksxcejirrl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ksxcejirrl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ksxcejirrl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ksxcejirrl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ksxcejirrl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ksxcejirrl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksxcejirrl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ksxcejirrl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ksxcejirrl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ksxcejirrl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ksxcejirrl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ksxcejirrl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ksxcejirrl .gt_spanner_row { border-bottom-style: hidden; }
 #ksxcejirrl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ksxcejirrl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ksxcejirrl .gt_from_md> :first-child { margin-top: 0; }
 #ksxcejirrl .gt_from_md> :last-child { margin-bottom: 0; }
 #ksxcejirrl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ksxcejirrl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ksxcejirrl .gt_indent_1 { text-indent: 5px; }
 #ksxcejirrl .gt_indent_2 { text-indent: calc(5px * 2); }
 #ksxcejirrl .gt_indent_3 { text-indent: calc(5px * 3); }
 #ksxcejirrl .gt_indent_4 { text-indent: calc(5px * 4); }
 #ksxcejirrl .gt_indent_5 { text-indent: calc(5px * 5); }
 #ksxcejirrl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ksxcejirrl .gt_row_group_first td { border-top-width: 2px; }
 #ksxcejirrl .gt_row_group_first th { border-top-width: 2px; }
 #ksxcejirrl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ksxcejirrl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksxcejirrl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ksxcejirrl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ksxcejirrl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksxcejirrl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ksxcejirrl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ksxcejirrl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ksxcejirrl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksxcejirrl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ksxcejirrl .gt_left { text-align: left; }
 #ksxcejirrl .gt_center { text-align: center; }
 #ksxcejirrl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ksxcejirrl .gt_font_normal { font-weight: normal; }
 #ksxcejirrl .gt_font_bold { font-weight: bold; }
 #ksxcejirrl .gt_font_italic { font-style: italic; }
 #ksxcejirrl .gt_super { font-size: 65%; }
 #ksxcejirrl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksxcejirrl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ksxcejirrl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksxcejirrl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ksxcejirrl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ksxcejirrl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>

</table>


Now, with [opt_table_font()](../../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font) + [google_font()](../../reference/google_font.md#great_tables.google_font), we'll change the table's font to one from Google Fonts. I like [`Noto Serif`](https://fonts.google.com/noto/specimen/Noto+Serif) so let's use that here!


``` python
from great_tables import GT, exibble, style, loc, google_font

(
    gt_tbl
    .opt_table_font(font=google_font(name="Noto Serif"))
)
```


<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif&display=swap');
#ebxujajxdh table {
          font-family: 'Noto Serif', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ebxujajxdh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ebxujajxdh p { margin: 0; padding: 0; }
 #ebxujajxdh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ebxujajxdh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ebxujajxdh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ebxujajxdh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ebxujajxdh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ebxujajxdh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ebxujajxdh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ebxujajxdh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ebxujajxdh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ebxujajxdh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ebxujajxdh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ebxujajxdh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ebxujajxdh .gt_spanner_row { border-bottom-style: hidden; }
 #ebxujajxdh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ebxujajxdh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ebxujajxdh .gt_from_md> :first-child { margin-top: 0; }
 #ebxujajxdh .gt_from_md> :last-child { margin-bottom: 0; }
 #ebxujajxdh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ebxujajxdh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ebxujajxdh .gt_indent_1 { text-indent: 5px; }
 #ebxujajxdh .gt_indent_2 { text-indent: calc(5px * 2); }
 #ebxujajxdh .gt_indent_3 { text-indent: calc(5px * 3); }
 #ebxujajxdh .gt_indent_4 { text-indent: calc(5px * 4); }
 #ebxujajxdh .gt_indent_5 { text-indent: calc(5px * 5); }
 #ebxujajxdh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ebxujajxdh .gt_row_group_first td { border-top-width: 2px; }
 #ebxujajxdh .gt_row_group_first th { border-top-width: 2px; }
 #ebxujajxdh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ebxujajxdh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ebxujajxdh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ebxujajxdh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ebxujajxdh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ebxujajxdh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ebxujajxdh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ebxujajxdh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ebxujajxdh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ebxujajxdh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ebxujajxdh .gt_left { text-align: left; }
 #ebxujajxdh .gt_center { text-align: center; }
 #ebxujajxdh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ebxujajxdh .gt_font_normal { font-weight: normal; }
 #ebxujajxdh .gt_font_bold { font-weight: bold; }
 #ebxujajxdh .gt_font_italic { font-style: italic; }
 #ebxujajxdh .gt_super { font-size: 65%; }
 #ebxujajxdh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ebxujajxdh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ebxujajxdh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ebxujajxdh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ebxujajxdh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ebxujajxdh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>

</table>


Looking good! And we don't have to apply the font to the entire table. We might just wanted to use a Google Font in the table body. For that use case, [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) is the preferred method. Here's an example that uses the [`IBM Plex Mono`](https://fonts.google.com/specimen/IBM+Plex+Mono) typeface.


``` python
(
    gt_tbl
    .tab_style(
        style=style.text(font=google_font(name="IBM Plex Mono")),
        locations=loc.body()
    )
)
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
#gsdaqoljnf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gsdaqoljnf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gsdaqoljnf p { margin: 0; padding: 0; }
 #gsdaqoljnf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gsdaqoljnf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gsdaqoljnf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gsdaqoljnf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gsdaqoljnf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gsdaqoljnf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gsdaqoljnf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gsdaqoljnf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gsdaqoljnf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gsdaqoljnf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gsdaqoljnf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gsdaqoljnf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gsdaqoljnf .gt_spanner_row { border-bottom-style: hidden; }
 #gsdaqoljnf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gsdaqoljnf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gsdaqoljnf .gt_from_md> :first-child { margin-top: 0; }
 #gsdaqoljnf .gt_from_md> :last-child { margin-bottom: 0; }
 #gsdaqoljnf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gsdaqoljnf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gsdaqoljnf .gt_indent_1 { text-indent: 5px; }
 #gsdaqoljnf .gt_indent_2 { text-indent: calc(5px * 2); }
 #gsdaqoljnf .gt_indent_3 { text-indent: calc(5px * 3); }
 #gsdaqoljnf .gt_indent_4 { text-indent: calc(5px * 4); }
 #gsdaqoljnf .gt_indent_5 { text-indent: calc(5px * 5); }
 #gsdaqoljnf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gsdaqoljnf .gt_row_group_first td { border-top-width: 2px; }
 #gsdaqoljnf .gt_row_group_first th { border-top-width: 2px; }
 #gsdaqoljnf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gsdaqoljnf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gsdaqoljnf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gsdaqoljnf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gsdaqoljnf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gsdaqoljnf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gsdaqoljnf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gsdaqoljnf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gsdaqoljnf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gsdaqoljnf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gsdaqoljnf .gt_left { text-align: left; }
 #gsdaqoljnf .gt_center { text-align: center; }
 #gsdaqoljnf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gsdaqoljnf .gt_font_normal { font-weight: normal; }
 #gsdaqoljnf .gt_font_bold { font-weight: bold; }
 #gsdaqoljnf .gt_font_italic { font-style: italic; }
 #gsdaqoljnf .gt_super { font-size: 65%; }
 #gsdaqoljnf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gsdaqoljnf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gsdaqoljnf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gsdaqoljnf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gsdaqoljnf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gsdaqoljnf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">0.1111</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-01-01 02:22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2.222</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-02-02 14:33</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">33.33</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-03-03 03:44</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">444.4</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-04-04 15:55</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">5550.0</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-05-05 04:00</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">1325.81</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>

</table>


Nice! And it's refreshing to see tables with fonts different from default set, as good as it might be. We kept the [google_font()](../../reference/google_font.md#great_tables.google_font) helper function as simple as possible, requiring only the font name in its `name=` argument. There are hundreds of fonts hosted on [Google Fonts](https://fonts.google.com) so look through the site, experiment, and find the fonts that you think look best in your tables!


## Striping rows in your table

Some people like having row striping (a.k.a. zebra stripes) in their display tables. We also know that some [advise against the practice](https://www.darkhorseanalytics.com/blog/clear-off-the-table/). We understand it's a controversial table issue, however, we also want to give you the creative freedom to just include the stripes. To that end, we now have that option in the package. There are two ways to enable this look:

1.  invoking [opt_row_striping()](../../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping) to quickly set row stripes in the table body
2.  using some combination of three `row_striping_*` arguments in [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options)

Let's use that example table with [opt_row_striping()](../../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping).


``` python
gt_tbl.opt_row_striping()
```


<style>
#xcpfhzkekn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xcpfhzkekn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xcpfhzkekn p { margin: 0; padding: 0; }
 #xcpfhzkekn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xcpfhzkekn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xcpfhzkekn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xcpfhzkekn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xcpfhzkekn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xcpfhzkekn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xcpfhzkekn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xcpfhzkekn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xcpfhzkekn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xcpfhzkekn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xcpfhzkekn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xcpfhzkekn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xcpfhzkekn .gt_spanner_row { border-bottom-style: hidden; }
 #xcpfhzkekn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xcpfhzkekn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xcpfhzkekn .gt_from_md> :first-child { margin-top: 0; }
 #xcpfhzkekn .gt_from_md> :last-child { margin-bottom: 0; }
 #xcpfhzkekn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xcpfhzkekn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xcpfhzkekn .gt_indent_1 { text-indent: 5px; }
 #xcpfhzkekn .gt_indent_2 { text-indent: calc(5px * 2); }
 #xcpfhzkekn .gt_indent_3 { text-indent: calc(5px * 3); }
 #xcpfhzkekn .gt_indent_4 { text-indent: calc(5px * 4); }
 #xcpfhzkekn .gt_indent_5 { text-indent: calc(5px * 5); }
 #xcpfhzkekn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xcpfhzkekn .gt_row_group_first td { border-top-width: 2px; }
 #xcpfhzkekn .gt_row_group_first th { border-top-width: 2px; }
 #xcpfhzkekn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xcpfhzkekn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xcpfhzkekn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xcpfhzkekn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xcpfhzkekn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xcpfhzkekn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xcpfhzkekn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xcpfhzkekn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xcpfhzkekn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xcpfhzkekn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xcpfhzkekn .gt_left { text-align: left; }
 #xcpfhzkekn .gt_center { text-align: center; }
 #xcpfhzkekn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xcpfhzkekn .gt_font_normal { font-weight: normal; }
 #xcpfhzkekn .gt_font_bold { font-weight: bold; }
 #xcpfhzkekn .gt_font_italic { font-style: italic; }
 #xcpfhzkekn .gt_super { font-size: 65%; }
 #xcpfhzkekn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xcpfhzkekn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xcpfhzkekn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xcpfhzkekn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xcpfhzkekn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xcpfhzkekn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.222</td>
<td class="gt_row gt_right gt_striped">2018-02-02 14:33</td>
<td class="gt_row gt_right gt_striped">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.4</td>
<td class="gt_row gt_right gt_striped">2018-04-04 15:55</td>
<td class="gt_row gt_right gt_striped">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>

</table>


It's somewhat subtle but there is an alternating, slightly gray background (starting on the `"row_2"` row). The color is `#808080` but with an alpha (transparency) value of `0.05`.

If this is not exactly what you want, there is an alternative to this. The [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options) method has three new arguments:

- `row_striping_background_color`: color to use for row striping
- `row_striping_include_stub`: should striping include cells in the stub?
- `row_striping_include_table_body`: should striping include cells in the body?

With these new options, we can choose to stripe the *entire* row (stub cells + body cells) and use a darker color like `"lightblue"`.


``` python
(
    gt_tbl
    .tab_options(
        row_striping_background_color="lightblue",
        row_striping_include_stub=True,
        row_striping_include_table_body=True,
    )
)
```


<style>
#tyhrzfwsjb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tyhrzfwsjb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tyhrzfwsjb p { margin: 0; padding: 0; }
 #tyhrzfwsjb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tyhrzfwsjb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tyhrzfwsjb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tyhrzfwsjb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tyhrzfwsjb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tyhrzfwsjb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tyhrzfwsjb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tyhrzfwsjb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tyhrzfwsjb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tyhrzfwsjb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tyhrzfwsjb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tyhrzfwsjb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tyhrzfwsjb .gt_spanner_row { border-bottom-style: hidden; }
 #tyhrzfwsjb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tyhrzfwsjb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tyhrzfwsjb .gt_from_md> :first-child { margin-top: 0; }
 #tyhrzfwsjb .gt_from_md> :last-child { margin-bottom: 0; }
 #tyhrzfwsjb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tyhrzfwsjb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tyhrzfwsjb .gt_indent_1 { text-indent: 5px; }
 #tyhrzfwsjb .gt_indent_2 { text-indent: calc(5px * 2); }
 #tyhrzfwsjb .gt_indent_3 { text-indent: calc(5px * 3); }
 #tyhrzfwsjb .gt_indent_4 { text-indent: calc(5px * 4); }
 #tyhrzfwsjb .gt_indent_5 { text-indent: calc(5px * 5); }
 #tyhrzfwsjb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tyhrzfwsjb .gt_row_group_first td { border-top-width: 2px; }
 #tyhrzfwsjb .gt_row_group_first th { border-top-width: 2px; }
 #tyhrzfwsjb .gt_striped { color: #333333; background-color: lightblue; }
 #tyhrzfwsjb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tyhrzfwsjb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tyhrzfwsjb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tyhrzfwsjb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tyhrzfwsjb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tyhrzfwsjb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tyhrzfwsjb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tyhrzfwsjb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tyhrzfwsjb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tyhrzfwsjb .gt_left { text-align: left; }
 #tyhrzfwsjb .gt_center { text-align: center; }
 #tyhrzfwsjb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tyhrzfwsjb .gt_font_normal { font-weight: normal; }
 #tyhrzfwsjb .gt_font_bold { font-weight: bold; }
 #tyhrzfwsjb .gt_font_italic { font-style: italic; }
 #tyhrzfwsjb .gt_super { font-size: 65%; }
 #tyhrzfwsjb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tyhrzfwsjb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tyhrzfwsjb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tyhrzfwsjb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tyhrzfwsjb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tyhrzfwsjb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_striped">row_2</td>
<td class="gt_row gt_right gt_striped">2.222</td>
<td class="gt_row gt_right gt_striped">2018-02-02 14:33</td>
<td class="gt_row gt_right gt_striped">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_striped">row_4</td>
<td class="gt_row gt_right gt_striped">444.4</td>
<td class="gt_row gt_right gt_striped">2018-04-04 15:55</td>
<td class="gt_row gt_right gt_striped">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>

</table>


These alternating fills can be a good idea in some table display circumstances. Now, you can make that call and the functionality is there to support your decision.


## Wrapping up

We are excited that this new functionality is now available in Great Tables. As ever, please let us know through [GitHub Issues](https://github.com/posit-dev/great-tables/issues) whether you ran into problems with any feature (new or old), or, if you have suggestions for further improvement!
