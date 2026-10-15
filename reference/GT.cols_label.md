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
#hjqrzkjpkq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hjqrzkjpkq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hjqrzkjpkq p { margin: 0; padding: 0; }
 #hjqrzkjpkq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hjqrzkjpkq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hjqrzkjpkq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hjqrzkjpkq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hjqrzkjpkq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjqrzkjpkq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjqrzkjpkq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjqrzkjpkq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hjqrzkjpkq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hjqrzkjpkq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hjqrzkjpkq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hjqrzkjpkq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hjqrzkjpkq .gt_spanner_row { border-bottom-style: hidden; }
 #hjqrzkjpkq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hjqrzkjpkq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hjqrzkjpkq .gt_from_md> :first-child { margin-top: 0; }
 #hjqrzkjpkq .gt_from_md> :last-child { margin-bottom: 0; }
 #hjqrzkjpkq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hjqrzkjpkq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hjqrzkjpkq .gt_indent_1 { text-indent: 5px; }
 #hjqrzkjpkq .gt_indent_2 { text-indent: calc(5px * 2); }
 #hjqrzkjpkq .gt_indent_3 { text-indent: calc(5px * 3); }
 #hjqrzkjpkq .gt_indent_4 { text-indent: calc(5px * 4); }
 #hjqrzkjpkq .gt_indent_5 { text-indent: calc(5px * 5); }
 #hjqrzkjpkq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hjqrzkjpkq .gt_row_group_first td { border-top-width: 2px; }
 #hjqrzkjpkq .gt_row_group_first th { border-top-width: 2px; }
 #hjqrzkjpkq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hjqrzkjpkq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjqrzkjpkq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjqrzkjpkq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hjqrzkjpkq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjqrzkjpkq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjqrzkjpkq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hjqrzkjpkq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hjqrzkjpkq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjqrzkjpkq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjqrzkjpkq .gt_left { text-align: left; }
 #hjqrzkjpkq .gt_center { text-align: center; }
 #hjqrzkjpkq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hjqrzkjpkq .gt_font_normal { font-weight: normal; }
 #hjqrzkjpkq .gt_font_bold { font-weight: bold; }
 #hjqrzkjpkq .gt_font_italic { font-style: italic; }
 #hjqrzkjpkq .gt_super { font-size: 65%; }
 #hjqrzkjpkq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjqrzkjpkq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hjqrzkjpkq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjqrzkjpkq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjqrzkjpkq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hjqrzkjpkq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ymlleznzjn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ymlleznzjn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ymlleznzjn p { margin: 0; padding: 0; }
 #ymlleznzjn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ymlleznzjn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ymlleznzjn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ymlleznzjn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ymlleznzjn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ymlleznzjn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ymlleznzjn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ymlleznzjn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ymlleznzjn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ymlleznzjn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ymlleznzjn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ymlleznzjn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ymlleznzjn .gt_spanner_row { border-bottom-style: hidden; }
 #ymlleznzjn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ymlleznzjn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ymlleznzjn .gt_from_md> :first-child { margin-top: 0; }
 #ymlleznzjn .gt_from_md> :last-child { margin-bottom: 0; }
 #ymlleznzjn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ymlleznzjn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ymlleznzjn .gt_indent_1 { text-indent: 5px; }
 #ymlleznzjn .gt_indent_2 { text-indent: calc(5px * 2); }
 #ymlleznzjn .gt_indent_3 { text-indent: calc(5px * 3); }
 #ymlleznzjn .gt_indent_4 { text-indent: calc(5px * 4); }
 #ymlleznzjn .gt_indent_5 { text-indent: calc(5px * 5); }
 #ymlleznzjn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ymlleznzjn .gt_row_group_first td { border-top-width: 2px; }
 #ymlleznzjn .gt_row_group_first th { border-top-width: 2px; }
 #ymlleznzjn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ymlleznzjn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ymlleznzjn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ymlleznzjn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ymlleznzjn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ymlleznzjn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ymlleznzjn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ymlleznzjn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ymlleznzjn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ymlleznzjn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ymlleznzjn .gt_left { text-align: left; }
 #ymlleznzjn .gt_center { text-align: center; }
 #ymlleznzjn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ymlleznzjn .gt_font_normal { font-weight: normal; }
 #ymlleznzjn .gt_font_bold { font-weight: bold; }
 #ymlleznzjn .gt_font_italic { font-style: italic; }
 #ymlleznzjn .gt_super { font-size: 65%; }
 #ymlleznzjn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ymlleznzjn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ymlleznzjn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ymlleznzjn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ymlleznzjn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ymlleznzjn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tmdwwipufg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tmdwwipufg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tmdwwipufg p { margin: 0; padding: 0; }
 #tmdwwipufg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tmdwwipufg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tmdwwipufg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tmdwwipufg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tmdwwipufg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tmdwwipufg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tmdwwipufg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tmdwwipufg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tmdwwipufg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tmdwwipufg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tmdwwipufg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tmdwwipufg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tmdwwipufg .gt_spanner_row { border-bottom-style: hidden; }
 #tmdwwipufg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tmdwwipufg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tmdwwipufg .gt_from_md> :first-child { margin-top: 0; }
 #tmdwwipufg .gt_from_md> :last-child { margin-bottom: 0; }
 #tmdwwipufg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tmdwwipufg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tmdwwipufg .gt_indent_1 { text-indent: 5px; }
 #tmdwwipufg .gt_indent_2 { text-indent: calc(5px * 2); }
 #tmdwwipufg .gt_indent_3 { text-indent: calc(5px * 3); }
 #tmdwwipufg .gt_indent_4 { text-indent: calc(5px * 4); }
 #tmdwwipufg .gt_indent_5 { text-indent: calc(5px * 5); }
 #tmdwwipufg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tmdwwipufg .gt_row_group_first td { border-top-width: 2px; }
 #tmdwwipufg .gt_row_group_first th { border-top-width: 2px; }
 #tmdwwipufg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tmdwwipufg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tmdwwipufg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tmdwwipufg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tmdwwipufg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tmdwwipufg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tmdwwipufg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tmdwwipufg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tmdwwipufg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tmdwwipufg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tmdwwipufg .gt_left { text-align: left; }
 #tmdwwipufg .gt_center { text-align: center; }
 #tmdwwipufg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tmdwwipufg .gt_font_normal { font-weight: normal; }
 #tmdwwipufg .gt_font_bold { font-weight: bold; }
 #tmdwwipufg .gt_font_italic { font-style: italic; }
 #tmdwwipufg .gt_super { font-size: 65%; }
 #tmdwwipufg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tmdwwipufg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tmdwwipufg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tmdwwipufg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tmdwwipufg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tmdwwipufg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
