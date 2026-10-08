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
#smqalojbpq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#smqalojbpq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#smqalojbpq p { margin: 0; padding: 0; }
 #smqalojbpq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #smqalojbpq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #smqalojbpq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #smqalojbpq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #smqalojbpq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #smqalojbpq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #smqalojbpq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #smqalojbpq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #smqalojbpq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #smqalojbpq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #smqalojbpq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #smqalojbpq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #smqalojbpq .gt_spanner_row { border-bottom-style: hidden; }
 #smqalojbpq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #smqalojbpq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #smqalojbpq .gt_from_md> :first-child { margin-top: 0; }
 #smqalojbpq .gt_from_md> :last-child { margin-bottom: 0; }
 #smqalojbpq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #smqalojbpq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #smqalojbpq .gt_indent_1 { text-indent: 5px; }
 #smqalojbpq .gt_indent_2 { text-indent: calc(5px * 2); }
 #smqalojbpq .gt_indent_3 { text-indent: calc(5px * 3); }
 #smqalojbpq .gt_indent_4 { text-indent: calc(5px * 4); }
 #smqalojbpq .gt_indent_5 { text-indent: calc(5px * 5); }
 #smqalojbpq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #smqalojbpq .gt_row_group_first td { border-top-width: 2px; }
 #smqalojbpq .gt_row_group_first th { border-top-width: 2px; }
 #smqalojbpq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #smqalojbpq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #smqalojbpq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #smqalojbpq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #smqalojbpq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #smqalojbpq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #smqalojbpq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #smqalojbpq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #smqalojbpq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #smqalojbpq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #smqalojbpq .gt_left { text-align: left; }
 #smqalojbpq .gt_center { text-align: center; }
 #smqalojbpq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #smqalojbpq .gt_font_normal { font-weight: normal; }
 #smqalojbpq .gt_font_bold { font-weight: bold; }
 #smqalojbpq .gt_font_italic { font-style: italic; }
 #smqalojbpq .gt_super { font-size: 65%; }
 #smqalojbpq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #smqalojbpq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #smqalojbpq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #smqalojbpq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #smqalojbpq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #smqalojbpq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#azjbdbiwgy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#azjbdbiwgy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#azjbdbiwgy p { margin: 0; padding: 0; }
 #azjbdbiwgy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #azjbdbiwgy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #azjbdbiwgy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #azjbdbiwgy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #azjbdbiwgy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #azjbdbiwgy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #azjbdbiwgy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #azjbdbiwgy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #azjbdbiwgy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #azjbdbiwgy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #azjbdbiwgy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #azjbdbiwgy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #azjbdbiwgy .gt_spanner_row { border-bottom-style: hidden; }
 #azjbdbiwgy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #azjbdbiwgy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #azjbdbiwgy .gt_from_md> :first-child { margin-top: 0; }
 #azjbdbiwgy .gt_from_md> :last-child { margin-bottom: 0; }
 #azjbdbiwgy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #azjbdbiwgy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #azjbdbiwgy .gt_indent_1 { text-indent: 5px; }
 #azjbdbiwgy .gt_indent_2 { text-indent: calc(5px * 2); }
 #azjbdbiwgy .gt_indent_3 { text-indent: calc(5px * 3); }
 #azjbdbiwgy .gt_indent_4 { text-indent: calc(5px * 4); }
 #azjbdbiwgy .gt_indent_5 { text-indent: calc(5px * 5); }
 #azjbdbiwgy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #azjbdbiwgy .gt_row_group_first td { border-top-width: 2px; }
 #azjbdbiwgy .gt_row_group_first th { border-top-width: 2px; }
 #azjbdbiwgy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #azjbdbiwgy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #azjbdbiwgy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #azjbdbiwgy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #azjbdbiwgy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #azjbdbiwgy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #azjbdbiwgy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #azjbdbiwgy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #azjbdbiwgy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #azjbdbiwgy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #azjbdbiwgy .gt_left { text-align: left; }
 #azjbdbiwgy .gt_center { text-align: center; }
 #azjbdbiwgy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #azjbdbiwgy .gt_font_normal { font-weight: normal; }
 #azjbdbiwgy .gt_font_bold { font-weight: bold; }
 #azjbdbiwgy .gt_font_italic { font-style: italic; }
 #azjbdbiwgy .gt_super { font-size: 65%; }
 #azjbdbiwgy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #azjbdbiwgy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #azjbdbiwgy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #azjbdbiwgy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #azjbdbiwgy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #azjbdbiwgy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jntbhzwsaa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jntbhzwsaa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jntbhzwsaa p { margin: 0; padding: 0; }
 #jntbhzwsaa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jntbhzwsaa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jntbhzwsaa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jntbhzwsaa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jntbhzwsaa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jntbhzwsaa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jntbhzwsaa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jntbhzwsaa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jntbhzwsaa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jntbhzwsaa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jntbhzwsaa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jntbhzwsaa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jntbhzwsaa .gt_spanner_row { border-bottom-style: hidden; }
 #jntbhzwsaa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jntbhzwsaa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jntbhzwsaa .gt_from_md> :first-child { margin-top: 0; }
 #jntbhzwsaa .gt_from_md> :last-child { margin-bottom: 0; }
 #jntbhzwsaa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jntbhzwsaa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jntbhzwsaa .gt_indent_1 { text-indent: 5px; }
 #jntbhzwsaa .gt_indent_2 { text-indent: calc(5px * 2); }
 #jntbhzwsaa .gt_indent_3 { text-indent: calc(5px * 3); }
 #jntbhzwsaa .gt_indent_4 { text-indent: calc(5px * 4); }
 #jntbhzwsaa .gt_indent_5 { text-indent: calc(5px * 5); }
 #jntbhzwsaa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jntbhzwsaa .gt_row_group_first td { border-top-width: 2px; }
 #jntbhzwsaa .gt_row_group_first th { border-top-width: 2px; }
 #jntbhzwsaa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jntbhzwsaa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jntbhzwsaa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jntbhzwsaa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jntbhzwsaa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jntbhzwsaa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jntbhzwsaa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jntbhzwsaa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jntbhzwsaa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jntbhzwsaa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jntbhzwsaa .gt_left { text-align: left; }
 #jntbhzwsaa .gt_center { text-align: center; }
 #jntbhzwsaa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jntbhzwsaa .gt_font_normal { font-weight: normal; }
 #jntbhzwsaa .gt_font_bold { font-weight: bold; }
 #jntbhzwsaa .gt_font_italic { font-style: italic; }
 #jntbhzwsaa .gt_super { font-size: 65%; }
 #jntbhzwsaa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jntbhzwsaa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jntbhzwsaa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jntbhzwsaa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jntbhzwsaa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jntbhzwsaa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#eykhjovldt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eykhjovldt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eykhjovldt p { margin: 0; padding: 0; }
 #eykhjovldt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eykhjovldt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eykhjovldt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eykhjovldt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eykhjovldt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eykhjovldt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eykhjovldt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eykhjovldt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eykhjovldt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eykhjovldt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eykhjovldt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eykhjovldt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eykhjovldt .gt_spanner_row { border-bottom-style: hidden; }
 #eykhjovldt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eykhjovldt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eykhjovldt .gt_from_md> :first-child { margin-top: 0; }
 #eykhjovldt .gt_from_md> :last-child { margin-bottom: 0; }
 #eykhjovldt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eykhjovldt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eykhjovldt .gt_indent_1 { text-indent: 5px; }
 #eykhjovldt .gt_indent_2 { text-indent: calc(5px * 2); }
 #eykhjovldt .gt_indent_3 { text-indent: calc(5px * 3); }
 #eykhjovldt .gt_indent_4 { text-indent: calc(5px * 4); }
 #eykhjovldt .gt_indent_5 { text-indent: calc(5px * 5); }
 #eykhjovldt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eykhjovldt .gt_row_group_first td { border-top-width: 2px; }
 #eykhjovldt .gt_row_group_first th { border-top-width: 2px; }
 #eykhjovldt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eykhjovldt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eykhjovldt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eykhjovldt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eykhjovldt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eykhjovldt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eykhjovldt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eykhjovldt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eykhjovldt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eykhjovldt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eykhjovldt .gt_left { text-align: left; }
 #eykhjovldt .gt_center { text-align: center; }
 #eykhjovldt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eykhjovldt .gt_font_normal { font-weight: normal; }
 #eykhjovldt .gt_font_bold { font-weight: bold; }
 #eykhjovldt .gt_font_italic { font-style: italic; }
 #eykhjovldt .gt_super { font-size: 65%; }
 #eykhjovldt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eykhjovldt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eykhjovldt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eykhjovldt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eykhjovldt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eykhjovldt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#byblupxnhz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#byblupxnhz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#byblupxnhz p { margin: 0; padding: 0; }
 #byblupxnhz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #byblupxnhz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #byblupxnhz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #byblupxnhz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #byblupxnhz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #byblupxnhz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #byblupxnhz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #byblupxnhz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #byblupxnhz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #byblupxnhz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #byblupxnhz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #byblupxnhz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #byblupxnhz .gt_spanner_row { border-bottom-style: hidden; }
 #byblupxnhz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #byblupxnhz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #byblupxnhz .gt_from_md> :first-child { margin-top: 0; }
 #byblupxnhz .gt_from_md> :last-child { margin-bottom: 0; }
 #byblupxnhz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #byblupxnhz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #byblupxnhz .gt_indent_1 { text-indent: 5px; }
 #byblupxnhz .gt_indent_2 { text-indent: calc(5px * 2); }
 #byblupxnhz .gt_indent_3 { text-indent: calc(5px * 3); }
 #byblupxnhz .gt_indent_4 { text-indent: calc(5px * 4); }
 #byblupxnhz .gt_indent_5 { text-indent: calc(5px * 5); }
 #byblupxnhz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #byblupxnhz .gt_row_group_first td { border-top-width: 2px; }
 #byblupxnhz .gt_row_group_first th { border-top-width: 2px; }
 #byblupxnhz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #byblupxnhz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #byblupxnhz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #byblupxnhz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #byblupxnhz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #byblupxnhz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #byblupxnhz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #byblupxnhz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #byblupxnhz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #byblupxnhz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #byblupxnhz .gt_left { text-align: left; }
 #byblupxnhz .gt_center { text-align: center; }
 #byblupxnhz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #byblupxnhz .gt_font_normal { font-weight: normal; }
 #byblupxnhz .gt_font_bold { font-weight: bold; }
 #byblupxnhz .gt_font_italic { font-style: italic; }
 #byblupxnhz .gt_super { font-size: 65%; }
 #byblupxnhz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #byblupxnhz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #byblupxnhz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #byblupxnhz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #byblupxnhz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #byblupxnhz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qfnxsrwvne table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qfnxsrwvne thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qfnxsrwvne p { margin: 0; padding: 0; }
 #qfnxsrwvne .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qfnxsrwvne .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qfnxsrwvne .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qfnxsrwvne .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qfnxsrwvne .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qfnxsrwvne .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qfnxsrwvne .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qfnxsrwvne .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qfnxsrwvne .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qfnxsrwvne .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qfnxsrwvne .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qfnxsrwvne .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qfnxsrwvne .gt_spanner_row { border-bottom-style: hidden; }
 #qfnxsrwvne .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qfnxsrwvne .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qfnxsrwvne .gt_from_md> :first-child { margin-top: 0; }
 #qfnxsrwvne .gt_from_md> :last-child { margin-bottom: 0; }
 #qfnxsrwvne .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qfnxsrwvne .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qfnxsrwvne .gt_indent_1 { text-indent: 5px; }
 #qfnxsrwvne .gt_indent_2 { text-indent: calc(5px * 2); }
 #qfnxsrwvne .gt_indent_3 { text-indent: calc(5px * 3); }
 #qfnxsrwvne .gt_indent_4 { text-indent: calc(5px * 4); }
 #qfnxsrwvne .gt_indent_5 { text-indent: calc(5px * 5); }
 #qfnxsrwvne .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qfnxsrwvne .gt_row_group_first td { border-top-width: 2px; }
 #qfnxsrwvne .gt_row_group_first th { border-top-width: 2px; }
 #qfnxsrwvne .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qfnxsrwvne .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qfnxsrwvne .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qfnxsrwvne .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qfnxsrwvne .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qfnxsrwvne .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qfnxsrwvne .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qfnxsrwvne .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qfnxsrwvne .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qfnxsrwvne .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qfnxsrwvne .gt_left { text-align: left; }
 #qfnxsrwvne .gt_center { text-align: center; }
 #qfnxsrwvne .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qfnxsrwvne .gt_font_normal { font-weight: normal; }
 #qfnxsrwvne .gt_font_bold { font-weight: bold; }
 #qfnxsrwvne .gt_font_italic { font-style: italic; }
 #qfnxsrwvne .gt_super { font-size: 65%; }
 #qfnxsrwvne .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qfnxsrwvne .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qfnxsrwvne .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qfnxsrwvne .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qfnxsrwvne .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qfnxsrwvne .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xcdutlywbs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xcdutlywbs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xcdutlywbs p { margin: 0; padding: 0; }
 #xcdutlywbs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xcdutlywbs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xcdutlywbs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xcdutlywbs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xcdutlywbs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xcdutlywbs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xcdutlywbs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xcdutlywbs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xcdutlywbs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xcdutlywbs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xcdutlywbs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xcdutlywbs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xcdutlywbs .gt_spanner_row { border-bottom-style: hidden; }
 #xcdutlywbs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xcdutlywbs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xcdutlywbs .gt_from_md> :first-child { margin-top: 0; }
 #xcdutlywbs .gt_from_md> :last-child { margin-bottom: 0; }
 #xcdutlywbs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xcdutlywbs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xcdutlywbs .gt_indent_1 { text-indent: 5px; }
 #xcdutlywbs .gt_indent_2 { text-indent: calc(5px * 2); }
 #xcdutlywbs .gt_indent_3 { text-indent: calc(5px * 3); }
 #xcdutlywbs .gt_indent_4 { text-indent: calc(5px * 4); }
 #xcdutlywbs .gt_indent_5 { text-indent: calc(5px * 5); }
 #xcdutlywbs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xcdutlywbs .gt_row_group_first td { border-top-width: 2px; }
 #xcdutlywbs .gt_row_group_first th { border-top-width: 2px; }
 #xcdutlywbs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xcdutlywbs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xcdutlywbs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xcdutlywbs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xcdutlywbs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xcdutlywbs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xcdutlywbs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xcdutlywbs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xcdutlywbs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xcdutlywbs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xcdutlywbs .gt_left { text-align: left; }
 #xcdutlywbs .gt_center { text-align: center; }
 #xcdutlywbs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xcdutlywbs .gt_font_normal { font-weight: normal; }
 #xcdutlywbs .gt_font_bold { font-weight: bold; }
 #xcdutlywbs .gt_font_italic { font-style: italic; }
 #xcdutlywbs .gt_super { font-size: 65%; }
 #xcdutlywbs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xcdutlywbs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xcdutlywbs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xcdutlywbs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xcdutlywbs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xcdutlywbs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
