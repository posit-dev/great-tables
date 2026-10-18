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
#lwyhsbqthc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lwyhsbqthc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lwyhsbqthc p { margin: 0; padding: 0; }
 #lwyhsbqthc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lwyhsbqthc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lwyhsbqthc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lwyhsbqthc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lwyhsbqthc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lwyhsbqthc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lwyhsbqthc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lwyhsbqthc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lwyhsbqthc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lwyhsbqthc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lwyhsbqthc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lwyhsbqthc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lwyhsbqthc .gt_spanner_row { border-bottom-style: hidden; }
 #lwyhsbqthc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lwyhsbqthc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lwyhsbqthc .gt_from_md> :first-child { margin-top: 0; }
 #lwyhsbqthc .gt_from_md> :last-child { margin-bottom: 0; }
 #lwyhsbqthc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lwyhsbqthc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lwyhsbqthc .gt_indent_1 { text-indent: 5px; }
 #lwyhsbqthc .gt_indent_2 { text-indent: calc(5px * 2); }
 #lwyhsbqthc .gt_indent_3 { text-indent: calc(5px * 3); }
 #lwyhsbqthc .gt_indent_4 { text-indent: calc(5px * 4); }
 #lwyhsbqthc .gt_indent_5 { text-indent: calc(5px * 5); }
 #lwyhsbqthc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lwyhsbqthc .gt_row_group_first td { border-top-width: 2px; }
 #lwyhsbqthc .gt_row_group_first th { border-top-width: 2px; }
 #lwyhsbqthc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lwyhsbqthc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lwyhsbqthc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lwyhsbqthc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lwyhsbqthc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lwyhsbqthc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lwyhsbqthc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lwyhsbqthc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lwyhsbqthc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lwyhsbqthc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lwyhsbqthc .gt_left { text-align: left; }
 #lwyhsbqthc .gt_center { text-align: center; }
 #lwyhsbqthc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lwyhsbqthc .gt_font_normal { font-weight: normal; }
 #lwyhsbqthc .gt_font_bold { font-weight: bold; }
 #lwyhsbqthc .gt_font_italic { font-style: italic; }
 #lwyhsbqthc .gt_super { font-size: 65%; }
 #lwyhsbqthc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lwyhsbqthc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lwyhsbqthc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lwyhsbqthc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lwyhsbqthc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lwyhsbqthc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" id="title" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
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
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_left" headers="stub-1 mfr">Ford</td>
<td class="gt_row gt_right" headers="stub-1 performance hp"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right" headers="stub-1 performance trq">550.0</td>
<td class="gt_row gt_right" headers="stub-1 msrp">447000.0</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_left" headers="stub-2 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-2 performance hp">597.0</td>
<td class="gt_row gt_right" headers="stub-2 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-2 msrp">291744.0</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_left" headers="stub-3 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-3 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-3 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-3 msrp">263553.0</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_left" headers="stub-4 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-4 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-4 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-4 msrp">233509.0</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_left" headers="stub-5 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-5 performance hp">661.0</td>
<td class="gt_row gt_right" headers="stub-5 performance trq">561.0</td>
<td class="gt_row gt_right" headers="stub-5 msrp">245400.0</td>
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
#oxnjuyarow table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oxnjuyarow thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oxnjuyarow p { margin: 0; padding: 0; }
 #oxnjuyarow .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oxnjuyarow .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oxnjuyarow .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oxnjuyarow .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oxnjuyarow .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oxnjuyarow .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxnjuyarow .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oxnjuyarow .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oxnjuyarow .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oxnjuyarow .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oxnjuyarow .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oxnjuyarow .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oxnjuyarow .gt_spanner_row { border-bottom-style: hidden; }
 #oxnjuyarow .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oxnjuyarow .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oxnjuyarow .gt_from_md> :first-child { margin-top: 0; }
 #oxnjuyarow .gt_from_md> :last-child { margin-bottom: 0; }
 #oxnjuyarow .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oxnjuyarow .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oxnjuyarow .gt_indent_1 { text-indent: 5px; }
 #oxnjuyarow .gt_indent_2 { text-indent: calc(5px * 2); }
 #oxnjuyarow .gt_indent_3 { text-indent: calc(5px * 3); }
 #oxnjuyarow .gt_indent_4 { text-indent: calc(5px * 4); }
 #oxnjuyarow .gt_indent_5 { text-indent: calc(5px * 5); }
 #oxnjuyarow .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oxnjuyarow .gt_row_group_first td { border-top-width: 2px; }
 #oxnjuyarow .gt_row_group_first th { border-top-width: 2px; }
 #oxnjuyarow .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oxnjuyarow .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxnjuyarow .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oxnjuyarow .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oxnjuyarow .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxnjuyarow .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oxnjuyarow .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oxnjuyarow .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oxnjuyarow .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxnjuyarow .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oxnjuyarow .gt_left { text-align: left; }
 #oxnjuyarow .gt_center { text-align: center; }
 #oxnjuyarow .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oxnjuyarow .gt_font_normal { font-weight: normal; }
 #oxnjuyarow .gt_font_bold { font-weight: bold; }
 #oxnjuyarow .gt_font_italic { font-style: italic; }
 #oxnjuyarow .gt_super { font-size: 65%; }
 #oxnjuyarow .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxnjuyarow .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oxnjuyarow .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxnjuyarow .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oxnjuyarow .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oxnjuyarow .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_left" headers="stub-1 mfr">Ford</td>
<td class="gt_row gt_right" headers="stub-1 performance hp"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right" headers="stub-1 performance trq">550.0</td>
<td class="gt_row gt_right" headers="stub-1 msrp">447000.0</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_left" headers="stub-2 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-2 performance hp">597.0</td>
<td class="gt_row gt_right" headers="stub-2 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-2 msrp">291744.0</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_left" headers="stub-3 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-3 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-3 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-3 msrp">263553.0</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_left" headers="stub-4 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-4 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-4 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-4 msrp">233509.0</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_left" headers="stub-5 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-5 performance hp">661.0</td>
<td class="gt_row gt_right" headers="stub-5 performance trq">561.0</td>
<td class="gt_row gt_right" headers="stub-5 msrp">245400.0</td>
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
#yequpmwjpv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yequpmwjpv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yequpmwjpv p { margin: 0; padding: 0; }
 #yequpmwjpv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yequpmwjpv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yequpmwjpv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yequpmwjpv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yequpmwjpv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yequpmwjpv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yequpmwjpv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yequpmwjpv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yequpmwjpv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yequpmwjpv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yequpmwjpv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yequpmwjpv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yequpmwjpv .gt_spanner_row { border-bottom-style: hidden; }
 #yequpmwjpv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yequpmwjpv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yequpmwjpv .gt_from_md> :first-child { margin-top: 0; }
 #yequpmwjpv .gt_from_md> :last-child { margin-bottom: 0; }
 #yequpmwjpv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yequpmwjpv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yequpmwjpv .gt_indent_1 { text-indent: 5px; }
 #yequpmwjpv .gt_indent_2 { text-indent: calc(5px * 2); }
 #yequpmwjpv .gt_indent_3 { text-indent: calc(5px * 3); }
 #yequpmwjpv .gt_indent_4 { text-indent: calc(5px * 4); }
 #yequpmwjpv .gt_indent_5 { text-indent: calc(5px * 5); }
 #yequpmwjpv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yequpmwjpv .gt_row_group_first td { border-top-width: 2px; }
 #yequpmwjpv .gt_row_group_first th { border-top-width: 2px; }
 #yequpmwjpv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yequpmwjpv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yequpmwjpv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yequpmwjpv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yequpmwjpv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yequpmwjpv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yequpmwjpv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yequpmwjpv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yequpmwjpv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yequpmwjpv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yequpmwjpv .gt_left { text-align: left; }
 #yequpmwjpv .gt_center { text-align: center; }
 #yequpmwjpv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yequpmwjpv .gt_font_normal { font-weight: normal; }
 #yequpmwjpv .gt_font_bold { font-weight: bold; }
 #yequpmwjpv .gt_font_italic { font-style: italic; }
 #yequpmwjpv .gt_super { font-size: 65%; }
 #yequpmwjpv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yequpmwjpv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yequpmwjpv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yequpmwjpv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yequpmwjpv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yequpmwjpv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" id="title" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
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
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_left" headers="stub-1 mfr">Ford</td>
<td class="gt_row gt_right" headers="stub-1 performance hp"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right" headers="stub-1 performance trq">550.0</td>
<td class="gt_row gt_right" headers="stub-1 msrp">447000.0</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_left" headers="stub-2 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-2 performance hp">597.0</td>
<td class="gt_row gt_right" headers="stub-2 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-2 msrp">291744.0</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_left" headers="stub-3 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-3 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-3 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-3 msrp">263553.0</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_left" headers="stub-4 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-4 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-4 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-4 msrp">233509.0</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_left" headers="stub-5 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-5 performance hp">661.0</td>
<td class="gt_row gt_right" headers="stub-5 performance trq">561.0</td>
<td class="gt_row gt_right" headers="stub-5 msrp">245400.0</td>
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
#jaxnszlbli table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jaxnszlbli thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jaxnszlbli p { margin: 0; padding: 0; }
 #jaxnszlbli .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jaxnszlbli .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jaxnszlbli .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jaxnszlbli .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jaxnszlbli .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jaxnszlbli .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jaxnszlbli .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jaxnszlbli .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jaxnszlbli .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jaxnszlbli .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jaxnszlbli .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jaxnszlbli .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jaxnszlbli .gt_spanner_row { border-bottom-style: hidden; }
 #jaxnszlbli .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jaxnszlbli .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jaxnszlbli .gt_from_md> :first-child { margin-top: 0; }
 #jaxnszlbli .gt_from_md> :last-child { margin-bottom: 0; }
 #jaxnszlbli .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jaxnszlbli .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jaxnszlbli .gt_indent_1 { text-indent: 5px; }
 #jaxnszlbli .gt_indent_2 { text-indent: calc(5px * 2); }
 #jaxnszlbli .gt_indent_3 { text-indent: calc(5px * 3); }
 #jaxnszlbli .gt_indent_4 { text-indent: calc(5px * 4); }
 #jaxnszlbli .gt_indent_5 { text-indent: calc(5px * 5); }
 #jaxnszlbli .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jaxnszlbli .gt_row_group_first td { border-top-width: 2px; }
 #jaxnszlbli .gt_row_group_first th { border-top-width: 2px; }
 #jaxnszlbli .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jaxnszlbli .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jaxnszlbli .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jaxnszlbli .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jaxnszlbli .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jaxnszlbli .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jaxnszlbli .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jaxnszlbli .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jaxnszlbli .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jaxnszlbli .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jaxnszlbli .gt_left { text-align: left; }
 #jaxnszlbli .gt_center { text-align: center; }
 #jaxnszlbli .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jaxnszlbli .gt_font_normal { font-weight: normal; }
 #jaxnszlbli .gt_font_bold { font-weight: bold; }
 #jaxnszlbli .gt_font_italic { font-style: italic; }
 #jaxnszlbli .gt_super { font-size: 65%; }
 #jaxnszlbli .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jaxnszlbli .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jaxnszlbli .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jaxnszlbli .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jaxnszlbli .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jaxnszlbli .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" id="title" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
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
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_left" headers="stub-1 mfr">Ford</td>
<td class="gt_row gt_right" headers="stub-1 performance hp"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right" headers="stub-1 performance trq">550.0</td>
<td class="gt_row gt_right" headers="stub-1 msrp">447000.0</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_left" headers="stub-2 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-2 performance hp">597.0</td>
<td class="gt_row gt_right" headers="stub-2 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-2 msrp">291744.0</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_left" headers="stub-3 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-3 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-3 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-3 msrp">263553.0</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_left" headers="stub-4 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-4 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-4 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-4 msrp">233509.0</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_left" headers="stub-5 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-5 performance hp">661.0</td>
<td class="gt_row gt_right" headers="stub-5 performance trq">561.0</td>
<td class="gt_row gt_right" headers="stub-5 msrp">245400.0</td>
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
#wkqwocfsnp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wkqwocfsnp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wkqwocfsnp p { margin: 0; padding: 0; }
 #wkqwocfsnp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wkqwocfsnp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wkqwocfsnp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wkqwocfsnp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wkqwocfsnp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wkqwocfsnp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wkqwocfsnp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wkqwocfsnp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wkqwocfsnp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wkqwocfsnp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wkqwocfsnp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wkqwocfsnp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wkqwocfsnp .gt_spanner_row { border-bottom-style: hidden; }
 #wkqwocfsnp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wkqwocfsnp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wkqwocfsnp .gt_from_md> :first-child { margin-top: 0; }
 #wkqwocfsnp .gt_from_md> :last-child { margin-bottom: 0; }
 #wkqwocfsnp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wkqwocfsnp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wkqwocfsnp .gt_indent_1 { text-indent: 5px; }
 #wkqwocfsnp .gt_indent_2 { text-indent: calc(5px * 2); }
 #wkqwocfsnp .gt_indent_3 { text-indent: calc(5px * 3); }
 #wkqwocfsnp .gt_indent_4 { text-indent: calc(5px * 4); }
 #wkqwocfsnp .gt_indent_5 { text-indent: calc(5px * 5); }
 #wkqwocfsnp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wkqwocfsnp .gt_row_group_first td { border-top-width: 2px; }
 #wkqwocfsnp .gt_row_group_first th { border-top-width: 2px; }
 #wkqwocfsnp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wkqwocfsnp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wkqwocfsnp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wkqwocfsnp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wkqwocfsnp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wkqwocfsnp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wkqwocfsnp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wkqwocfsnp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wkqwocfsnp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wkqwocfsnp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wkqwocfsnp .gt_left { text-align: left; }
 #wkqwocfsnp .gt_center { text-align: center; }
 #wkqwocfsnp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wkqwocfsnp .gt_font_normal { font-weight: normal; }
 #wkqwocfsnp .gt_font_bold { font-weight: bold; }
 #wkqwocfsnp .gt_font_italic { font-style: italic; }
 #wkqwocfsnp .gt_super { font-size: 65%; }
 #wkqwocfsnp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wkqwocfsnp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wkqwocfsnp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wkqwocfsnp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wkqwocfsnp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wkqwocfsnp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" id="title" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
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
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_left" headers="stub-1 mfr">Ford</td>
<td class="gt_row gt_right" headers="stub-1 performance hp"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right" headers="stub-1 performance trq">550.0</td>
<td class="gt_row gt_right" headers="stub-1 msrp">447000.0</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_left" headers="stub-2 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-2 performance hp">597.0</td>
<td class="gt_row gt_right" headers="stub-2 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-2 msrp">291744.0</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_left" headers="stub-3 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-3 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-3 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-3 msrp">263553.0</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_left" headers="stub-4 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-4 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-4 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-4 msrp">233509.0</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_left" headers="stub-5 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-5 performance hp">661.0</td>
<td class="gt_row gt_right" headers="stub-5 performance trq">561.0</td>
<td class="gt_row gt_right" headers="stub-5 msrp">245400.0</td>
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
#aisqbheyvg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#aisqbheyvg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#aisqbheyvg p { margin: 0; padding: 0; }
 #aisqbheyvg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #aisqbheyvg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #aisqbheyvg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #aisqbheyvg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #aisqbheyvg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aisqbheyvg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aisqbheyvg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aisqbheyvg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #aisqbheyvg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #aisqbheyvg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #aisqbheyvg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #aisqbheyvg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #aisqbheyvg .gt_spanner_row { border-bottom-style: hidden; }
 #aisqbheyvg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #aisqbheyvg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #aisqbheyvg .gt_from_md> :first-child { margin-top: 0; }
 #aisqbheyvg .gt_from_md> :last-child { margin-bottom: 0; }
 #aisqbheyvg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #aisqbheyvg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #aisqbheyvg .gt_indent_1 { text-indent: 5px; }
 #aisqbheyvg .gt_indent_2 { text-indent: calc(5px * 2); }
 #aisqbheyvg .gt_indent_3 { text-indent: calc(5px * 3); }
 #aisqbheyvg .gt_indent_4 { text-indent: calc(5px * 4); }
 #aisqbheyvg .gt_indent_5 { text-indent: calc(5px * 5); }
 #aisqbheyvg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #aisqbheyvg .gt_row_group_first td { border-top-width: 2px; }
 #aisqbheyvg .gt_row_group_first th { border-top-width: 2px; }
 #aisqbheyvg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #aisqbheyvg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aisqbheyvg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aisqbheyvg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #aisqbheyvg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aisqbheyvg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aisqbheyvg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #aisqbheyvg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #aisqbheyvg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aisqbheyvg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aisqbheyvg .gt_left { text-align: left; }
 #aisqbheyvg .gt_center { text-align: center; }
 #aisqbheyvg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #aisqbheyvg .gt_font_normal { font-weight: normal; }
 #aisqbheyvg .gt_font_bold { font-weight: bold; }
 #aisqbheyvg .gt_font_italic { font-style: italic; }
 #aisqbheyvg .gt_super { font-size: 65%; }
 #aisqbheyvg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aisqbheyvg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #aisqbheyvg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aisqbheyvg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aisqbheyvg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #aisqbheyvg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" id="title" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
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
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_left" headers="stub-1 mfr">Ford</td>
<td class="gt_row gt_right" headers="stub-1 performance hp">647.0</td>
<td class="gt_row gt_right" headers="stub-1 performance trq">550.0</td>
<td class="gt_row gt_right" headers="stub-1 msrp">447000.0</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_left" headers="stub-2 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-2 performance hp">597.0</td>
<td class="gt_row gt_right" headers="stub-2 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-2 msrp">291744.0</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_left" headers="stub-3 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-3 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-3 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-3 msrp">263553.0</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_left" headers="stub-4 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-4 performance hp">562.0</td>
<td class="gt_row gt_right" headers="stub-4 performance trq">398.0</td>
<td class="gt_row gt_right" headers="stub-4 msrp">233509.0</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_left" headers="stub-5 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-5 performance hp">661.0</td>
<td class="gt_row gt_right" headers="stub-5 performance trq">561.0</td>
<td class="gt_row gt_right" headers="stub-5 msrp">245400.0</td>
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
#iynoyngvgm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iynoyngvgm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iynoyngvgm p { margin: 0; padding: 0; }
 #iynoyngvgm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iynoyngvgm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iynoyngvgm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iynoyngvgm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iynoyngvgm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iynoyngvgm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iynoyngvgm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iynoyngvgm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iynoyngvgm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iynoyngvgm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iynoyngvgm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iynoyngvgm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iynoyngvgm .gt_spanner_row { border-bottom-style: hidden; }
 #iynoyngvgm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iynoyngvgm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iynoyngvgm .gt_from_md> :first-child { margin-top: 0; }
 #iynoyngvgm .gt_from_md> :last-child { margin-bottom: 0; }
 #iynoyngvgm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iynoyngvgm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iynoyngvgm .gt_indent_1 { text-indent: 5px; }
 #iynoyngvgm .gt_indent_2 { text-indent: calc(5px * 2); }
 #iynoyngvgm .gt_indent_3 { text-indent: calc(5px * 3); }
 #iynoyngvgm .gt_indent_4 { text-indent: calc(5px * 4); }
 #iynoyngvgm .gt_indent_5 { text-indent: calc(5px * 5); }
 #iynoyngvgm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iynoyngvgm .gt_row_group_first td { border-top-width: 2px; }
 #iynoyngvgm .gt_row_group_first th { border-top-width: 2px; }
 #iynoyngvgm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iynoyngvgm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iynoyngvgm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iynoyngvgm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iynoyngvgm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iynoyngvgm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iynoyngvgm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iynoyngvgm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iynoyngvgm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iynoyngvgm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iynoyngvgm .gt_left { text-align: left; }
 #iynoyngvgm .gt_center { text-align: center; }
 #iynoyngvgm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iynoyngvgm .gt_font_normal { font-weight: normal; }
 #iynoyngvgm .gt_font_bold { font-weight: bold; }
 #iynoyngvgm .gt_font_italic { font-style: italic; }
 #iynoyngvgm .gt_super { font-size: 65%; }
 #iynoyngvgm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iynoyngvgm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iynoyngvgm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iynoyngvgm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iynoyngvgm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iynoyngvgm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" id="title" class="gt_heading gt_title gt_font_normal">Five Cars</th>
</tr>
<tr class="gt_heading">
<th colspan="5" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From the gtcars dataset</th>
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
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_left" headers="stub-1 mfr">Ford</td>
<td class="gt_row gt_right" headers="stub-1 hp"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 647.0</td>
<td class="gt_row gt_right" headers="stub-1 trq">550.0</td>
<td class="gt_row gt_right" headers="stub-1 msrp">447000.0</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_left" headers="stub-2 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-2 hp">597.0</td>
<td class="gt_row gt_right" headers="stub-2 trq">398.0</td>
<td class="gt_row gt_right" headers="stub-2 msrp">291744.0</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_left" headers="stub-3 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-3 hp">562.0</td>
<td class="gt_row gt_right" headers="stub-3 trq">398.0</td>
<td class="gt_row gt_right" headers="stub-3 msrp">263553.0</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_left" headers="stub-4 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-4 hp">562.0</td>
<td class="gt_row gt_right" headers="stub-4 trq">398.0</td>
<td class="gt_row gt_right" headers="stub-4 msrp">233509.0</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_left" headers="stub-5 mfr">Ferrari</td>
<td class="gt_row gt_right" headers="stub-5 hp">661.0</td>
<td class="gt_row gt_right" headers="stub-5 trq">561.0</td>
<td class="gt_row gt_right" headers="stub-5 msrp">245400.0</td>
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
