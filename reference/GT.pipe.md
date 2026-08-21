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
#cvsvqgpawo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cvsvqgpawo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cvsvqgpawo p { margin: 0; padding: 0; }
 #cvsvqgpawo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cvsvqgpawo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cvsvqgpawo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cvsvqgpawo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cvsvqgpawo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cvsvqgpawo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvsvqgpawo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cvsvqgpawo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cvsvqgpawo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cvsvqgpawo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cvsvqgpawo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cvsvqgpawo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cvsvqgpawo .gt_spanner_row { border-bottom-style: hidden; }
 #cvsvqgpawo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cvsvqgpawo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cvsvqgpawo .gt_from_md> :first-child { margin-top: 0; }
 #cvsvqgpawo .gt_from_md> :last-child { margin-bottom: 0; }
 #cvsvqgpawo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cvsvqgpawo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cvsvqgpawo .gt_indent_1 { text-indent: 5px; }
 #cvsvqgpawo .gt_indent_2 { text-indent: calc(5px * 2); }
 #cvsvqgpawo .gt_indent_3 { text-indent: calc(5px * 3); }
 #cvsvqgpawo .gt_indent_4 { text-indent: calc(5px * 4); }
 #cvsvqgpawo .gt_indent_5 { text-indent: calc(5px * 5); }
 #cvsvqgpawo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cvsvqgpawo .gt_row_group_first td { border-top-width: 2px; }
 #cvsvqgpawo .gt_row_group_first th { border-top-width: 2px; }
 #cvsvqgpawo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cvsvqgpawo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvsvqgpawo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cvsvqgpawo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cvsvqgpawo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvsvqgpawo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cvsvqgpawo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cvsvqgpawo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cvsvqgpawo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvsvqgpawo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cvsvqgpawo .gt_left { text-align: left; }
 #cvsvqgpawo .gt_center { text-align: center; }
 #cvsvqgpawo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cvsvqgpawo .gt_font_normal { font-weight: normal; }
 #cvsvqgpawo .gt_font_bold { font-weight: bold; }
 #cvsvqgpawo .gt_font_italic { font-style: italic; }
 #cvsvqgpawo .gt_super { font-size: 65%; }
 #cvsvqgpawo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvsvqgpawo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cvsvqgpawo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvsvqgpawo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cvsvqgpawo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cvsvqgpawo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ehmzsnsdpw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ehmzsnsdpw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ehmzsnsdpw p { margin: 0; padding: 0; }
 #ehmzsnsdpw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ehmzsnsdpw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ehmzsnsdpw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ehmzsnsdpw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ehmzsnsdpw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ehmzsnsdpw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ehmzsnsdpw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ehmzsnsdpw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ehmzsnsdpw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ehmzsnsdpw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ehmzsnsdpw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ehmzsnsdpw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ehmzsnsdpw .gt_spanner_row { border-bottom-style: hidden; }
 #ehmzsnsdpw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ehmzsnsdpw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ehmzsnsdpw .gt_from_md> :first-child { margin-top: 0; }
 #ehmzsnsdpw .gt_from_md> :last-child { margin-bottom: 0; }
 #ehmzsnsdpw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ehmzsnsdpw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ehmzsnsdpw .gt_indent_1 { text-indent: 5px; }
 #ehmzsnsdpw .gt_indent_2 { text-indent: calc(5px * 2); }
 #ehmzsnsdpw .gt_indent_3 { text-indent: calc(5px * 3); }
 #ehmzsnsdpw .gt_indent_4 { text-indent: calc(5px * 4); }
 #ehmzsnsdpw .gt_indent_5 { text-indent: calc(5px * 5); }
 #ehmzsnsdpw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ehmzsnsdpw .gt_row_group_first td { border-top-width: 2px; }
 #ehmzsnsdpw .gt_row_group_first th { border-top-width: 2px; }
 #ehmzsnsdpw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ehmzsnsdpw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ehmzsnsdpw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ehmzsnsdpw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ehmzsnsdpw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ehmzsnsdpw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ehmzsnsdpw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ehmzsnsdpw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ehmzsnsdpw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ehmzsnsdpw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ehmzsnsdpw .gt_left { text-align: left; }
 #ehmzsnsdpw .gt_center { text-align: center; }
 #ehmzsnsdpw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ehmzsnsdpw .gt_font_normal { font-weight: normal; }
 #ehmzsnsdpw .gt_font_bold { font-weight: bold; }
 #ehmzsnsdpw .gt_font_italic { font-style: italic; }
 #ehmzsnsdpw .gt_super { font-size: 65%; }
 #ehmzsnsdpw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ehmzsnsdpw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ehmzsnsdpw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ehmzsnsdpw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ehmzsnsdpw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ehmzsnsdpw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
