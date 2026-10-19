# GT.tab_stub_indent()


Control indentation of row labels in the stub.


Usage

``` python
GT.tab_stub_indent(
    rows,
    indent="increase",
)
```


Indentation of row labels is an effective way to establish visual hierarchy in a table stub. [tab_stub_indent()](GT.tab_stub_indent.md#great_tables.GT.tab_stub_indent) allows for fine-grained control over row label indentation in the stub. You can use an explicit integer indentation level (between `0` and `5`), or use a keyword directive: `"increase"` (the default) or `"decrease"`.


## Parameters


`rows: RowSelectExpr`  
The rows to target for the indentation change. We can supply a list of row indices, a single row index integer, or a callable that takes the table data and returns a boolean Series. When targeting rows by name, provide a list of row label strings.

`indent: Union[int, Literal[``"increase", `<span class="st">`"decrease"``]]`</span>` = ``"increase"`  
An indentation directive or explicit integer level. The keyword `"increase"` (the default) increments the indentation level by `1`; `"decrease"` decrements it by `1`. The minimum indentation level is `0` (no indentation) and the maximum is `5`. An integer value directly sets the indentation level (clamped to the `0`-`5` range).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use a subset of the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a gt table with row groups and row labels. We'll use [tab_stub_indent()](GT.tab_stub_indent.md#great_tables.GT.tab_stub_indent) to add indentation to all the row labels in the stub.


``` python
from great_tables import GT
from great_tables.data import exibble

exibble_mini = exibble[["num", "char", "row", "group"]].head(8)

(
    GT(exibble_mini, rowname_col="row", groupname_col="group")
    .tab_stub_indent(rows=True, indent=2)
)
```


<style>
#jozmpwvwoy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jozmpwvwoy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jozmpwvwoy p { margin: 0; padding: 0; }
 #jozmpwvwoy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jozmpwvwoy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jozmpwvwoy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jozmpwvwoy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jozmpwvwoy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jozmpwvwoy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jozmpwvwoy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jozmpwvwoy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jozmpwvwoy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jozmpwvwoy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jozmpwvwoy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jozmpwvwoy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jozmpwvwoy .gt_spanner_row { border-bottom-style: hidden; }
 #jozmpwvwoy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jozmpwvwoy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jozmpwvwoy .gt_from_md> :first-child { margin-top: 0; }
 #jozmpwvwoy .gt_from_md> :last-child { margin-bottom: 0; }
 #jozmpwvwoy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jozmpwvwoy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jozmpwvwoy .gt_indent_1 { text-indent: 5px; }
 #jozmpwvwoy .gt_indent_2 { text-indent: calc(5px * 2); }
 #jozmpwvwoy .gt_indent_3 { text-indent: calc(5px * 3); }
 #jozmpwvwoy .gt_indent_4 { text-indent: calc(5px * 4); }
 #jozmpwvwoy .gt_indent_5 { text-indent: calc(5px * 5); }
 #jozmpwvwoy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jozmpwvwoy .gt_row_group_first td { border-top-width: 2px; }
 #jozmpwvwoy .gt_row_group_first th { border-top-width: 2px; }
 #jozmpwvwoy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jozmpwvwoy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jozmpwvwoy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jozmpwvwoy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jozmpwvwoy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jozmpwvwoy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jozmpwvwoy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jozmpwvwoy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jozmpwvwoy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jozmpwvwoy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jozmpwvwoy .gt_left { text-align: left; }
 #jozmpwvwoy .gt_center { text-align: center; }
 #jozmpwvwoy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jozmpwvwoy .gt_font_normal { font-weight: normal; }
 #jozmpwvwoy .gt_font_bold { font-weight: bold; }
 #jozmpwvwoy .gt_font_italic { font-style: italic; }
 #jozmpwvwoy .gt_super { font-size: 65%; }
 #jozmpwvwoy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jozmpwvwoy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jozmpwvwoy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jozmpwvwoy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jozmpwvwoy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jozmpwvwoy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub gt_indent_2" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub gt_indent_2" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub gt_indent_2" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub gt_indent_2" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub gt_indent_2" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub gt_indent_2" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub gt_indent_2" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub gt_indent_2" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
</tr>
</tbody>
</table>


Here's a more advanced example using the [constants](data.constants.md#great_tables.data.constants) dataset. We filter for three groups of physical constants and rename the sub-entries to start with `"..."` so it's clear they belong to a parent constant. Then [tab_stub_indent()](GT.tab_stub_indent.md#great_tables.GT.tab_stub_indent) targets those sub-rows (via a Polars expression) and indents them by 4 levels.


``` python
from great_tables import GT, stub
from great_tables.data import constants
import polars as pl

constants_mini = (
    pl.from_pandas(constants)
    .select(["name", "value", "uncert", "units"])
    .filter(
        pl.col("name").str.starts_with("atomic mass constant")
        | pl.col("name").str.starts_with("Rydberg constant")
        | pl.col("name").str.starts_with("Bohr magneton")
    )
    .with_columns(
        name=pl.when(
            pl.col("name").str.contains("constant ")
            | pl.col("name").str.contains("magneton ")
        )
        .then(pl.col("name").str.replace(r".*?(?:constant |magneton )", "..."))
        .otherwise(pl.col("name"))
    )
)

(
    GT(constants_mini, rowname_col="name")
    .tab_stubhead(label="Physical Constant")
    .tab_stub_indent(
        rows=pl.col("name").str.starts_with("..."),
        indent=4,
    )
    .fmt_scientific(columns=["value", "uncert"])
    .fmt_units(columns="units")
    .cols_label(value="Value", uncert="Uncertainty", units="Units")
    .cols_width(cases={stub: "250px", "value": "150px", "uncert": "150px", "units": "80px"})
)
```


    /home/runner/work/great-tables/great-tables/great_tables/_render_checks.py:37: RenderWarning: Rendering table with .cols_width() in Quarto may result in unexpected behavior. This is because Quarto performs custom table processing. Either use all percentage widths, or set .tab_options(quarto_disable_processing=True) to disable Quarto table processing.
      warnings.warn(


<style>
#anobphginq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#anobphginq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#anobphginq p { margin: 0; padding: 0; }
 #anobphginq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #anobphginq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #anobphginq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #anobphginq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #anobphginq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #anobphginq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #anobphginq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #anobphginq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #anobphginq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #anobphginq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #anobphginq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #anobphginq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #anobphginq .gt_spanner_row { border-bottom-style: hidden; }
 #anobphginq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #anobphginq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #anobphginq .gt_from_md> :first-child { margin-top: 0; }
 #anobphginq .gt_from_md> :last-child { margin-bottom: 0; }
 #anobphginq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #anobphginq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #anobphginq .gt_indent_1 { text-indent: 5px; }
 #anobphginq .gt_indent_2 { text-indent: calc(5px * 2); }
 #anobphginq .gt_indent_3 { text-indent: calc(5px * 3); }
 #anobphginq .gt_indent_4 { text-indent: calc(5px * 4); }
 #anobphginq .gt_indent_5 { text-indent: calc(5px * 5); }
 #anobphginq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #anobphginq .gt_row_group_first td { border-top-width: 2px; }
 #anobphginq .gt_row_group_first th { border-top-width: 2px; }
 #anobphginq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #anobphginq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #anobphginq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #anobphginq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #anobphginq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #anobphginq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #anobphginq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #anobphginq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #anobphginq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #anobphginq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #anobphginq .gt_left { text-align: left; }
 #anobphginq .gt_center { text-align: center; }
 #anobphginq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #anobphginq .gt_font_normal { font-weight: normal; }
 #anobphginq .gt_font_bold { font-weight: bold; }
 #anobphginq .gt_font_italic { font-style: italic; }
 #anobphginq .gt_super { font-size: 65%; }
 #anobphginq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #anobphginq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #anobphginq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #anobphginq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #anobphginq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #anobphginq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Physical Constant | Value | Uncertainty | Units |
|----|----|----|----|
| atomic mass constant | 1.66 × 10<sup>−27</sup> | 5.00 × 10<sup>−37</sup> | kg |
| ...energy equivalent | 1.49 × 10<sup>−10</sup> | 4.50 × 10<sup>−20</sup> | J |
| ...energy equivalent in MeV | 9.31 × 10<sup>2</sup> | 2.80 × 10<sup>−7</sup> | MeV |
| Bohr magneton | 9.27 × 10<sup>−24</sup> | 2.80 × 10<sup>−33</sup> | J T<span style="white-space:nowrap;"><sup>−1</sup></span> |
| ...in eV/T | 5.79 × 10<sup>−5</sup> | 1.70 × 10<sup>−14</sup> | eV T<span style="white-space:nowrap;"><sup>−1</sup></span> |
| ...in Hz/T | 1.40 × 10<sup>10</sup> | 4.20 | Hz T<span style="white-space:nowrap;"><sup>−1</sup></span> |
| ...in inverse meter per tesla | 4.67 × 10<sup>1</sup> | 1.40 × 10<sup>−8</sup> | m<span style="white-space:nowrap;"><sup>−1</sup></span> T<span style="white-space:nowrap;"><sup>−1</sup></span> |
| ...in K/T | 6.72 × 10<sup>−1</sup> | 2.00 × 10<sup>−10</sup> | K T<span style="white-space:nowrap;"><sup>−1</sup></span> |
| Rydberg constant | 1.10 × 10<sup>7</sup> | 2.10 × 10<sup>−5</sup> | m<span style="white-space:nowrap;"><sup>−1</sup></span> |
| ...times c in Hz | 3.29 × 10<sup>15</sup> | 6.40 × 10<sup>3</sup> | Hz |
| ...times hc in eV | 1.36 × 10<sup>1</sup> | 2.60 × 10<sup>−11</sup> | eV |
| ...times hc in J | 2.18 × 10<sup>−18</sup> | 4.20 × 10<sup>−30</sup> | J |
