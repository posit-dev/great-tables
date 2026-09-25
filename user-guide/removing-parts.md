# Removing Table Parts

Just as the `tab_*()` family of methods lets you *add* components to a table, the `rm_*()` family lets you *remove* them. This is useful when you're handed a [GT](../reference/GT.md#great_tables.GT) object that already carries a header, footnotes, or spanners (perhaps from a shared helper function or a template) and you'd like to strip a component out rather than rebuild the table from scratch. Every `rm_*()` method returns the [GT](../reference/GT.md#great_tables.GT) object, so these calls chain like any other.

A common workflow where removal shines is when you start with a template or shared helper function that builds a fully-decorated table and then strip away the parts that aren't relevant for a particular audience or context. For example, a detailed report might include footnotes and source notes that provide full attribution and methodology details, while a dashboard version of the same table might strip those away for a cleaner, more compact look. Rather than maintaining two separate table-building functions, you maintain one and selectively remove what you don't need.

To have something to remove, let's build up a table that uses several components at once. We'll take a small slice of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset and give it a header, a stubhead label, a spanner, a footnote, and two source notes.


``` python
from great_tables import GT, md, loc
from great_tables.data import gtcars

gtcars_mini = gtcars[["model", "mfr", "hp", "trq", "msrp"]].head(5)

gt_tbl = (
    GT(gtcars_mini, rowname_col="model")
    .tab_header(title="Five Cars", subtitle="From the gtcars dataset")
    .tab_stubhead(label="car")
    .tab_spanner(label="performance", columns=["hp", "trq"], id="performance")
    .tab_footnote(footnote="Horsepower.", locations=loc.body(columns="hp", rows=[0]))
    .tab_source_note(source_note="Source: the gtcars dataset.")
    .tab_source_note(source_note=md("Prices in *USD*."))
)

gt_tbl
```


<style>
#ehzuixzwsh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ehzuixzwsh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ehzuixzwsh p { margin: 0; padding: 0; }
 #ehzuixzwsh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ehzuixzwsh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ehzuixzwsh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ehzuixzwsh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ehzuixzwsh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ehzuixzwsh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ehzuixzwsh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ehzuixzwsh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ehzuixzwsh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ehzuixzwsh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ehzuixzwsh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ehzuixzwsh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ehzuixzwsh .gt_spanner_row { border-bottom-style: hidden; }
 #ehzuixzwsh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ehzuixzwsh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ehzuixzwsh .gt_from_md> :first-child { margin-top: 0; }
 #ehzuixzwsh .gt_from_md> :last-child { margin-bottom: 0; }
 #ehzuixzwsh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ehzuixzwsh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ehzuixzwsh .gt_indent_1 { text-indent: 5px; }
 #ehzuixzwsh .gt_indent_2 { text-indent: calc(5px * 2); }
 #ehzuixzwsh .gt_indent_3 { text-indent: calc(5px * 3); }
 #ehzuixzwsh .gt_indent_4 { text-indent: calc(5px * 4); }
 #ehzuixzwsh .gt_indent_5 { text-indent: calc(5px * 5); }
 #ehzuixzwsh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ehzuixzwsh .gt_row_group_first td { border-top-width: 2px; }
 #ehzuixzwsh .gt_row_group_first th { border-top-width: 2px; }
 #ehzuixzwsh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ehzuixzwsh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ehzuixzwsh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ehzuixzwsh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ehzuixzwsh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ehzuixzwsh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ehzuixzwsh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ehzuixzwsh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ehzuixzwsh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ehzuixzwsh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ehzuixzwsh .gt_left { text-align: left; }
 #ehzuixzwsh .gt_center { text-align: center; }
 #ehzuixzwsh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ehzuixzwsh .gt_font_normal { font-weight: normal; }
 #ehzuixzwsh .gt_font_bold { font-weight: bold; }
 #ehzuixzwsh .gt_font_italic { font-style: italic; }
 #ehzuixzwsh .gt_super { font-size: 65%; }
 #ehzuixzwsh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ehzuixzwsh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ehzuixzwsh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ehzuixzwsh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ehzuixzwsh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ehzuixzwsh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="car" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">car</th>
<th rowspan="2" id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th colspan="2" id="performance" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
<th rowspan="2" id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
<tr class="gt_col_headings">
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Source: the gtcars dataset.</td>
</tr>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Prices in <em>USD</em>.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="5" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Horsepower.</td>
</tr>
</tfoot>

</table>


# Removing the Header

The **Table Header** (the title and optional subtitle) is removed with the [rm_header()](../reference/GT.rm_header.md#great_tables.GT.rm_header) method. It takes no arguments and clears the entire header at once.


``` python
gt_tbl.rm_header()
```


<style>
#euvjzgwcdk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#euvjzgwcdk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#euvjzgwcdk p { margin: 0; padding: 0; }
 #euvjzgwcdk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #euvjzgwcdk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #euvjzgwcdk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #euvjzgwcdk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #euvjzgwcdk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #euvjzgwcdk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #euvjzgwcdk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #euvjzgwcdk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #euvjzgwcdk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #euvjzgwcdk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #euvjzgwcdk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #euvjzgwcdk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #euvjzgwcdk .gt_spanner_row { border-bottom-style: hidden; }
 #euvjzgwcdk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #euvjzgwcdk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #euvjzgwcdk .gt_from_md> :first-child { margin-top: 0; }
 #euvjzgwcdk .gt_from_md> :last-child { margin-bottom: 0; }
 #euvjzgwcdk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #euvjzgwcdk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #euvjzgwcdk .gt_indent_1 { text-indent: 5px; }
 #euvjzgwcdk .gt_indent_2 { text-indent: calc(5px * 2); }
 #euvjzgwcdk .gt_indent_3 { text-indent: calc(5px * 3); }
 #euvjzgwcdk .gt_indent_4 { text-indent: calc(5px * 4); }
 #euvjzgwcdk .gt_indent_5 { text-indent: calc(5px * 5); }
 #euvjzgwcdk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #euvjzgwcdk .gt_row_group_first td { border-top-width: 2px; }
 #euvjzgwcdk .gt_row_group_first th { border-top-width: 2px; }
 #euvjzgwcdk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #euvjzgwcdk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #euvjzgwcdk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #euvjzgwcdk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #euvjzgwcdk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #euvjzgwcdk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #euvjzgwcdk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #euvjzgwcdk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #euvjzgwcdk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #euvjzgwcdk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #euvjzgwcdk .gt_left { text-align: left; }
 #euvjzgwcdk .gt_center { text-align: center; }
 #euvjzgwcdk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #euvjzgwcdk .gt_font_normal { font-weight: normal; }
 #euvjzgwcdk .gt_font_bold { font-weight: bold; }
 #euvjzgwcdk .gt_font_italic { font-style: italic; }
 #euvjzgwcdk .gt_super { font-size: 65%; }
 #euvjzgwcdk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #euvjzgwcdk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #euvjzgwcdk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #euvjzgwcdk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #euvjzgwcdk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #euvjzgwcdk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="car" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">car</th>
<th rowspan="2" id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th colspan="2" id="performance" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
<th rowspan="2" id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
<tr class="gt_col_headings">
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Source: the gtcars dataset.</td>
</tr>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Prices in <em>USD</em>.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="5" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Horsepower.</td>
</tr>
</tfoot>

</table>


# Removing the Stubhead Label

The *stubhead label* is the label that sits above the table stub. It's removed with [rm_stubhead()](../reference/GT.rm_stubhead.md#great_tables.GT.rm_stubhead), which leaves the stub itself in place and takes away only the label.


``` python
gt_tbl.rm_stubhead()
```


<style>
#qgenbjufhu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qgenbjufhu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qgenbjufhu p { margin: 0; padding: 0; }
 #qgenbjufhu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qgenbjufhu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qgenbjufhu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qgenbjufhu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qgenbjufhu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qgenbjufhu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgenbjufhu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qgenbjufhu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qgenbjufhu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qgenbjufhu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qgenbjufhu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qgenbjufhu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qgenbjufhu .gt_spanner_row { border-bottom-style: hidden; }
 #qgenbjufhu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qgenbjufhu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qgenbjufhu .gt_from_md> :first-child { margin-top: 0; }
 #qgenbjufhu .gt_from_md> :last-child { margin-bottom: 0; }
 #qgenbjufhu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qgenbjufhu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qgenbjufhu .gt_indent_1 { text-indent: 5px; }
 #qgenbjufhu .gt_indent_2 { text-indent: calc(5px * 2); }
 #qgenbjufhu .gt_indent_3 { text-indent: calc(5px * 3); }
 #qgenbjufhu .gt_indent_4 { text-indent: calc(5px * 4); }
 #qgenbjufhu .gt_indent_5 { text-indent: calc(5px * 5); }
 #qgenbjufhu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qgenbjufhu .gt_row_group_first td { border-top-width: 2px; }
 #qgenbjufhu .gt_row_group_first th { border-top-width: 2px; }
 #qgenbjufhu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qgenbjufhu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgenbjufhu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qgenbjufhu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qgenbjufhu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgenbjufhu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qgenbjufhu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qgenbjufhu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qgenbjufhu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgenbjufhu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qgenbjufhu .gt_left { text-align: left; }
 #qgenbjufhu .gt_center { text-align: center; }
 #qgenbjufhu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qgenbjufhu .gt_font_normal { font-weight: normal; }
 #qgenbjufhu .gt_font_bold { font-weight: bold; }
 #qgenbjufhu .gt_font_italic { font-style: italic; }
 #qgenbjufhu .gt_super { font-size: 65%; }
 #qgenbjufhu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgenbjufhu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qgenbjufhu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgenbjufhu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qgenbjufhu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qgenbjufhu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th rowspan="2" id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th colspan="2" id="performance" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
<th rowspan="2" id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
<tr class="gt_col_headings">
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Source: the gtcars dataset.</td>
</tr>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Prices in <em>USD</em>.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="5" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Horsepower.</td>
</tr>
</tfoot>

</table>


# Removing Source Notes

Source notes live in the **Table Footer**. Calling [rm_source_notes()](../reference/GT.rm_source_notes.md#great_tables.GT.rm_source_notes) with no arguments removes all of them.


``` python
gt_tbl.rm_source_notes()
```


<style>
#ggtsvpwkuj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ggtsvpwkuj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ggtsvpwkuj p { margin: 0; padding: 0; }
 #ggtsvpwkuj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ggtsvpwkuj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ggtsvpwkuj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ggtsvpwkuj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ggtsvpwkuj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ggtsvpwkuj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ggtsvpwkuj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ggtsvpwkuj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ggtsvpwkuj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ggtsvpwkuj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ggtsvpwkuj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ggtsvpwkuj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ggtsvpwkuj .gt_spanner_row { border-bottom-style: hidden; }
 #ggtsvpwkuj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ggtsvpwkuj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ggtsvpwkuj .gt_from_md> :first-child { margin-top: 0; }
 #ggtsvpwkuj .gt_from_md> :last-child { margin-bottom: 0; }
 #ggtsvpwkuj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ggtsvpwkuj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ggtsvpwkuj .gt_indent_1 { text-indent: 5px; }
 #ggtsvpwkuj .gt_indent_2 { text-indent: calc(5px * 2); }
 #ggtsvpwkuj .gt_indent_3 { text-indent: calc(5px * 3); }
 #ggtsvpwkuj .gt_indent_4 { text-indent: calc(5px * 4); }
 #ggtsvpwkuj .gt_indent_5 { text-indent: calc(5px * 5); }
 #ggtsvpwkuj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ggtsvpwkuj .gt_row_group_first td { border-top-width: 2px; }
 #ggtsvpwkuj .gt_row_group_first th { border-top-width: 2px; }
 #ggtsvpwkuj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ggtsvpwkuj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ggtsvpwkuj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ggtsvpwkuj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ggtsvpwkuj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ggtsvpwkuj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ggtsvpwkuj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ggtsvpwkuj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ggtsvpwkuj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ggtsvpwkuj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ggtsvpwkuj .gt_left { text-align: left; }
 #ggtsvpwkuj .gt_center { text-align: center; }
 #ggtsvpwkuj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ggtsvpwkuj .gt_font_normal { font-weight: normal; }
 #ggtsvpwkuj .gt_font_bold { font-weight: bold; }
 #ggtsvpwkuj .gt_font_italic { font-style: italic; }
 #ggtsvpwkuj .gt_super { font-size: 65%; }
 #ggtsvpwkuj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ggtsvpwkuj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ggtsvpwkuj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ggtsvpwkuj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ggtsvpwkuj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ggtsvpwkuj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="car" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">car</th>
<th rowspan="2" id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th colspan="2" id="performance" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
<th rowspan="2" id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
<tr class="gt_col_headings">
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="5" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Horsepower.</td>
</tr>
</tfoot>

</table>


To remove only *some* of the source notes, supply the `source_notes=` argument with a `0`-based index (or a list of indices) reflecting the order in which the notes were added. Here we drop just the first source note and keep the second.


``` python
gt_tbl.rm_source_notes(source_notes=0)
```


<style>
#fknuafwcvx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fknuafwcvx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fknuafwcvx p { margin: 0; padding: 0; }
 #fknuafwcvx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fknuafwcvx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fknuafwcvx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fknuafwcvx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fknuafwcvx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fknuafwcvx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fknuafwcvx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fknuafwcvx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fknuafwcvx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fknuafwcvx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fknuafwcvx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fknuafwcvx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fknuafwcvx .gt_spanner_row { border-bottom-style: hidden; }
 #fknuafwcvx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fknuafwcvx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fknuafwcvx .gt_from_md> :first-child { margin-top: 0; }
 #fknuafwcvx .gt_from_md> :last-child { margin-bottom: 0; }
 #fknuafwcvx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fknuafwcvx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fknuafwcvx .gt_indent_1 { text-indent: 5px; }
 #fknuafwcvx .gt_indent_2 { text-indent: calc(5px * 2); }
 #fknuafwcvx .gt_indent_3 { text-indent: calc(5px * 3); }
 #fknuafwcvx .gt_indent_4 { text-indent: calc(5px * 4); }
 #fknuafwcvx .gt_indent_5 { text-indent: calc(5px * 5); }
 #fknuafwcvx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fknuafwcvx .gt_row_group_first td { border-top-width: 2px; }
 #fknuafwcvx .gt_row_group_first th { border-top-width: 2px; }
 #fknuafwcvx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fknuafwcvx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fknuafwcvx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fknuafwcvx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fknuafwcvx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fknuafwcvx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fknuafwcvx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fknuafwcvx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fknuafwcvx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fknuafwcvx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fknuafwcvx .gt_left { text-align: left; }
 #fknuafwcvx .gt_center { text-align: center; }
 #fknuafwcvx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fknuafwcvx .gt_font_normal { font-weight: normal; }
 #fknuafwcvx .gt_font_bold { font-weight: bold; }
 #fknuafwcvx .gt_font_italic { font-style: italic; }
 #fknuafwcvx .gt_super { font-size: 65%; }
 #fknuafwcvx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fknuafwcvx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fknuafwcvx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fknuafwcvx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fknuafwcvx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fknuafwcvx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="car" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">car</th>
<th rowspan="2" id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th colspan="2" id="performance" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
<th rowspan="2" id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
<tr class="gt_col_headings">
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Prices in <em>USD</em>.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="5" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Horsepower.</td>
</tr>
</tfoot>

</table>


# Removing Footnotes

Footnotes are removed the same way through the [rm_footnotes()](../reference/GT.rm_footnotes.md#great_tables.GT.rm_footnotes) method. Called without arguments, all footnotes are removed. The `footnotes=` argument accepts a `0`-based index or a list of indices when you want to remove specific ones while keeping the rest.


``` python
gt_tbl.rm_footnotes()
```


<style>
#biyzlspwfb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#biyzlspwfb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#biyzlspwfb p { margin: 0; padding: 0; }
 #biyzlspwfb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #biyzlspwfb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #biyzlspwfb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #biyzlspwfb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #biyzlspwfb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #biyzlspwfb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #biyzlspwfb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #biyzlspwfb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #biyzlspwfb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #biyzlspwfb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #biyzlspwfb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #biyzlspwfb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #biyzlspwfb .gt_spanner_row { border-bottom-style: hidden; }
 #biyzlspwfb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #biyzlspwfb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #biyzlspwfb .gt_from_md> :first-child { margin-top: 0; }
 #biyzlspwfb .gt_from_md> :last-child { margin-bottom: 0; }
 #biyzlspwfb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #biyzlspwfb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #biyzlspwfb .gt_indent_1 { text-indent: 5px; }
 #biyzlspwfb .gt_indent_2 { text-indent: calc(5px * 2); }
 #biyzlspwfb .gt_indent_3 { text-indent: calc(5px * 3); }
 #biyzlspwfb .gt_indent_4 { text-indent: calc(5px * 4); }
 #biyzlspwfb .gt_indent_5 { text-indent: calc(5px * 5); }
 #biyzlspwfb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #biyzlspwfb .gt_row_group_first td { border-top-width: 2px; }
 #biyzlspwfb .gt_row_group_first th { border-top-width: 2px; }
 #biyzlspwfb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #biyzlspwfb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #biyzlspwfb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #biyzlspwfb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #biyzlspwfb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #biyzlspwfb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #biyzlspwfb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #biyzlspwfb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #biyzlspwfb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #biyzlspwfb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #biyzlspwfb .gt_left { text-align: left; }
 #biyzlspwfb .gt_center { text-align: center; }
 #biyzlspwfb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #biyzlspwfb .gt_font_normal { font-weight: normal; }
 #biyzlspwfb .gt_font_bold { font-weight: bold; }
 #biyzlspwfb .gt_font_italic { font-style: italic; }
 #biyzlspwfb .gt_super { font-size: 65%; }
 #biyzlspwfb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #biyzlspwfb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #biyzlspwfb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #biyzlspwfb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #biyzlspwfb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #biyzlspwfb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="car" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">car</th>
<th rowspan="2" id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th colspan="2" id="performance" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
<th rowspan="2" id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
<tr class="gt_col_headings">
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Source: the gtcars dataset.</td>
</tr>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Prices in <em>USD</em>.</td>
</tr>
</tfoot>

</table>


# Removing Spanners

Spanners are removed with [rm_spanners()](../reference/GT.rm_spanners.md#great_tables.GT.rm_spanners), which takes away the spanner labels while leaving the underlying columns untouched. With no arguments, all spanners are removed. To target specific ones, pass their ID values to the `spanners=` argument.


``` python
gt_tbl.rm_spanners(spanners="performance")
```


<style>
#eowwupdtrr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eowwupdtrr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eowwupdtrr p { margin: 0; padding: 0; }
 #eowwupdtrr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eowwupdtrr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eowwupdtrr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eowwupdtrr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eowwupdtrr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eowwupdtrr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eowwupdtrr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eowwupdtrr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eowwupdtrr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eowwupdtrr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eowwupdtrr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eowwupdtrr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eowwupdtrr .gt_spanner_row { border-bottom-style: hidden; }
 #eowwupdtrr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eowwupdtrr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eowwupdtrr .gt_from_md> :first-child { margin-top: 0; }
 #eowwupdtrr .gt_from_md> :last-child { margin-bottom: 0; }
 #eowwupdtrr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eowwupdtrr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eowwupdtrr .gt_indent_1 { text-indent: 5px; }
 #eowwupdtrr .gt_indent_2 { text-indent: calc(5px * 2); }
 #eowwupdtrr .gt_indent_3 { text-indent: calc(5px * 3); }
 #eowwupdtrr .gt_indent_4 { text-indent: calc(5px * 4); }
 #eowwupdtrr .gt_indent_5 { text-indent: calc(5px * 5); }
 #eowwupdtrr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eowwupdtrr .gt_row_group_first td { border-top-width: 2px; }
 #eowwupdtrr .gt_row_group_first th { border-top-width: 2px; }
 #eowwupdtrr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eowwupdtrr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eowwupdtrr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eowwupdtrr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eowwupdtrr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eowwupdtrr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eowwupdtrr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eowwupdtrr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eowwupdtrr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eowwupdtrr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eowwupdtrr .gt_left { text-align: left; }
 #eowwupdtrr .gt_center { text-align: center; }
 #eowwupdtrr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eowwupdtrr .gt_font_normal { font-weight: normal; }
 #eowwupdtrr .gt_font_bold { font-weight: bold; }
 #eowwupdtrr .gt_font_italic { font-style: italic; }
 #eowwupdtrr .gt_super { font-size: 65%; }
 #eowwupdtrr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eowwupdtrr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eowwupdtrr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eowwupdtrr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eowwupdtrr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eowwupdtrr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
</tr>
<tr class="gt_col_headings">
<th id="car" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">car</th>
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Source: the gtcars dataset.</td>
</tr>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote">Prices in <em>USD</em>.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="5" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Horsepower.</td>
</tr>
</tfoot>

</table>


Spanners can also be removed by *level* using the `levels=` argument. Levels are numbered starting at `0` for the row of spanners closest to the column labels, increasing as you move upward. This is handy when a table has stacked (nested) spanners and you want to clear an entire tier at once. When both `spanners=` and `levels=` are supplied, only the spanners that match *both* conditions are removed.

The ability to remove by level is especially useful when working with deeply nested spanners (spanners that span other spanners). Rather than tracking individual spanner IDs (which can become unwieldy as the number of spanners grows) you can clear an entire tier at once. For instance, if you have a three-level spanner hierarchy and want to simplify the table down to a single level, two [rm_spanners()](../reference/GT.rm_spanners.md#great_tables.GT.rm_spanners) calls with the appropriate `levels=` values will do the job cleanly.

The `rm_*()` methods round out the table-building workflow: the `tab_*()` methods put components in place, and their `rm_*()` counterparts take them back out. Because each returns a [GT](../reference/GT.md#great_tables.GT) object, you can freely mix additions and removals within a single chain, which makes it easy to adapt a table that was created elsewhere to suit your needs.
