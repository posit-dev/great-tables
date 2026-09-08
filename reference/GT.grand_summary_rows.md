# GT.grand_summary_rows()


Add grand summary rows to the table.


Usage

``` python
GT.grand_summary_rows(
    *,
    fns,
    fmt=None,
    columns=None,
    side="bottom",
    missing_text="---",
)
```


Add grand summary rows by using the table data and any suitable aggregation functions. With grand summary rows, all of the available data in the gt table is incorporated (regardless of whether some of the data are part of row groups). Multiple grand summary rows can be added via expressions given to fns. You can selectively format the values in the resulting grand summary cells by use of formatting expressions from the `vals.fmt_*` class of functions.

Note that currently all arguments are keyword-only, since the final positions may change.


## Parameters


`fns: dict[str, PlExpr] | dict[str, Callable[[TblData], Any]]`  
A dictionary mapping row labels to aggregation expressions. Can be either Polars expressions or callable functions that take the entire DataFrame and return aggregated results. Each key becomes the label for a grand summary row.

`fmt: FormatFn | None = None`  
A formatting function from the `vals.fmt_*` family (e.g., [vals.fmt_number](vals.fmt_number.md#great_tables.vals.fmt_number), [vals.fmt_currency](vals.fmt_currency.md#great_tables.vals.fmt_currency)) to apply to the summary row values. If `None`, no formatting is applied.

`columns: SelectExpr = None`  
Currently, this function does not support selection by columns. If you would like to choose which columns to summarize, you can select columns within the functions given to `fns=`. See examples below for more explicit cases.

`side: Literal[``"bottom", `<span class="st">`"top"``]`</span>` = ``"bottom"`  
Should the grand summary rows be placed at the `"bottom"` (the default) or the `"top"` of the table?

`missing_text: str = ``"--"`  
The text to be used in summary cells with no data outputs.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use a subset of the [sp500](data.sp500.md#great_tables.data.sp500) dataset to create a table with grand summary rows. We'll calculate min, max, and mean values for the numeric columns. Notice the different approaches to selecting columns to apply the aggregations to: we can use polars selectors or select the columns directly.


``` python
import polars as pl
import polars.selectors as cs
from great_tables import GT, vals, style, loc
from great_tables.data import sp500

sp500_mini = (
    pl.from_pandas(sp500)
    .slice(0, 7)
    .drop(["volume", "adj_close"])
)

(
    GT(sp500_mini, rowname_col="date")
    .grand_summary_rows(
        fns={
            "Minimum": pl.min("open", "high", "low", "close"),
            "Maximum": pl.col("open", "high", "low", "close").max(),
            "Average": cs.numeric().mean(),
        },
        fmt=vals.fmt_currency,
    )
    .tab_style(
        style=[
            style.text(color="crimson"),
            style.fill(color="lightgray"),
        ],
        locations=loc.grand_summary(),
    )
)
```


<style>
#khxkdwnedt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#khxkdwnedt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#khxkdwnedt p { margin: 0; padding: 0; }
 #khxkdwnedt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #khxkdwnedt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #khxkdwnedt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #khxkdwnedt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #khxkdwnedt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khxkdwnedt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khxkdwnedt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khxkdwnedt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #khxkdwnedt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #khxkdwnedt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #khxkdwnedt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #khxkdwnedt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #khxkdwnedt .gt_spanner_row { border-bottom-style: hidden; }
 #khxkdwnedt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #khxkdwnedt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #khxkdwnedt .gt_from_md> :first-child { margin-top: 0; }
 #khxkdwnedt .gt_from_md> :last-child { margin-bottom: 0; }
 #khxkdwnedt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #khxkdwnedt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #khxkdwnedt .gt_indent_1 { text-indent: 5px; }
 #khxkdwnedt .gt_indent_2 { text-indent: calc(5px * 2); }
 #khxkdwnedt .gt_indent_3 { text-indent: calc(5px * 3); }
 #khxkdwnedt .gt_indent_4 { text-indent: calc(5px * 4); }
 #khxkdwnedt .gt_indent_5 { text-indent: calc(5px * 5); }
 #khxkdwnedt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #khxkdwnedt .gt_row_group_first td { border-top-width: 2px; }
 #khxkdwnedt .gt_row_group_first th { border-top-width: 2px; }
 #khxkdwnedt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #khxkdwnedt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khxkdwnedt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khxkdwnedt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #khxkdwnedt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khxkdwnedt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khxkdwnedt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #khxkdwnedt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #khxkdwnedt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khxkdwnedt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khxkdwnedt .gt_left { text-align: left; }
 #khxkdwnedt .gt_center { text-align: center; }
 #khxkdwnedt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #khxkdwnedt .gt_font_normal { font-weight: normal; }
 #khxkdwnedt .gt_font_bold { font-weight: bold; }
 #khxkdwnedt .gt_font_italic { font-style: italic; }
 #khxkdwnedt .gt_super { font-size: 65%; }
 #khxkdwnedt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khxkdwnedt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #khxkdwnedt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khxkdwnedt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khxkdwnedt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #khxkdwnedt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|            | open       | high       | low        | close      |
|------------|------------|------------|------------|------------|
| 2015-12-31 | 2060.5901  | 2062.54    | 2043.62    | 2043.9399  |
| 2015-12-30 | 2077.3401  | 2077.3401  | 2061.97    | 2063.3601  |
| 2015-12-29 | 2060.54    | 2081.5601  | 2060.54    | 2078.3601  |
| 2015-12-28 | 2057.77    | 2057.77    | 2044.2     | 2056.5     |
| 2015-12-24 | 2063.52    | 2067.3601  | 2058.73    | 2060.99    |
| 2015-12-23 | 2042.2     | 2064.73    | 2042.2     | 2064.29    |
| 2015-12-22 | 2023.15    | 2042.74    | 2020.49    | 2038.97    |
| Minimum    | \$2,023.15 | \$2,042.74 | \$2,020.49 | \$2,038.97 |
| Maximum    | \$2,077.34 | \$2,081.56 | \$2,061.97 | \$2,078.36 |
| Average    | \$2,055.02 | \$2,064.86 | \$2,047.39 | \$2,058.06 |


We can also use custom callable functions to create more complex summary calculations. Notice here that grand summary rows can be placed at the top of the table and formatted with currency notation, by passing a formatter from the `vals.fmt_*` class of functions.


``` python
from great_tables import GT, style, loc, vals
from great_tables.data import gtcars

def pd_median(df):
    return df.median(numeric_only=True)


(
    GT(
        gtcars[["mfr", "model", "hp", "trq", "mpg_c"]].head(6),
        rowname_col="model",
    )
    .fmt_integer(columns=["hp", "trq", "mpg_c"])
    .grand_summary_rows(
        fns={
            "Min": lambda df: df.min(numeric_only=True),
            "Max": lambda df: df.max(numeric_only=True),
            "Median": pd_median,
        },
        side="top",
        fmt=vals.fmt_integer,
    )
    .tab_style(
        style=[style.text(color="crimson", weight="bold"), style.fill(color="lightgray")],
        locations=loc.grand_summary_stub(),
    )
)
```


<style>
#hnvemvlast table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hnvemvlast thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hnvemvlast p { margin: 0; padding: 0; }
 #hnvemvlast .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hnvemvlast .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hnvemvlast .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hnvemvlast .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hnvemvlast .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hnvemvlast .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hnvemvlast .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hnvemvlast .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hnvemvlast .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hnvemvlast .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hnvemvlast .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hnvemvlast .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hnvemvlast .gt_spanner_row { border-bottom-style: hidden; }
 #hnvemvlast .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hnvemvlast .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hnvemvlast .gt_from_md> :first-child { margin-top: 0; }
 #hnvemvlast .gt_from_md> :last-child { margin-bottom: 0; }
 #hnvemvlast .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hnvemvlast .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hnvemvlast .gt_indent_1 { text-indent: 5px; }
 #hnvemvlast .gt_indent_2 { text-indent: calc(5px * 2); }
 #hnvemvlast .gt_indent_3 { text-indent: calc(5px * 3); }
 #hnvemvlast .gt_indent_4 { text-indent: calc(5px * 4); }
 #hnvemvlast .gt_indent_5 { text-indent: calc(5px * 5); }
 #hnvemvlast .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hnvemvlast .gt_row_group_first td { border-top-width: 2px; }
 #hnvemvlast .gt_row_group_first th { border-top-width: 2px; }
 #hnvemvlast .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hnvemvlast .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hnvemvlast .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hnvemvlast .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hnvemvlast .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hnvemvlast .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hnvemvlast .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hnvemvlast .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hnvemvlast .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hnvemvlast .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hnvemvlast .gt_left { text-align: left; }
 #hnvemvlast .gt_center { text-align: center; }
 #hnvemvlast .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hnvemvlast .gt_font_normal { font-weight: normal; }
 #hnvemvlast .gt_font_bold { font-weight: bold; }
 #hnvemvlast .gt_font_italic { font-style: italic; }
 #hnvemvlast .gt_super { font-size: 65%; }
 #hnvemvlast .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hnvemvlast .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hnvemvlast .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hnvemvlast .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hnvemvlast .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hnvemvlast .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|              | mfr     | hp  | trq | mpg_c |
|--------------|---------|-----|-----|-------|
| Min          | ---     | 553 | 398 | 11    |
| Max          | ---     | 661 | 561 | 16    |
| Median       | ---     | 580 | 474 | 13    |
| GT           | Ford    | 647 | 550 | 11    |
| 458 Speciale | Ferrari | 597 | 398 | 13    |
| 458 Spider   | Ferrari | 562 | 398 | 13    |
| 458 Italia   | Ferrari | 562 | 398 | 13    |
| 488 GTB      | Ferrari | 661 | 561 | 15    |
| California   | Ferrari | 553 | 557 | 16    |
