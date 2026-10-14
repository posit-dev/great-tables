# GT.cols_label()


Relabel one or more columns.


Usage

``` python
GT.cols_label(
    cases=None,
    **kwargs,
)
```


There are three important pieces to labelling:

- Each argument has the form: {name in data} = {new label}.
- Multiple columns may be given the same label.
- Labels may use curly braces to apply special formatting, called unit notation. For example, "area ({{ft^2}})" would appear as "area (ft²)".

See <a href="../reference/define_units.html#great_tables.define_units" class="gdls-link"><code>define_units()</code></a> for details on unit notation.


## Parameters


`cases: dict[str, str | BaseText] | None = None`  
A dictionary where the keys are column names and the values are the labels. Labels may use <a href="../reference/md.html#great_tables.md" class="gdls-link"><code>md()</code></a> or <a href="../reference/html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helpers for formatting.

`**kwargs: str | BaseText`  
Keyword arguments to specify column labels. Each keyword corresponds to a column name, with its value indicating the new label.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Notes

GT always selects columns using their name in the underlying data. This means that a column's label is purely for final presentation.


## Examples

The example below relabels columns from the [countrypops](data.countrypops.md#great_tables.data.countrypops) data to start with uppercase.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "Uganda"][
    ["country_name", "year", "population"]
].tail(5)

(
    GT(countrypops_mini)
    .cols_label(
        country_name="Country Name",
        year="Year",
        population="Population"
    )
)
```


<style>
#fwvygdhezm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fwvygdhezm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fwvygdhezm p { margin: 0; padding: 0; }
 #fwvygdhezm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fwvygdhezm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fwvygdhezm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fwvygdhezm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fwvygdhezm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fwvygdhezm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fwvygdhezm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fwvygdhezm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fwvygdhezm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fwvygdhezm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fwvygdhezm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fwvygdhezm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fwvygdhezm .gt_spanner_row { border-bottom-style: hidden; }
 #fwvygdhezm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fwvygdhezm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fwvygdhezm .gt_from_md> :first-child { margin-top: 0; }
 #fwvygdhezm .gt_from_md> :last-child { margin-bottom: 0; }
 #fwvygdhezm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fwvygdhezm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fwvygdhezm .gt_indent_1 { text-indent: 5px; }
 #fwvygdhezm .gt_indent_2 { text-indent: calc(5px * 2); }
 #fwvygdhezm .gt_indent_3 { text-indent: calc(5px * 3); }
 #fwvygdhezm .gt_indent_4 { text-indent: calc(5px * 4); }
 #fwvygdhezm .gt_indent_5 { text-indent: calc(5px * 5); }
 #fwvygdhezm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fwvygdhezm .gt_row_group_first td { border-top-width: 2px; }
 #fwvygdhezm .gt_row_group_first th { border-top-width: 2px; }
 #fwvygdhezm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fwvygdhezm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fwvygdhezm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fwvygdhezm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fwvygdhezm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fwvygdhezm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fwvygdhezm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fwvygdhezm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fwvygdhezm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fwvygdhezm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fwvygdhezm .gt_left { text-align: left; }
 #fwvygdhezm .gt_center { text-align: center; }
 #fwvygdhezm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fwvygdhezm .gt_font_normal { font-weight: normal; }
 #fwvygdhezm .gt_font_bold { font-weight: bold; }
 #fwvygdhezm .gt_font_italic { font-style: italic; }
 #fwvygdhezm .gt_super { font-size: 65%; }
 #fwvygdhezm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fwvygdhezm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fwvygdhezm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fwvygdhezm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fwvygdhezm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fwvygdhezm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Country Name | Year | Population |
|--------------|------|------------|
| Uganda       | 2018 | 41515395   |
| Uganda       | 2019 | 42949080   |
| Uganda       | 2020 | 44404611   |
| Uganda       | 2021 | 45853778   |
| Uganda       | 2022 | 47249585   |


Note that we supplied the name of the column as the key, and the new label as the value.

We can also use Markdown formatting for the column labels. In this example, we'll use `md("*Population*")` to make the label italicized.


``` python
from great_tables import GT, md
from great_tables.data import countrypops

(
    GT(countrypops_mini)
    .cols_label(
        country_name="Name",
        year="Year",
        population=md("*Population*")
    )
)
```


<style>
#lydrgzlwyu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lydrgzlwyu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lydrgzlwyu p { margin: 0; padding: 0; }
 #lydrgzlwyu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lydrgzlwyu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lydrgzlwyu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lydrgzlwyu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lydrgzlwyu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lydrgzlwyu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lydrgzlwyu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lydrgzlwyu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lydrgzlwyu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lydrgzlwyu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lydrgzlwyu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lydrgzlwyu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lydrgzlwyu .gt_spanner_row { border-bottom-style: hidden; }
 #lydrgzlwyu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lydrgzlwyu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lydrgzlwyu .gt_from_md> :first-child { margin-top: 0; }
 #lydrgzlwyu .gt_from_md> :last-child { margin-bottom: 0; }
 #lydrgzlwyu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lydrgzlwyu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lydrgzlwyu .gt_indent_1 { text-indent: 5px; }
 #lydrgzlwyu .gt_indent_2 { text-indent: calc(5px * 2); }
 #lydrgzlwyu .gt_indent_3 { text-indent: calc(5px * 3); }
 #lydrgzlwyu .gt_indent_4 { text-indent: calc(5px * 4); }
 #lydrgzlwyu .gt_indent_5 { text-indent: calc(5px * 5); }
 #lydrgzlwyu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lydrgzlwyu .gt_row_group_first td { border-top-width: 2px; }
 #lydrgzlwyu .gt_row_group_first th { border-top-width: 2px; }
 #lydrgzlwyu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lydrgzlwyu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lydrgzlwyu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lydrgzlwyu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lydrgzlwyu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lydrgzlwyu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lydrgzlwyu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lydrgzlwyu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lydrgzlwyu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lydrgzlwyu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lydrgzlwyu .gt_left { text-align: left; }
 #lydrgzlwyu .gt_center { text-align: center; }
 #lydrgzlwyu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lydrgzlwyu .gt_font_normal { font-weight: normal; }
 #lydrgzlwyu .gt_font_bold { font-weight: bold; }
 #lydrgzlwyu .gt_font_italic { font-style: italic; }
 #lydrgzlwyu .gt_super { font-size: 65%; }
 #lydrgzlwyu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lydrgzlwyu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lydrgzlwyu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lydrgzlwyu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lydrgzlwyu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lydrgzlwyu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Name   | Year | *Population* |
|--------|------|--------------|
| Uganda | 2018 | 41515395     |
| Uganda | 2019 | 42949080     |
| Uganda | 2020 | 44404611     |
| Uganda | 2021 | 45853778     |
| Uganda | 2022 | 47249585     |


We can also use unit notation to format the column labels. In this example, we'll use `{cm^3 molecules^-1 s^-1}` for part of the label for the `OH_k298` column.


``` python
from great_tables import GT
from great_tables.data import reactions
import polars as pl

reactions_mini = (
    pl.from_pandas(reactions)
    .filter(pl.col("cmpd_type") == "mercaptan")
    .select(["cmpd_name", "OH_k298"])
)

(
    GT(reactions_mini)
    .fmt_scientific("OH_k298")
    .sub_missing()
    .cols_label(
        cmpd_name="Compound Name",
        OH_k298="OH, {{cm^3 molecules^-1 s^-1}}",
    )
)
```


<style>
#twdzkvkndo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#twdzkvkndo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#twdzkvkndo p { margin: 0; padding: 0; }
 #twdzkvkndo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #twdzkvkndo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #twdzkvkndo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #twdzkvkndo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #twdzkvkndo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #twdzkvkndo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #twdzkvkndo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #twdzkvkndo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #twdzkvkndo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #twdzkvkndo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #twdzkvkndo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #twdzkvkndo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #twdzkvkndo .gt_spanner_row { border-bottom-style: hidden; }
 #twdzkvkndo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #twdzkvkndo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #twdzkvkndo .gt_from_md> :first-child { margin-top: 0; }
 #twdzkvkndo .gt_from_md> :last-child { margin-bottom: 0; }
 #twdzkvkndo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #twdzkvkndo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #twdzkvkndo .gt_indent_1 { text-indent: 5px; }
 #twdzkvkndo .gt_indent_2 { text-indent: calc(5px * 2); }
 #twdzkvkndo .gt_indent_3 { text-indent: calc(5px * 3); }
 #twdzkvkndo .gt_indent_4 { text-indent: calc(5px * 4); }
 #twdzkvkndo .gt_indent_5 { text-indent: calc(5px * 5); }
 #twdzkvkndo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #twdzkvkndo .gt_row_group_first td { border-top-width: 2px; }
 #twdzkvkndo .gt_row_group_first th { border-top-width: 2px; }
 #twdzkvkndo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #twdzkvkndo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #twdzkvkndo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #twdzkvkndo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #twdzkvkndo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #twdzkvkndo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #twdzkvkndo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #twdzkvkndo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #twdzkvkndo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #twdzkvkndo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #twdzkvkndo .gt_left { text-align: left; }
 #twdzkvkndo .gt_center { text-align: center; }
 #twdzkvkndo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #twdzkvkndo .gt_font_normal { font-weight: normal; }
 #twdzkvkndo .gt_font_bold { font-weight: bold; }
 #twdzkvkndo .gt_font_italic { font-style: italic; }
 #twdzkvkndo .gt_super { font-size: 65%; }
 #twdzkvkndo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #twdzkvkndo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #twdzkvkndo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #twdzkvkndo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #twdzkvkndo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #twdzkvkndo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Compound Name | OH, cm<span style="white-space:nowrap;"><sup>3</sup></span> molecules<span style="white-space:nowrap;"><sup>−1</sup></span> s<span style="white-space:nowrap;"><sup>−1</sup></span> |
|----|----|
| methanethiol | 3.50 × 10<sup>−11</sup> |
| ethanethiol | 4.50 × 10<sup>−11</sup> |
| propanethiol | 5.30 × 10<sup>−11</sup> |
| 2-propanethiol | 3.90 × 10<sup>−11</sup> |
| 1-butanethiol | 5.60 × 10<sup>−11</sup> |
| 2-methyl-1-propanethiol | 4.60 × 10<sup>−11</sup> |
| 2-butanethiol | 3.80 × 10<sup>−11</sup> |
| t-butylsulfide | 2.90 × 10<sup>−11</sup> |
| 2-methylbutanethiol | 5.20 × 10<sup>−11</sup> |
| n-pentanethiol | -- |
| 1,2-ethanedithiol | 3.80 × 10<sup>−11</sup> |
