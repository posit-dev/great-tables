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
#rmaboaaist table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rmaboaaist thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rmaboaaist p { margin: 0; padding: 0; }
 #rmaboaaist .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rmaboaaist .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rmaboaaist .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rmaboaaist .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rmaboaaist .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rmaboaaist .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rmaboaaist .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rmaboaaist .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rmaboaaist .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rmaboaaist .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rmaboaaist .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rmaboaaist .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rmaboaaist .gt_spanner_row { border-bottom-style: hidden; }
 #rmaboaaist .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rmaboaaist .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rmaboaaist .gt_from_md> :first-child { margin-top: 0; }
 #rmaboaaist .gt_from_md> :last-child { margin-bottom: 0; }
 #rmaboaaist .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rmaboaaist .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rmaboaaist .gt_indent_1 { text-indent: 5px; }
 #rmaboaaist .gt_indent_2 { text-indent: calc(5px * 2); }
 #rmaboaaist .gt_indent_3 { text-indent: calc(5px * 3); }
 #rmaboaaist .gt_indent_4 { text-indent: calc(5px * 4); }
 #rmaboaaist .gt_indent_5 { text-indent: calc(5px * 5); }
 #rmaboaaist .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rmaboaaist .gt_row_group_first td { border-top-width: 2px; }
 #rmaboaaist .gt_row_group_first th { border-top-width: 2px; }
 #rmaboaaist .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rmaboaaist .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rmaboaaist .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rmaboaaist .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rmaboaaist .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rmaboaaist .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rmaboaaist .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rmaboaaist .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rmaboaaist .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rmaboaaist .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rmaboaaist .gt_left { text-align: left; }
 #rmaboaaist .gt_center { text-align: center; }
 #rmaboaaist .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rmaboaaist .gt_font_normal { font-weight: normal; }
 #rmaboaaist .gt_font_bold { font-weight: bold; }
 #rmaboaaist .gt_font_italic { font-style: italic; }
 #rmaboaaist .gt_super { font-size: 65%; }
 #rmaboaaist .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rmaboaaist .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rmaboaaist .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rmaboaaist .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rmaboaaist .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rmaboaaist .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rzrtdhmorg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rzrtdhmorg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rzrtdhmorg p { margin: 0; padding: 0; }
 #rzrtdhmorg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rzrtdhmorg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rzrtdhmorg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rzrtdhmorg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rzrtdhmorg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rzrtdhmorg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rzrtdhmorg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rzrtdhmorg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rzrtdhmorg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rzrtdhmorg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rzrtdhmorg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rzrtdhmorg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rzrtdhmorg .gt_spanner_row { border-bottom-style: hidden; }
 #rzrtdhmorg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rzrtdhmorg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rzrtdhmorg .gt_from_md> :first-child { margin-top: 0; }
 #rzrtdhmorg .gt_from_md> :last-child { margin-bottom: 0; }
 #rzrtdhmorg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rzrtdhmorg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rzrtdhmorg .gt_indent_1 { text-indent: 5px; }
 #rzrtdhmorg .gt_indent_2 { text-indent: calc(5px * 2); }
 #rzrtdhmorg .gt_indent_3 { text-indent: calc(5px * 3); }
 #rzrtdhmorg .gt_indent_4 { text-indent: calc(5px * 4); }
 #rzrtdhmorg .gt_indent_5 { text-indent: calc(5px * 5); }
 #rzrtdhmorg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rzrtdhmorg .gt_row_group_first td { border-top-width: 2px; }
 #rzrtdhmorg .gt_row_group_first th { border-top-width: 2px; }
 #rzrtdhmorg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rzrtdhmorg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rzrtdhmorg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rzrtdhmorg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rzrtdhmorg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rzrtdhmorg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rzrtdhmorg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rzrtdhmorg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rzrtdhmorg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rzrtdhmorg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rzrtdhmorg .gt_left { text-align: left; }
 #rzrtdhmorg .gt_center { text-align: center; }
 #rzrtdhmorg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rzrtdhmorg .gt_font_normal { font-weight: normal; }
 #rzrtdhmorg .gt_font_bold { font-weight: bold; }
 #rzrtdhmorg .gt_font_italic { font-style: italic; }
 #rzrtdhmorg .gt_super { font-size: 65%; }
 #rzrtdhmorg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rzrtdhmorg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rzrtdhmorg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rzrtdhmorg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rzrtdhmorg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rzrtdhmorg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tbibszlhwn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tbibszlhwn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tbibszlhwn p { margin: 0; padding: 0; }
 #tbibszlhwn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tbibszlhwn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tbibszlhwn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tbibszlhwn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tbibszlhwn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tbibszlhwn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tbibszlhwn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tbibszlhwn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tbibszlhwn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tbibszlhwn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tbibszlhwn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tbibszlhwn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tbibszlhwn .gt_spanner_row { border-bottom-style: hidden; }
 #tbibszlhwn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tbibszlhwn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tbibszlhwn .gt_from_md> :first-child { margin-top: 0; }
 #tbibszlhwn .gt_from_md> :last-child { margin-bottom: 0; }
 #tbibszlhwn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tbibszlhwn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tbibszlhwn .gt_indent_1 { text-indent: 5px; }
 #tbibszlhwn .gt_indent_2 { text-indent: calc(5px * 2); }
 #tbibszlhwn .gt_indent_3 { text-indent: calc(5px * 3); }
 #tbibszlhwn .gt_indent_4 { text-indent: calc(5px * 4); }
 #tbibszlhwn .gt_indent_5 { text-indent: calc(5px * 5); }
 #tbibszlhwn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tbibszlhwn .gt_row_group_first td { border-top-width: 2px; }
 #tbibszlhwn .gt_row_group_first th { border-top-width: 2px; }
 #tbibszlhwn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tbibszlhwn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tbibszlhwn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tbibszlhwn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tbibszlhwn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tbibszlhwn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tbibszlhwn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tbibszlhwn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tbibszlhwn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tbibszlhwn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tbibszlhwn .gt_left { text-align: left; }
 #tbibszlhwn .gt_center { text-align: center; }
 #tbibszlhwn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tbibszlhwn .gt_font_normal { font-weight: normal; }
 #tbibszlhwn .gt_font_bold { font-weight: bold; }
 #tbibszlhwn .gt_font_italic { font-style: italic; }
 #tbibszlhwn .gt_super { font-size: 65%; }
 #tbibszlhwn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tbibszlhwn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tbibszlhwn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tbibszlhwn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tbibszlhwn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tbibszlhwn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xzelfvdxsr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xzelfvdxsr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xzelfvdxsr p { margin: 0; padding: 0; }
 #xzelfvdxsr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xzelfvdxsr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xzelfvdxsr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xzelfvdxsr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xzelfvdxsr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xzelfvdxsr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xzelfvdxsr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xzelfvdxsr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xzelfvdxsr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xzelfvdxsr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xzelfvdxsr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xzelfvdxsr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xzelfvdxsr .gt_spanner_row { border-bottom-style: hidden; }
 #xzelfvdxsr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xzelfvdxsr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xzelfvdxsr .gt_from_md> :first-child { margin-top: 0; }
 #xzelfvdxsr .gt_from_md> :last-child { margin-bottom: 0; }
 #xzelfvdxsr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xzelfvdxsr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xzelfvdxsr .gt_indent_1 { text-indent: 5px; }
 #xzelfvdxsr .gt_indent_2 { text-indent: calc(5px * 2); }
 #xzelfvdxsr .gt_indent_3 { text-indent: calc(5px * 3); }
 #xzelfvdxsr .gt_indent_4 { text-indent: calc(5px * 4); }
 #xzelfvdxsr .gt_indent_5 { text-indent: calc(5px * 5); }
 #xzelfvdxsr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xzelfvdxsr .gt_row_group_first td { border-top-width: 2px; }
 #xzelfvdxsr .gt_row_group_first th { border-top-width: 2px; }
 #xzelfvdxsr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xzelfvdxsr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xzelfvdxsr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xzelfvdxsr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xzelfvdxsr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xzelfvdxsr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xzelfvdxsr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xzelfvdxsr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xzelfvdxsr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xzelfvdxsr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xzelfvdxsr .gt_left { text-align: left; }
 #xzelfvdxsr .gt_center { text-align: center; }
 #xzelfvdxsr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xzelfvdxsr .gt_font_normal { font-weight: normal; }
 #xzelfvdxsr .gt_font_bold { font-weight: bold; }
 #xzelfvdxsr .gt_font_italic { font-style: italic; }
 #xzelfvdxsr .gt_super { font-size: 65%; }
 #xzelfvdxsr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xzelfvdxsr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xzelfvdxsr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xzelfvdxsr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xzelfvdxsr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xzelfvdxsr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ekxlgbeaba table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ekxlgbeaba thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ekxlgbeaba p { margin: 0; padding: 0; }
 #ekxlgbeaba .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ekxlgbeaba .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ekxlgbeaba .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ekxlgbeaba .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ekxlgbeaba .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ekxlgbeaba .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ekxlgbeaba .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ekxlgbeaba .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ekxlgbeaba .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ekxlgbeaba .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ekxlgbeaba .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ekxlgbeaba .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ekxlgbeaba .gt_spanner_row { border-bottom-style: hidden; }
 #ekxlgbeaba .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ekxlgbeaba .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ekxlgbeaba .gt_from_md> :first-child { margin-top: 0; }
 #ekxlgbeaba .gt_from_md> :last-child { margin-bottom: 0; }
 #ekxlgbeaba .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ekxlgbeaba .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ekxlgbeaba .gt_indent_1 { text-indent: 5px; }
 #ekxlgbeaba .gt_indent_2 { text-indent: calc(5px * 2); }
 #ekxlgbeaba .gt_indent_3 { text-indent: calc(5px * 3); }
 #ekxlgbeaba .gt_indent_4 { text-indent: calc(5px * 4); }
 #ekxlgbeaba .gt_indent_5 { text-indent: calc(5px * 5); }
 #ekxlgbeaba .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ekxlgbeaba .gt_row_group_first td { border-top-width: 2px; }
 #ekxlgbeaba .gt_row_group_first th { border-top-width: 2px; }
 #ekxlgbeaba .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ekxlgbeaba .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ekxlgbeaba .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ekxlgbeaba .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ekxlgbeaba .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ekxlgbeaba .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ekxlgbeaba .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ekxlgbeaba .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ekxlgbeaba .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ekxlgbeaba .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ekxlgbeaba .gt_left { text-align: left; }
 #ekxlgbeaba .gt_center { text-align: center; }
 #ekxlgbeaba .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ekxlgbeaba .gt_font_normal { font-weight: normal; }
 #ekxlgbeaba .gt_font_bold { font-weight: bold; }
 #ekxlgbeaba .gt_font_italic { font-style: italic; }
 #ekxlgbeaba .gt_super { font-size: 65%; }
 #ekxlgbeaba .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ekxlgbeaba .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ekxlgbeaba .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ekxlgbeaba .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ekxlgbeaba .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ekxlgbeaba .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tfqwcvtmni table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tfqwcvtmni thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tfqwcvtmni p { margin: 0; padding: 0; }
 #tfqwcvtmni .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tfqwcvtmni .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tfqwcvtmni .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tfqwcvtmni .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tfqwcvtmni .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tfqwcvtmni .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tfqwcvtmni .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tfqwcvtmni .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tfqwcvtmni .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tfqwcvtmni .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tfqwcvtmni .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tfqwcvtmni .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tfqwcvtmni .gt_spanner_row { border-bottom-style: hidden; }
 #tfqwcvtmni .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tfqwcvtmni .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tfqwcvtmni .gt_from_md> :first-child { margin-top: 0; }
 #tfqwcvtmni .gt_from_md> :last-child { margin-bottom: 0; }
 #tfqwcvtmni .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tfqwcvtmni .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tfqwcvtmni .gt_indent_1 { text-indent: 5px; }
 #tfqwcvtmni .gt_indent_2 { text-indent: calc(5px * 2); }
 #tfqwcvtmni .gt_indent_3 { text-indent: calc(5px * 3); }
 #tfqwcvtmni .gt_indent_4 { text-indent: calc(5px * 4); }
 #tfqwcvtmni .gt_indent_5 { text-indent: calc(5px * 5); }
 #tfqwcvtmni .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tfqwcvtmni .gt_row_group_first td { border-top-width: 2px; }
 #tfqwcvtmni .gt_row_group_first th { border-top-width: 2px; }
 #tfqwcvtmni .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tfqwcvtmni .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tfqwcvtmni .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tfqwcvtmni .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tfqwcvtmni .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tfqwcvtmni .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tfqwcvtmni .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tfqwcvtmni .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tfqwcvtmni .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tfqwcvtmni .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tfqwcvtmni .gt_left { text-align: left; }
 #tfqwcvtmni .gt_center { text-align: center; }
 #tfqwcvtmni .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tfqwcvtmni .gt_font_normal { font-weight: normal; }
 #tfqwcvtmni .gt_font_bold { font-weight: bold; }
 #tfqwcvtmni .gt_font_italic { font-style: italic; }
 #tfqwcvtmni .gt_super { font-size: 65%; }
 #tfqwcvtmni .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tfqwcvtmni .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tfqwcvtmni .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tfqwcvtmni .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tfqwcvtmni .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tfqwcvtmni .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#idhprujhbg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#idhprujhbg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#idhprujhbg p { margin: 0; padding: 0; }
 #idhprujhbg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #idhprujhbg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #idhprujhbg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #idhprujhbg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #idhprujhbg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #idhprujhbg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #idhprujhbg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #idhprujhbg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #idhprujhbg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #idhprujhbg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #idhprujhbg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #idhprujhbg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #idhprujhbg .gt_spanner_row { border-bottom-style: hidden; }
 #idhprujhbg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #idhprujhbg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #idhprujhbg .gt_from_md> :first-child { margin-top: 0; }
 #idhprujhbg .gt_from_md> :last-child { margin-bottom: 0; }
 #idhprujhbg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #idhprujhbg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #idhprujhbg .gt_indent_1 { text-indent: 5px; }
 #idhprujhbg .gt_indent_2 { text-indent: calc(5px * 2); }
 #idhprujhbg .gt_indent_3 { text-indent: calc(5px * 3); }
 #idhprujhbg .gt_indent_4 { text-indent: calc(5px * 4); }
 #idhprujhbg .gt_indent_5 { text-indent: calc(5px * 5); }
 #idhprujhbg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #idhprujhbg .gt_row_group_first td { border-top-width: 2px; }
 #idhprujhbg .gt_row_group_first th { border-top-width: 2px; }
 #idhprujhbg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #idhprujhbg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #idhprujhbg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #idhprujhbg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #idhprujhbg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #idhprujhbg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #idhprujhbg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #idhprujhbg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #idhprujhbg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #idhprujhbg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #idhprujhbg .gt_left { text-align: left; }
 #idhprujhbg .gt_center { text-align: center; }
 #idhprujhbg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #idhprujhbg .gt_font_normal { font-weight: normal; }
 #idhprujhbg .gt_font_bold { font-weight: bold; }
 #idhprujhbg .gt_font_italic { font-style: italic; }
 #idhprujhbg .gt_super { font-size: 65%; }
 #idhprujhbg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #idhprujhbg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #idhprujhbg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #idhprujhbg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #idhprujhbg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #idhprujhbg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
