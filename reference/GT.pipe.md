# GT.pipe()


Provide a structured way to chain a function for a GT object.


Usage

``` python
GT.pipe(
    func,
    *args,
    **kwargs,
)
```


This function accepts a function that receives a GT object along with optional positional and keyword arguments, returning a GT object. This allows users to easily integrate a function into the chained API offered by **Great Tables**.


## Parameters


`func: Callable[Concatenate[``"GT", P], `<span class="st">`"GT"``]`</span>  
A function that receives a GT object along with optional positional and keyword arguments, returning a GT object.

`*args: P.args`  
Optional positional arguments to be passed to the function.

`**kwargs: P.kwargs`  
Optional keyword arguments to be passed to the function.


## Returns


`gt`  
A GT object.


## Examples

Let's use the `name`, `land_area_km2`, and `density_2021` columns of the [towny](data.towny.md#great_tables.data.towny) dataset to create a table. First, we'll demonstrate using two consecutive calls to the `.tab_style()` method to highlight the maximum value of the `land_area_km2` column with `"lightgray"` and the maximum value of the `density_2021` column with `"lightblue"`.


``` python
import polars as pl
from great_tables import GT, loc, style
from great_tables.data import towny


towny_mini = pl.from_pandas(towny).head(10)

(
    GT(
        towny_mini[["name", "land_area_km2", "density_2021"]],
        rowname_col="name",
    )
    .tab_style(
        style=style.fill(color="lightgray"),
        locations=loc.body(
            columns="land_area_km2",
            rows=pl.col("land_area_km2").eq(pl.col("land_area_km2").max()),
        ),
    )
    .tab_style(
        style=style.fill(color="lightblue"),
        locations=loc.body(
            columns="density_2021",
            rows=pl.col("density_2021").eq(pl.col("density_2021").max()),
        ),
    )
)
```


<style>
#kqwehfrgpc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kqwehfrgpc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kqwehfrgpc p { margin: 0; padding: 0; }
 #kqwehfrgpc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kqwehfrgpc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kqwehfrgpc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kqwehfrgpc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kqwehfrgpc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kqwehfrgpc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqwehfrgpc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kqwehfrgpc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kqwehfrgpc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kqwehfrgpc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kqwehfrgpc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kqwehfrgpc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kqwehfrgpc .gt_spanner_row { border-bottom-style: hidden; }
 #kqwehfrgpc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kqwehfrgpc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kqwehfrgpc .gt_from_md> :first-child { margin-top: 0; }
 #kqwehfrgpc .gt_from_md> :last-child { margin-bottom: 0; }
 #kqwehfrgpc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kqwehfrgpc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kqwehfrgpc .gt_indent_1 { text-indent: 5px; }
 #kqwehfrgpc .gt_indent_2 { text-indent: calc(5px * 2); }
 #kqwehfrgpc .gt_indent_3 { text-indent: calc(5px * 3); }
 #kqwehfrgpc .gt_indent_4 { text-indent: calc(5px * 4); }
 #kqwehfrgpc .gt_indent_5 { text-indent: calc(5px * 5); }
 #kqwehfrgpc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kqwehfrgpc .gt_row_group_first td { border-top-width: 2px; }
 #kqwehfrgpc .gt_row_group_first th { border-top-width: 2px; }
 #kqwehfrgpc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kqwehfrgpc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqwehfrgpc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kqwehfrgpc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kqwehfrgpc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqwehfrgpc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kqwehfrgpc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kqwehfrgpc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kqwehfrgpc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqwehfrgpc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kqwehfrgpc .gt_left { text-align: left; }
 #kqwehfrgpc .gt_center { text-align: center; }
 #kqwehfrgpc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kqwehfrgpc .gt_font_normal { font-weight: normal; }
 #kqwehfrgpc .gt_font_bold { font-weight: bold; }
 #kqwehfrgpc .gt_font_italic { font-style: italic; }
 #kqwehfrgpc .gt_super { font-size: 65%; }
 #kqwehfrgpc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqwehfrgpc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kqwehfrgpc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqwehfrgpc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kqwehfrgpc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kqwehfrgpc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                        | land_area_km2 | density_2021 |
|------------------------|---------------|--------------|
| Addington Highlands    | 1293.99       | 1.96         |
| Adelaide Metcalfe      | 331.11        | 9.09         |
| Adjala-Tosorontio      | 371.53        | 29.58        |
| Admaston/Bromley       | 519.59        | 5.76         |
| Ajax                   | 66.64         | 1900.75      |
| Alberton               | 116.6         | 8.18         |
| Alfred and Plantagenet | 391.79        | 25.39        |
| Algonquin Highlands    | 999.69        | 2.59         |
| Alnwick/Haldimand      | 398.25        | 18.76        |
| Amaranth               | 265.02        | 16.33        |


Next, we'll demonstrate how to achieve the same result using the `.pipe()` method to programmatically style each column.


``` python
columns = ["land_area_km2", "density_2021"]
colors = ["lightgray", "lightblue"]


def tbl_style(gtbl: GT, columns: list[str], colors: list[str]) -> GT:
    for column, color in zip(columns, colors):
        gtbl = gtbl.tab_style(
            style=style.fill(color=color),
            locations=loc.body(columns=column, rows=pl.col(column).eq(pl.col(column).max())),
        )
    return gtbl


(
    GT(
        towny_mini[["name", "land_area_km2", "density_2021"]],
        rowname_col="name",
    ).pipe(tbl_style, columns, colors)
)
```


<style>
#udheuvmcbx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#udheuvmcbx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#udheuvmcbx p { margin: 0; padding: 0; }
 #udheuvmcbx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #udheuvmcbx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #udheuvmcbx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #udheuvmcbx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #udheuvmcbx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #udheuvmcbx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #udheuvmcbx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #udheuvmcbx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #udheuvmcbx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #udheuvmcbx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #udheuvmcbx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #udheuvmcbx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #udheuvmcbx .gt_spanner_row { border-bottom-style: hidden; }
 #udheuvmcbx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #udheuvmcbx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #udheuvmcbx .gt_from_md> :first-child { margin-top: 0; }
 #udheuvmcbx .gt_from_md> :last-child { margin-bottom: 0; }
 #udheuvmcbx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #udheuvmcbx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #udheuvmcbx .gt_indent_1 { text-indent: 5px; }
 #udheuvmcbx .gt_indent_2 { text-indent: calc(5px * 2); }
 #udheuvmcbx .gt_indent_3 { text-indent: calc(5px * 3); }
 #udheuvmcbx .gt_indent_4 { text-indent: calc(5px * 4); }
 #udheuvmcbx .gt_indent_5 { text-indent: calc(5px * 5); }
 #udheuvmcbx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #udheuvmcbx .gt_row_group_first td { border-top-width: 2px; }
 #udheuvmcbx .gt_row_group_first th { border-top-width: 2px; }
 #udheuvmcbx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #udheuvmcbx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #udheuvmcbx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #udheuvmcbx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #udheuvmcbx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #udheuvmcbx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #udheuvmcbx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #udheuvmcbx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #udheuvmcbx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #udheuvmcbx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #udheuvmcbx .gt_left { text-align: left; }
 #udheuvmcbx .gt_center { text-align: center; }
 #udheuvmcbx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #udheuvmcbx .gt_font_normal { font-weight: normal; }
 #udheuvmcbx .gt_font_bold { font-weight: bold; }
 #udheuvmcbx .gt_font_italic { font-style: italic; }
 #udheuvmcbx .gt_super { font-size: 65%; }
 #udheuvmcbx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #udheuvmcbx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #udheuvmcbx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #udheuvmcbx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #udheuvmcbx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #udheuvmcbx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                        | land_area_km2 | density_2021 |
|------------------------|---------------|--------------|
| Addington Highlands    | 1293.99       | 1.96         |
| Adelaide Metcalfe      | 331.11        | 9.09         |
| Adjala-Tosorontio      | 371.53        | 29.58        |
| Admaston/Bromley       | 519.59        | 5.76         |
| Ajax                   | 66.64         | 1900.75      |
| Alberton               | 116.6         | 8.18         |
| Alfred and Plantagenet | 391.79        | 25.39        |
| Algonquin Highlands    | 999.69        | 2.59         |
| Alnwick/Haldimand      | 398.25        | 18.76        |
| Amaranth               | 265.02        | 16.33        |
