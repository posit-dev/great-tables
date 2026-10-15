# loc.subtitle


Target the table subtitle.


Usage

``` python
loc.subtitle()
```


With [loc.subtitle()](loc.subtitle.md#great_tables.loc.subtitle), we can target the part of table containing the subtitle (within the table header). This is useful for applying custom styling with the <a href="../reference/GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a> method. That method has a `locations=` argument and this class should be used there to perform the targeting.


## Returns


`LocSubTitle`  
A LocSubTitle object, which is used for a `locations=` argument if specifying the subtitle of the table.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style only the 'subtitle' part of the table header (leaving the 'title' part unaffected). This can be done by using `locations=loc.subtitle()` within <a href="../reference/GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>.


``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars

(
    GT(gtcars[["mfr", "model", "msrp"]].head(5))
    .tab_header(
        title="Select Cars from the gtcars Dataset",
        subtitle="Only the first five cars are displayed"
    )
    .tab_style(
        style=style.fill(color="lightblue"),
        locations=loc.subtitle()
    )
    .fmt_currency(columns="msrp", decimals=0)
)
```


<style>
#eoyjajmrbs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eoyjajmrbs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eoyjajmrbs p { margin: 0; padding: 0; }
 #eoyjajmrbs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eoyjajmrbs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eoyjajmrbs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eoyjajmrbs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eoyjajmrbs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eoyjajmrbs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eoyjajmrbs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eoyjajmrbs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eoyjajmrbs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eoyjajmrbs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eoyjajmrbs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eoyjajmrbs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eoyjajmrbs .gt_spanner_row { border-bottom-style: hidden; }
 #eoyjajmrbs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eoyjajmrbs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eoyjajmrbs .gt_from_md> :first-child { margin-top: 0; }
 #eoyjajmrbs .gt_from_md> :last-child { margin-bottom: 0; }
 #eoyjajmrbs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eoyjajmrbs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eoyjajmrbs .gt_indent_1 { text-indent: 5px; }
 #eoyjajmrbs .gt_indent_2 { text-indent: calc(5px * 2); }
 #eoyjajmrbs .gt_indent_3 { text-indent: calc(5px * 3); }
 #eoyjajmrbs .gt_indent_4 { text-indent: calc(5px * 4); }
 #eoyjajmrbs .gt_indent_5 { text-indent: calc(5px * 5); }
 #eoyjajmrbs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eoyjajmrbs .gt_row_group_first td { border-top-width: 2px; }
 #eoyjajmrbs .gt_row_group_first th { border-top-width: 2px; }
 #eoyjajmrbs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eoyjajmrbs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eoyjajmrbs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eoyjajmrbs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eoyjajmrbs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eoyjajmrbs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eoyjajmrbs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eoyjajmrbs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eoyjajmrbs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eoyjajmrbs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eoyjajmrbs .gt_left { text-align: left; }
 #eoyjajmrbs .gt_center { text-align: center; }
 #eoyjajmrbs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eoyjajmrbs .gt_font_normal { font-weight: normal; }
 #eoyjajmrbs .gt_font_bold { font-weight: bold; }
 #eoyjajmrbs .gt_font_italic { font-style: italic; }
 #eoyjajmrbs .gt_super { font-size: 65%; }
 #eoyjajmrbs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eoyjajmrbs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eoyjajmrbs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eoyjajmrbs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eoyjajmrbs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eoyjajmrbs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Select Cars from the gtcars Dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="3" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="background-color: lightblue">Only the first five cars are displayed</th>
</tr>
<tr class="gt_col_headings">
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left" headers="mfr">Ford</td>
<td class="gt_row gt_left" headers="model">GT</td>
<td class="gt_row gt_right" headers="msrp">$447,000</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="mfr">Ferrari</td>
<td class="gt_row gt_left" headers="model">458 Speciale</td>
<td class="gt_row gt_right" headers="msrp">$291,744</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="mfr">Ferrari</td>
<td class="gt_row gt_left" headers="model">458 Spider</td>
<td class="gt_row gt_right" headers="msrp">$263,553</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="mfr">Ferrari</td>
<td class="gt_row gt_left" headers="model">458 Italia</td>
<td class="gt_row gt_right" headers="msrp">$233,509</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="mfr">Ferrari</td>
<td class="gt_row gt_left" headers="model">488 GTB</td>
<td class="gt_row gt_right" headers="msrp">$245,400</td>
</tr>
</tbody>
</table>
