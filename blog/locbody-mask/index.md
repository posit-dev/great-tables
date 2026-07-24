# Style Table Body with `mask=` in [loc.body()](../../reference/loc.body.md#great_tables.loc.body)

In Great Tables `0.16.0`, we introduced the `mask=` parameter in [loc.body()](../../reference/loc.body.md#great_tables.loc.body), enabling users to apply conditional styling to rows on a per-column basis more efficiently when working with a Polars DataFrame. This post will demonstrate how it works and compare it with the "old-fashioned" approach:

- **Leveraging the `mask=` parameter in [loc.body()](../../reference/loc.body.md#great_tables.loc.body):** Use Polars expressions for streamlined styling.
- **Utilizing the `locations=` parameter in [GT.tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style):** Pass a list of [loc.body()](../../reference/loc.body.md#great_tables.loc.body) objects.

Let's dive in.


## Preparations

We'll use the built-in dataset [gtcars](../../reference/data.gtcars.md#great_tables.data.gtcars) to create a Polars DataFrame. Next, we'll select the columns `mfr`, `drivetrain`, `year`, and `hp` to create a small pivoted table named `df_mini`. Finally, we'll pass `df_mini` to the [GT](../../reference/GT.md#great_tables.GT) object to create a table named `gt`, using `drivetrain` as the `rowname_col=` and `mfr` as the `groupname_col=`, as shown below:


Show the Code

``` python
import polars as pl
from great_tables import GT, loc, style
from great_tables.data import gtcars
from polars import selectors as cs

year_cols = ["2014", "2015", "2016", "2017"]
df_mini = (
    pl.from_pandas(gtcars)
    .filter(pl.col("mfr").is_in(["Ferrari", "Lamborghini", "BMW"]))
    .sort("drivetrain")
    .pivot(on="year", index=["mfr", "drivetrain"], values="hp", aggregate_function="mean")
    .select(["mfr", "drivetrain", *year_cols])
)

gt = GT(df_mini).tab_stub(rowname_col="drivetrain", groupname_col="mfr").opt_stylize(color="cyan")
gt
```


<style>
#ubpxhqbsdb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ubpxhqbsdb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ubpxhqbsdb p { margin: 0; padding: 0; }
 #ubpxhqbsdb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #016763; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #016763; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ubpxhqbsdb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ubpxhqbsdb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ubpxhqbsdb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ubpxhqbsdb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ubpxhqbsdb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; }
 #ubpxhqbsdb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ubpxhqbsdb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ubpxhqbsdb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ubpxhqbsdb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ubpxhqbsdb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ubpxhqbsdb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ubpxhqbsdb .gt_spanner_row { border-bottom-style: hidden; }
 #ubpxhqbsdb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ubpxhqbsdb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; vertical-align: middle; }
 #ubpxhqbsdb .gt_from_md> :first-child { margin-top: 0; }
 #ubpxhqbsdb .gt_from_md> :last-child { margin-bottom: 0; }
 #ubpxhqbsdb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #A5FEF2; border-left-style: none; border-left-width: 1px; border-left-color: #A5FEF2; border-right-style: none; border-right-width: 1px; border-right-color: #A5FEF2; vertical-align: middle; overflow-x: hidden; }
 #ubpxhqbsdb .gt_stub { color: #FFFFFF; background-color: #01837B; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #01837B; padding-left: 5px; padding-right: 5px; }
 #ubpxhqbsdb .gt_indent_1 { text-indent: 5px; }
 #ubpxhqbsdb .gt_indent_2 { text-indent: calc(5px * 2); }
 #ubpxhqbsdb .gt_indent_3 { text-indent: calc(5px * 3); }
 #ubpxhqbsdb .gt_indent_4 { text-indent: calc(5px * 4); }
 #ubpxhqbsdb .gt_indent_5 { text-indent: calc(5px * 5); }
 #ubpxhqbsdb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ubpxhqbsdb .gt_row_group_first td { border-top-width: 2px; }
 #ubpxhqbsdb .gt_row_group_first th { border-top-width: 2px; }
 #ubpxhqbsdb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ubpxhqbsdb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; }
 #ubpxhqbsdb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ubpxhqbsdb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ubpxhqbsdb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ubpxhqbsdb .gt_grand_summary_row { color: #333333; background-color: #A5FEF2; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ubpxhqbsdb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ubpxhqbsdb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ubpxhqbsdb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ubpxhqbsdb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ubpxhqbsdb .gt_left { text-align: left; }
 #ubpxhqbsdb .gt_center { text-align: center; }
 #ubpxhqbsdb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ubpxhqbsdb .gt_font_normal { font-weight: normal; }
 #ubpxhqbsdb .gt_font_bold { font-weight: bold; }
 #ubpxhqbsdb .gt_font_italic { font-style: italic; }
 #ubpxhqbsdb .gt_super { font-size: 65%; }
 #ubpxhqbsdb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ubpxhqbsdb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ubpxhqbsdb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ubpxhqbsdb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ubpxhqbsdb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ubpxhqbsdb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="2014" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2014</th>
<th id="2015" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2015</th>
<th id="2016" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2016</th>
<th id="2017" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2017</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="5" class="gt_group_heading">Ferrari</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">680.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">562.0</td>
<td class="gt_row gt_right gt_striped">678.4</td>
<td class="gt_row gt_right gt_striped">661.0</td>
<td class="gt_row gt_right gt_striped">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">Lamborghini</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">700.0</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">550.0</td>
<td class="gt_row gt_right gt_striped">610.0</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">BMW</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">357.0</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">465.0</td>
<td class="gt_row gt_right gt_striped">None</td>
</tr>
</tbody>
</table>


The numbers in the cells represent the average horsepower for each combination of `mfr` and `drivetrain` for a specific year.


## Leveraging the `mask=` parameter in [loc.body()](../../reference/loc.body.md#great_tables.loc.body)

The `mask=` parameter in [loc.body()](../../reference/loc.body.md#great_tables.loc.body) accepts a Polars expression that evaluates to a boolean result for each cell.

Here's how we can use it to achieve the two goals:

- Highlight the cell text in red if the column datatype is numerical and the cell value exceeds 650.
- Fill the background color as lightgrey if the cell value is missing in the last two columns (`2016` and `2017`).


``` python
(
    gt.tab_style(
        style=style.text(color="red"),
        locations=loc.body(mask=cs.numeric().gt(650))
    ).tab_style(
        style=style.fill(color="lightgrey"),
        locations=loc.body(mask=pl.nth(-2, -1).is_null()),
    )
)
```


<style>
#lruidqwxbz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lruidqwxbz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lruidqwxbz p { margin: 0; padding: 0; }
 #lruidqwxbz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #016763; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #016763; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lruidqwxbz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lruidqwxbz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lruidqwxbz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lruidqwxbz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lruidqwxbz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; }
 #lruidqwxbz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lruidqwxbz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lruidqwxbz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lruidqwxbz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lruidqwxbz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lruidqwxbz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lruidqwxbz .gt_spanner_row { border-bottom-style: hidden; }
 #lruidqwxbz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lruidqwxbz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; vertical-align: middle; }
 #lruidqwxbz .gt_from_md> :first-child { margin-top: 0; }
 #lruidqwxbz .gt_from_md> :last-child { margin-bottom: 0; }
 #lruidqwxbz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #A5FEF2; border-left-style: none; border-left-width: 1px; border-left-color: #A5FEF2; border-right-style: none; border-right-width: 1px; border-right-color: #A5FEF2; vertical-align: middle; overflow-x: hidden; }
 #lruidqwxbz .gt_stub { color: #FFFFFF; background-color: #01837B; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #01837B; padding-left: 5px; padding-right: 5px; }
 #lruidqwxbz .gt_indent_1 { text-indent: 5px; }
 #lruidqwxbz .gt_indent_2 { text-indent: calc(5px * 2); }
 #lruidqwxbz .gt_indent_3 { text-indent: calc(5px * 3); }
 #lruidqwxbz .gt_indent_4 { text-indent: calc(5px * 4); }
 #lruidqwxbz .gt_indent_5 { text-indent: calc(5px * 5); }
 #lruidqwxbz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lruidqwxbz .gt_row_group_first td { border-top-width: 2px; }
 #lruidqwxbz .gt_row_group_first th { border-top-width: 2px; }
 #lruidqwxbz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lruidqwxbz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; }
 #lruidqwxbz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lruidqwxbz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lruidqwxbz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lruidqwxbz .gt_grand_summary_row { color: #333333; background-color: #A5FEF2; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lruidqwxbz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lruidqwxbz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lruidqwxbz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lruidqwxbz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lruidqwxbz .gt_left { text-align: left; }
 #lruidqwxbz .gt_center { text-align: center; }
 #lruidqwxbz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lruidqwxbz .gt_font_normal { font-weight: normal; }
 #lruidqwxbz .gt_font_bold { font-weight: bold; }
 #lruidqwxbz .gt_font_italic { font-style: italic; }
 #lruidqwxbz .gt_super { font-size: 65%; }
 #lruidqwxbz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lruidqwxbz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lruidqwxbz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lruidqwxbz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lruidqwxbz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lruidqwxbz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="2014" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2014</th>
<th id="2015" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2015</th>
<th id="2016" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2016</th>
<th id="2017" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2017</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="5" class="gt_group_heading">Ferrari</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right" style="color: red">652.0</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
<td class="gt_row gt_right" style="color: red">680.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">562.0</td>
<td class="gt_row gt_right gt_striped" style="color: red">678.4</td>
<td class="gt_row gt_right gt_striped" style="color: red">661.0</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">Lamborghini</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right" style="color: red">700.0</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">550.0</td>
<td class="gt_row gt_right gt_striped">610.0</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">BMW</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">357.0</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">465.0</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
</tr>
</tbody>
</table>


In this example:

- `cs.numeric()` targets numerical columns, and `.gt(650)` checks if the cell value is greater than 650.
- `pl.nth(-2, -1)` targets the last two columns, and `.is_null()` identifies missing values.

Did you notice that we can use Polars selectors and expressions to dynamically identify columns at runtime? This is definitely a killer feature when working with pivoted operations.

The `mask=` parameter acts as a syntactic sugar, streamlining the process and removing the need to loop through columns manually.

> **Warning: Using `mask=` Independently**
>
> `mask=` should not be used in combination with the `columns` or `rows` arguments. Attempting to do so will raise a `ValueError`.


## Utilizing the `locations=` parameter in [GT.tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style)

A more "old-fashioned" approach involves passing a list of [loc.body()](../../reference/loc.body.md#great_tables.loc.body) objects to the `locations=` parameter in [GT.tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style):


``` python
(
    gt.tab_style(
        style=style.text(color="red"),
        locations=[loc.body(columns=col, rows=pl.col(col).gt(650))
                   for col in year_cols],
    ).tab_style(
        style=style.fill(color="lightgrey"),
        locations=[loc.body(columns=col, rows=pl.col(col).is_null())
                   for col in year_cols[-2:]],
    )
)
```


This approach, though functional, demands additional effort:

- Explicitly preparing the column names in advance.
- Specifying the `columns=` and `rows=` arguments for each [loc.body()](../../reference/loc.body.md#great_tables.loc.body) in the loop.

While effective, it is less efficient and more verbose compared to the first approach.


## Wrapping up

With the introduction of the `mask=` parameter in [loc.body()](../../reference/loc.body.md#great_tables.loc.body), users can now style the table body in a more vectorized-like manner, akin to using `df.apply()` in Pandas, enhancing the overall user experience.

We extend our gratitude to [<span class="citation" data-cites="igorcalabria">@igorcalabria</span>](https://github.com/igorcalabria) for suggesting this feature in [\#389](https://github.com/posit-dev/great-tables/issues/389) and providing an insightful explanation of its utility. A special thanks to [<span class="citation" data-cites="henryharbeck">@henryharbeck</span>](https://github.com/henryharbeck) for providing the second approach.

We hope you enjoy this new functionality as much as we do! Have ideas to make Great Tables even better? Share them with us via [GitHub Issues](https://github.com/posit-dev/great-tables/issues). We're always amazed by the creativity of our users! See you, until the next great table.
