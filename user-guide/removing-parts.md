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
#lafwisegjl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lafwisegjl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lafwisegjl p { margin: 0; padding: 0; }
 #lafwisegjl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lafwisegjl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lafwisegjl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lafwisegjl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lafwisegjl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lafwisegjl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lafwisegjl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lafwisegjl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lafwisegjl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lafwisegjl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lafwisegjl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lafwisegjl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lafwisegjl .gt_spanner_row { border-bottom-style: hidden; }
 #lafwisegjl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lafwisegjl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lafwisegjl .gt_from_md> :first-child { margin-top: 0; }
 #lafwisegjl .gt_from_md> :last-child { margin-bottom: 0; }
 #lafwisegjl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lafwisegjl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lafwisegjl .gt_indent_1 { text-indent: 5px; }
 #lafwisegjl .gt_indent_2 { text-indent: calc(5px * 2); }
 #lafwisegjl .gt_indent_3 { text-indent: calc(5px * 3); }
 #lafwisegjl .gt_indent_4 { text-indent: calc(5px * 4); }
 #lafwisegjl .gt_indent_5 { text-indent: calc(5px * 5); }
 #lafwisegjl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lafwisegjl .gt_row_group_first td { border-top-width: 2px; }
 #lafwisegjl .gt_row_group_first th { border-top-width: 2px; }
 #lafwisegjl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lafwisegjl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lafwisegjl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lafwisegjl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lafwisegjl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lafwisegjl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lafwisegjl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lafwisegjl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lafwisegjl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lafwisegjl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lafwisegjl .gt_left { text-align: left; }
 #lafwisegjl .gt_center { text-align: center; }
 #lafwisegjl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lafwisegjl .gt_font_normal { font-weight: normal; }
 #lafwisegjl .gt_font_bold { font-weight: bold; }
 #lafwisegjl .gt_font_italic { font-style: italic; }
 #lafwisegjl .gt_super { font-size: 65%; }
 #lafwisegjl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lafwisegjl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lafwisegjl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lafwisegjl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lafwisegjl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lafwisegjl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fahpwvgril table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fahpwvgril thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fahpwvgril p { margin: 0; padding: 0; }
 #fahpwvgril .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fahpwvgril .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fahpwvgril .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fahpwvgril .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fahpwvgril .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fahpwvgril .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fahpwvgril .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fahpwvgril .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fahpwvgril .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fahpwvgril .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fahpwvgril .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fahpwvgril .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fahpwvgril .gt_spanner_row { border-bottom-style: hidden; }
 #fahpwvgril .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fahpwvgril .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fahpwvgril .gt_from_md> :first-child { margin-top: 0; }
 #fahpwvgril .gt_from_md> :last-child { margin-bottom: 0; }
 #fahpwvgril .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fahpwvgril .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fahpwvgril .gt_indent_1 { text-indent: 5px; }
 #fahpwvgril .gt_indent_2 { text-indent: calc(5px * 2); }
 #fahpwvgril .gt_indent_3 { text-indent: calc(5px * 3); }
 #fahpwvgril .gt_indent_4 { text-indent: calc(5px * 4); }
 #fahpwvgril .gt_indent_5 { text-indent: calc(5px * 5); }
 #fahpwvgril .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fahpwvgril .gt_row_group_first td { border-top-width: 2px; }
 #fahpwvgril .gt_row_group_first th { border-top-width: 2px; }
 #fahpwvgril .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fahpwvgril .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fahpwvgril .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fahpwvgril .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fahpwvgril .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fahpwvgril .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fahpwvgril .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fahpwvgril .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fahpwvgril .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fahpwvgril .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fahpwvgril .gt_left { text-align: left; }
 #fahpwvgril .gt_center { text-align: center; }
 #fahpwvgril .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fahpwvgril .gt_font_normal { font-weight: normal; }
 #fahpwvgril .gt_font_bold { font-weight: bold; }
 #fahpwvgril .gt_font_italic { font-style: italic; }
 #fahpwvgril .gt_super { font-size: 65%; }
 #fahpwvgril .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fahpwvgril .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fahpwvgril .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fahpwvgril .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fahpwvgril .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fahpwvgril .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tdosnkbxjm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tdosnkbxjm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tdosnkbxjm p { margin: 0; padding: 0; }
 #tdosnkbxjm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tdosnkbxjm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tdosnkbxjm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tdosnkbxjm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tdosnkbxjm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tdosnkbxjm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tdosnkbxjm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tdosnkbxjm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tdosnkbxjm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tdosnkbxjm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tdosnkbxjm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tdosnkbxjm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tdosnkbxjm .gt_spanner_row { border-bottom-style: hidden; }
 #tdosnkbxjm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tdosnkbxjm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tdosnkbxjm .gt_from_md> :first-child { margin-top: 0; }
 #tdosnkbxjm .gt_from_md> :last-child { margin-bottom: 0; }
 #tdosnkbxjm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tdosnkbxjm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tdosnkbxjm .gt_indent_1 { text-indent: 5px; }
 #tdosnkbxjm .gt_indent_2 { text-indent: calc(5px * 2); }
 #tdosnkbxjm .gt_indent_3 { text-indent: calc(5px * 3); }
 #tdosnkbxjm .gt_indent_4 { text-indent: calc(5px * 4); }
 #tdosnkbxjm .gt_indent_5 { text-indent: calc(5px * 5); }
 #tdosnkbxjm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tdosnkbxjm .gt_row_group_first td { border-top-width: 2px; }
 #tdosnkbxjm .gt_row_group_first th { border-top-width: 2px; }
 #tdosnkbxjm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tdosnkbxjm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tdosnkbxjm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tdosnkbxjm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tdosnkbxjm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tdosnkbxjm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tdosnkbxjm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tdosnkbxjm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tdosnkbxjm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tdosnkbxjm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tdosnkbxjm .gt_left { text-align: left; }
 #tdosnkbxjm .gt_center { text-align: center; }
 #tdosnkbxjm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tdosnkbxjm .gt_font_normal { font-weight: normal; }
 #tdosnkbxjm .gt_font_bold { font-weight: bold; }
 #tdosnkbxjm .gt_font_italic { font-style: italic; }
 #tdosnkbxjm .gt_super { font-size: 65%; }
 #tdosnkbxjm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tdosnkbxjm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tdosnkbxjm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tdosnkbxjm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tdosnkbxjm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tdosnkbxjm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zgkzwxarlc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zgkzwxarlc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zgkzwxarlc p { margin: 0; padding: 0; }
 #zgkzwxarlc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zgkzwxarlc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zgkzwxarlc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zgkzwxarlc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zgkzwxarlc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zgkzwxarlc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zgkzwxarlc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zgkzwxarlc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zgkzwxarlc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zgkzwxarlc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zgkzwxarlc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zgkzwxarlc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zgkzwxarlc .gt_spanner_row { border-bottom-style: hidden; }
 #zgkzwxarlc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zgkzwxarlc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zgkzwxarlc .gt_from_md> :first-child { margin-top: 0; }
 #zgkzwxarlc .gt_from_md> :last-child { margin-bottom: 0; }
 #zgkzwxarlc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zgkzwxarlc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zgkzwxarlc .gt_indent_1 { text-indent: 5px; }
 #zgkzwxarlc .gt_indent_2 { text-indent: calc(5px * 2); }
 #zgkzwxarlc .gt_indent_3 { text-indent: calc(5px * 3); }
 #zgkzwxarlc .gt_indent_4 { text-indent: calc(5px * 4); }
 #zgkzwxarlc .gt_indent_5 { text-indent: calc(5px * 5); }
 #zgkzwxarlc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zgkzwxarlc .gt_row_group_first td { border-top-width: 2px; }
 #zgkzwxarlc .gt_row_group_first th { border-top-width: 2px; }
 #zgkzwxarlc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zgkzwxarlc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zgkzwxarlc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zgkzwxarlc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zgkzwxarlc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zgkzwxarlc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zgkzwxarlc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zgkzwxarlc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zgkzwxarlc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zgkzwxarlc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zgkzwxarlc .gt_left { text-align: left; }
 #zgkzwxarlc .gt_center { text-align: center; }
 #zgkzwxarlc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zgkzwxarlc .gt_font_normal { font-weight: normal; }
 #zgkzwxarlc .gt_font_bold { font-weight: bold; }
 #zgkzwxarlc .gt_font_italic { font-style: italic; }
 #zgkzwxarlc .gt_super { font-size: 65%; }
 #zgkzwxarlc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zgkzwxarlc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zgkzwxarlc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zgkzwxarlc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zgkzwxarlc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zgkzwxarlc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xjvmiqroug table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xjvmiqroug thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xjvmiqroug p { margin: 0; padding: 0; }
 #xjvmiqroug .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xjvmiqroug .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xjvmiqroug .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xjvmiqroug .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xjvmiqroug .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xjvmiqroug .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xjvmiqroug .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xjvmiqroug .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xjvmiqroug .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xjvmiqroug .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xjvmiqroug .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xjvmiqroug .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xjvmiqroug .gt_spanner_row { border-bottom-style: hidden; }
 #xjvmiqroug .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xjvmiqroug .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xjvmiqroug .gt_from_md> :first-child { margin-top: 0; }
 #xjvmiqroug .gt_from_md> :last-child { margin-bottom: 0; }
 #xjvmiqroug .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xjvmiqroug .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xjvmiqroug .gt_indent_1 { text-indent: 5px; }
 #xjvmiqroug .gt_indent_2 { text-indent: calc(5px * 2); }
 #xjvmiqroug .gt_indent_3 { text-indent: calc(5px * 3); }
 #xjvmiqroug .gt_indent_4 { text-indent: calc(5px * 4); }
 #xjvmiqroug .gt_indent_5 { text-indent: calc(5px * 5); }
 #xjvmiqroug .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xjvmiqroug .gt_row_group_first td { border-top-width: 2px; }
 #xjvmiqroug .gt_row_group_first th { border-top-width: 2px; }
 #xjvmiqroug .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xjvmiqroug .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xjvmiqroug .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xjvmiqroug .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xjvmiqroug .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xjvmiqroug .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xjvmiqroug .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xjvmiqroug .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xjvmiqroug .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xjvmiqroug .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xjvmiqroug .gt_left { text-align: left; }
 #xjvmiqroug .gt_center { text-align: center; }
 #xjvmiqroug .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xjvmiqroug .gt_font_normal { font-weight: normal; }
 #xjvmiqroug .gt_font_bold { font-weight: bold; }
 #xjvmiqroug .gt_font_italic { font-style: italic; }
 #xjvmiqroug .gt_super { font-size: 65%; }
 #xjvmiqroug .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xjvmiqroug .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xjvmiqroug .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xjvmiqroug .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xjvmiqroug .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xjvmiqroug .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qgsloldkus table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qgsloldkus thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qgsloldkus p { margin: 0; padding: 0; }
 #qgsloldkus .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qgsloldkus .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qgsloldkus .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qgsloldkus .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qgsloldkus .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qgsloldkus .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgsloldkus .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qgsloldkus .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qgsloldkus .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qgsloldkus .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qgsloldkus .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qgsloldkus .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qgsloldkus .gt_spanner_row { border-bottom-style: hidden; }
 #qgsloldkus .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qgsloldkus .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qgsloldkus .gt_from_md> :first-child { margin-top: 0; }
 #qgsloldkus .gt_from_md> :last-child { margin-bottom: 0; }
 #qgsloldkus .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qgsloldkus .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qgsloldkus .gt_indent_1 { text-indent: 5px; }
 #qgsloldkus .gt_indent_2 { text-indent: calc(5px * 2); }
 #qgsloldkus .gt_indent_3 { text-indent: calc(5px * 3); }
 #qgsloldkus .gt_indent_4 { text-indent: calc(5px * 4); }
 #qgsloldkus .gt_indent_5 { text-indent: calc(5px * 5); }
 #qgsloldkus .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qgsloldkus .gt_row_group_first td { border-top-width: 2px; }
 #qgsloldkus .gt_row_group_first th { border-top-width: 2px; }
 #qgsloldkus .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qgsloldkus .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgsloldkus .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qgsloldkus .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qgsloldkus .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgsloldkus .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qgsloldkus .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qgsloldkus .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qgsloldkus .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgsloldkus .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qgsloldkus .gt_left { text-align: left; }
 #qgsloldkus .gt_center { text-align: center; }
 #qgsloldkus .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qgsloldkus .gt_font_normal { font-weight: normal; }
 #qgsloldkus .gt_font_bold { font-weight: bold; }
 #qgsloldkus .gt_font_italic { font-style: italic; }
 #qgsloldkus .gt_super { font-size: 65%; }
 #qgsloldkus .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgsloldkus .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qgsloldkus .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgsloldkus .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qgsloldkus .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qgsloldkus .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#blpwirztiv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#blpwirztiv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#blpwirztiv p { margin: 0; padding: 0; }
 #blpwirztiv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #blpwirztiv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #blpwirztiv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #blpwirztiv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #blpwirztiv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #blpwirztiv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #blpwirztiv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #blpwirztiv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #blpwirztiv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #blpwirztiv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #blpwirztiv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #blpwirztiv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #blpwirztiv .gt_spanner_row { border-bottom-style: hidden; }
 #blpwirztiv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #blpwirztiv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #blpwirztiv .gt_from_md> :first-child { margin-top: 0; }
 #blpwirztiv .gt_from_md> :last-child { margin-bottom: 0; }
 #blpwirztiv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #blpwirztiv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #blpwirztiv .gt_indent_1 { text-indent: 5px; }
 #blpwirztiv .gt_indent_2 { text-indent: calc(5px * 2); }
 #blpwirztiv .gt_indent_3 { text-indent: calc(5px * 3); }
 #blpwirztiv .gt_indent_4 { text-indent: calc(5px * 4); }
 #blpwirztiv .gt_indent_5 { text-indent: calc(5px * 5); }
 #blpwirztiv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #blpwirztiv .gt_row_group_first td { border-top-width: 2px; }
 #blpwirztiv .gt_row_group_first th { border-top-width: 2px; }
 #blpwirztiv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #blpwirztiv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #blpwirztiv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #blpwirztiv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #blpwirztiv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #blpwirztiv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #blpwirztiv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #blpwirztiv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #blpwirztiv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #blpwirztiv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #blpwirztiv .gt_left { text-align: left; }
 #blpwirztiv .gt_center { text-align: center; }
 #blpwirztiv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #blpwirztiv .gt_font_normal { font-weight: normal; }
 #blpwirztiv .gt_font_bold { font-weight: bold; }
 #blpwirztiv .gt_font_italic { font-style: italic; }
 #blpwirztiv .gt_super { font-size: 65%; }
 #blpwirztiv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #blpwirztiv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #blpwirztiv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #blpwirztiv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #blpwirztiv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #blpwirztiv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
