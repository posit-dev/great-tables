# Adding Plots to Great Tables

While working on [**gt-extras**](https://posit-dev.github.io/gt-extras/articles/intro.html), I've been exploring how to add small plots to Great Tables. These can go by many names, like spark lines, nanoplots, and so on. In this post, I'll look at three approaches I tried: adding plots with [`plotnine`](https://plotnine.org/), [`svg.py`](https://github.com/orsinium-labs/svg.py), or adding HTML directly. In the first two cases, the plots are SVGs, while the latter entails a collection of composed HTML div elements.

Here are the pieces I'll cover:

- **svg.py**: creating your own tiny chart directly for a row.
- **direct HTML**: adding HTML divs directly.
- **plotnine**: adding a full, stripped-down chart to a row.

In the end, it's often simplest to use `svg.py`, since you can create basic charts with minimal overhead. Building elements with HTML has even *less* overhead, but it is also slightly less user-friendly. At the other end of the spectrum, as your charts become more complex, using existing packages like the more exhaustive `plotnine` is a good alternative.


<style>
#pfoheewjuk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pfoheewjuk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pfoheewjuk p { margin: 0; padding: 0; }
 #pfoheewjuk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pfoheewjuk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pfoheewjuk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pfoheewjuk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pfoheewjuk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pfoheewjuk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfoheewjuk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pfoheewjuk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pfoheewjuk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pfoheewjuk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pfoheewjuk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pfoheewjuk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pfoheewjuk .gt_spanner_row { border-bottom-style: hidden; }
 #pfoheewjuk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pfoheewjuk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pfoheewjuk .gt_from_md> :first-child { margin-top: 0; }
 #pfoheewjuk .gt_from_md> :last-child { margin-bottom: 0; }
 #pfoheewjuk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pfoheewjuk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pfoheewjuk .gt_indent_1 { text-indent: 5px; }
 #pfoheewjuk .gt_indent_2 { text-indent: calc(5px * 2); }
 #pfoheewjuk .gt_indent_3 { text-indent: calc(5px * 3); }
 #pfoheewjuk .gt_indent_4 { text-indent: calc(5px * 4); }
 #pfoheewjuk .gt_indent_5 { text-indent: calc(5px * 5); }
 #pfoheewjuk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pfoheewjuk .gt_row_group_first td { border-top-width: 2px; }
 #pfoheewjuk .gt_row_group_first th { border-top-width: 2px; }
 #pfoheewjuk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pfoheewjuk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfoheewjuk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pfoheewjuk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pfoheewjuk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfoheewjuk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pfoheewjuk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pfoheewjuk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pfoheewjuk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfoheewjuk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pfoheewjuk .gt_left { text-align: left; }
 #pfoheewjuk .gt_center { text-align: center; }
 #pfoheewjuk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pfoheewjuk .gt_font_normal { font-weight: normal; }
 #pfoheewjuk .gt_font_bold { font-weight: bold; }
 #pfoheewjuk .gt_font_italic { font-style: italic; }
 #pfoheewjuk .gt_super { font-size: 65%; }
 #pfoheewjuk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfoheewjuk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pfoheewjuk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfoheewjuk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pfoheewjuk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pfoheewjuk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Animal  | Legs | Plot |
|---------|------|------|
| Ostrich | 2    | 2    |
| Spider  | 8    | 8    |
| Lion    | 4    | 4    |


Here is the final result:


Code

``` python
import polars as pl
from great_tables import GT
from svg import SVG, Rect, Line

df = pl.DataFrame({"Animal": ["Ostrich", "Spider", "Lion"], "Legs": [2, 8, 4], "Plot": [2, 8, 4]})

width = 50
height = 30
max_legs_value = df["Legs"].max()


def create_plot_svg_py(val: int) -> str:
    canvas = SVG(
        width=width,
        height=height,
        elements=[
            Rect(
                x=0,
                y=height / 4,
                width=width * (val / max_legs_value),
                height=height / 2,
                fill="blue",
            ),
            Line(x1=0, x2=0, y1=0, y2=height, stroke="black"),
        ],
    )

    html = f"<div>{canvas}</div>"
    return html


GT(df).fmt(fns=create_plot_svg_py, columns=["Plot"])
```


<style>
#fkrykkirum table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fkrykkirum thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fkrykkirum p { margin: 0; padding: 0; }
 #fkrykkirum .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fkrykkirum .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fkrykkirum .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fkrykkirum .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fkrykkirum .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fkrykkirum .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fkrykkirum .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fkrykkirum .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fkrykkirum .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fkrykkirum .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fkrykkirum .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fkrykkirum .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fkrykkirum .gt_spanner_row { border-bottom-style: hidden; }
 #fkrykkirum .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fkrykkirum .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fkrykkirum .gt_from_md> :first-child { margin-top: 0; }
 #fkrykkirum .gt_from_md> :last-child { margin-bottom: 0; }
 #fkrykkirum .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fkrykkirum .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fkrykkirum .gt_indent_1 { text-indent: 5px; }
 #fkrykkirum .gt_indent_2 { text-indent: calc(5px * 2); }
 #fkrykkirum .gt_indent_3 { text-indent: calc(5px * 3); }
 #fkrykkirum .gt_indent_4 { text-indent: calc(5px * 4); }
 #fkrykkirum .gt_indent_5 { text-indent: calc(5px * 5); }
 #fkrykkirum .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fkrykkirum .gt_row_group_first td { border-top-width: 2px; }
 #fkrykkirum .gt_row_group_first th { border-top-width: 2px; }
 #fkrykkirum .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fkrykkirum .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fkrykkirum .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fkrykkirum .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fkrykkirum .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fkrykkirum .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fkrykkirum .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fkrykkirum .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fkrykkirum .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fkrykkirum .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fkrykkirum .gt_left { text-align: left; }
 #fkrykkirum .gt_center { text-align: center; }
 #fkrykkirum .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fkrykkirum .gt_font_normal { font-weight: normal; }
 #fkrykkirum .gt_font_bold { font-weight: bold; }
 #fkrykkirum .gt_font_italic { font-style: italic; }
 #fkrykkirum .gt_super { font-size: 65%; }
 #fkrykkirum .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fkrykkirum .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fkrykkirum .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fkrykkirum .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fkrykkirum .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fkrykkirum .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="Animal" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Animal</th>
<th id="Legs" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Legs</th>
<th id="Plot" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Plot</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ostrich</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right"><div>
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MCIgaGVpZ2h0PSIzMCI+PHJlY3QgeD0iMCIgeT0iNy41IiB3aWR0aD0iMTIuNSIgaGVpZ2h0PSIxNS4wIiBmaWxsPSJibHVlIiAvPjxsaW5lIHN0cm9rZT0iYmxhY2siIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIzMCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Spider</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right"><div>
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MCIgaGVpZ2h0PSIzMCI+PHJlY3QgeD0iMCIgeT0iNy41IiB3aWR0aD0iNTAuMCIgaGVpZ2h0PSIxNS4wIiBmaWxsPSJibHVlIiAvPjxsaW5lIHN0cm9rZT0iYmxhY2siIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIzMCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Lion</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right"><div>
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MCIgaGVpZ2h0PSIzMCI+PHJlY3QgeD0iMCIgeT0iNy41IiB3aWR0aD0iMjUuMCIgaGVpZ2h0PSIxNS4wIiBmaWxsPSJibHVlIiAvPjxsaW5lIHN0cm9rZT0iYmxhY2siIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIzMCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
</tbody>
</table>


# Setup

Here is the code to start:


``` python
import polars as pl
from great_tables import GT

df = pl.DataFrame(
    {
        "Animal": ["Ostrich", "Spider", "Lion"],
        "Legs": [2, 8, 4],
        "Plot": [2, 8, 4],
    }
)

gt = GT(df)
```


# The Binding Component: GT.fmt()

Let's take advantage of the [`fmt()`](https://posit-dev.github.io/great-tables/reference/GT.fmt.html#great_tables.GT.fmt) method to apply a plotting function that formats our row values into plots. To see how we might use [fmt()](../../reference/GT.fmt.md#great_tables.GT.fmt), we first need to define a formatting function to apply to each cell in a column. It will take as input the value in the cell, and should return whatever you want in that cell. Before plotting, let's imagine we wanted to replace the number with a tally of the number of legs:


``` python
def create_leg_tally(value: int) -> str:
    return "|" * value


gt.fmt(fns=create_leg_tally, columns="Plot")
```


<style>
#mxzgvbxhoq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mxzgvbxhoq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mxzgvbxhoq p { margin: 0; padding: 0; }
 #mxzgvbxhoq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mxzgvbxhoq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mxzgvbxhoq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mxzgvbxhoq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mxzgvbxhoq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mxzgvbxhoq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mxzgvbxhoq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mxzgvbxhoq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mxzgvbxhoq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mxzgvbxhoq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mxzgvbxhoq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mxzgvbxhoq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mxzgvbxhoq .gt_spanner_row { border-bottom-style: hidden; }
 #mxzgvbxhoq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mxzgvbxhoq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mxzgvbxhoq .gt_from_md> :first-child { margin-top: 0; }
 #mxzgvbxhoq .gt_from_md> :last-child { margin-bottom: 0; }
 #mxzgvbxhoq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mxzgvbxhoq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mxzgvbxhoq .gt_indent_1 { text-indent: 5px; }
 #mxzgvbxhoq .gt_indent_2 { text-indent: calc(5px * 2); }
 #mxzgvbxhoq .gt_indent_3 { text-indent: calc(5px * 3); }
 #mxzgvbxhoq .gt_indent_4 { text-indent: calc(5px * 4); }
 #mxzgvbxhoq .gt_indent_5 { text-indent: calc(5px * 5); }
 #mxzgvbxhoq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mxzgvbxhoq .gt_row_group_first td { border-top-width: 2px; }
 #mxzgvbxhoq .gt_row_group_first th { border-top-width: 2px; }
 #mxzgvbxhoq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mxzgvbxhoq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mxzgvbxhoq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mxzgvbxhoq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mxzgvbxhoq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mxzgvbxhoq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mxzgvbxhoq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mxzgvbxhoq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mxzgvbxhoq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mxzgvbxhoq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mxzgvbxhoq .gt_left { text-align: left; }
 #mxzgvbxhoq .gt_center { text-align: center; }
 #mxzgvbxhoq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mxzgvbxhoq .gt_font_normal { font-weight: normal; }
 #mxzgvbxhoq .gt_font_bold { font-weight: bold; }
 #mxzgvbxhoq .gt_font_italic { font-style: italic; }
 #mxzgvbxhoq .gt_super { font-size: 65%; }
 #mxzgvbxhoq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mxzgvbxhoq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mxzgvbxhoq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mxzgvbxhoq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mxzgvbxhoq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mxzgvbxhoq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Animal  | Legs | Plot             |
|---------|------|------------------|
| Ostrich | 2    | \|\|             |
| Spider  | 8    | \|\|\|\|\|\|\|\| |
| Lion    | 4    | \|\|\|\|         |


# A Lightweight Approach: Svg.py

Now we can apply that same logic to making our plots. Let's start with the function that will eventually be passed into [fmt()](../../reference/GT.fmt.md#great_tables.GT.fmt):


``` python
from svg import SVG, Rect, Line

height = 30
width = 50


def create_plot_svg_py(val: int) -> str:
    canvas = SVG(
        width=width,
        height=height,
        elements=[
            Rect(
                x=0,
                y=height / 4,
                width=width * (val / max_legs_value),
                height=height / 2,
                fill="blue",
            ),
            Line(x1=0, x2=0, y1=0, y2=height, stroke="black"),
        ],
    )

    html = f"<div>{canvas}</div>"
    return html
```


Here you get to call [fmt()](../../reference/GT.fmt.md#great_tables.GT.fmt) to modify the column you want to apply the plotting function to.


``` python
gt.fmt(fns=create_plot_svg_py, columns="Plot")
```


<style>
#dstciyzvla table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dstciyzvla thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dstciyzvla p { margin: 0; padding: 0; }
 #dstciyzvla .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dstciyzvla .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dstciyzvla .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dstciyzvla .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dstciyzvla .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dstciyzvla .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dstciyzvla .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dstciyzvla .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dstciyzvla .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dstciyzvla .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dstciyzvla .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dstciyzvla .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dstciyzvla .gt_spanner_row { border-bottom-style: hidden; }
 #dstciyzvla .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dstciyzvla .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dstciyzvla .gt_from_md> :first-child { margin-top: 0; }
 #dstciyzvla .gt_from_md> :last-child { margin-bottom: 0; }
 #dstciyzvla .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dstciyzvla .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dstciyzvla .gt_indent_1 { text-indent: 5px; }
 #dstciyzvla .gt_indent_2 { text-indent: calc(5px * 2); }
 #dstciyzvla .gt_indent_3 { text-indent: calc(5px * 3); }
 #dstciyzvla .gt_indent_4 { text-indent: calc(5px * 4); }
 #dstciyzvla .gt_indent_5 { text-indent: calc(5px * 5); }
 #dstciyzvla .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dstciyzvla .gt_row_group_first td { border-top-width: 2px; }
 #dstciyzvla .gt_row_group_first th { border-top-width: 2px; }
 #dstciyzvla .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dstciyzvla .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dstciyzvla .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dstciyzvla .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dstciyzvla .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dstciyzvla .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dstciyzvla .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dstciyzvla .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dstciyzvla .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dstciyzvla .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dstciyzvla .gt_left { text-align: left; }
 #dstciyzvla .gt_center { text-align: center; }
 #dstciyzvla .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dstciyzvla .gt_font_normal { font-weight: normal; }
 #dstciyzvla .gt_font_bold { font-weight: bold; }
 #dstciyzvla .gt_font_italic { font-style: italic; }
 #dstciyzvla .gt_super { font-size: 65%; }
 #dstciyzvla .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dstciyzvla .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dstciyzvla .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dstciyzvla .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dstciyzvla .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dstciyzvla .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="Animal" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Animal</th>
<th id="Legs" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Legs</th>
<th id="Plot" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Plot</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ostrich</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right"><div>
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MCIgaGVpZ2h0PSIzMCI+PHJlY3QgeD0iMCIgeT0iNy41IiB3aWR0aD0iMTIuNSIgaGVpZ2h0PSIxNS4wIiBmaWxsPSJibHVlIiAvPjxsaW5lIHN0cm9rZT0iYmxhY2siIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIzMCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Spider</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right"><div>
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MCIgaGVpZ2h0PSIzMCI+PHJlY3QgeD0iMCIgeT0iNy41IiB3aWR0aD0iNTAuMCIgaGVpZ2h0PSIxNS4wIiBmaWxsPSJibHVlIiAvPjxsaW5lIHN0cm9rZT0iYmxhY2siIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIzMCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Lion</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right"><div>
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MCIgaGVpZ2h0PSIzMCI+PHJlY3QgeD0iMCIgeT0iNy41IiB3aWR0aD0iMjUuMCIgaGVpZ2h0PSIxNS4wIiBmaWxsPSJibHVlIiAvPjxsaW5lIHN0cm9rZT0iYmxhY2siIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIzMCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
</tbody>
</table>


This was very direct, we didn't have save to a buffer or import heavy duty plotting functions. We built the string with the help of `svg.py` and were able to insert into the table. See the string below:


    '<div><svg xmlns="http://www.w3.org/2000/svg" width="50" height="30"><rect x="0" y="7.5" width="25.0" height="15.0" fill="blue"/><line stroke="black" x1="0" y1="0" x2="0" y2="30"/></svg></div>'


Even in its outputted form the string is still easily readable, which is another upside of using an SVG generation package.


# Extreme Minimalism: Adding HTML directly

In the previous section, note that `svg.py` simply generated a string of HTML. You can do the same thing directly.


``` python
def create_plot_html(val: int) -> str:
    bar_element = f"""
    <div style="position: absolute;
                width: {width * val / max_legs_value}px;
                height: {height / 2}px;
                background-color: purple;
                margin-top: {height / 4}px;
    "></div>"""

    line_element = """
    <div style="position: absolute;
                top: 0;
                bottom: 0;
                width: 1px;
                background-color: black;
    "></div>"""

    html = f"""
    <div style="position: relative; width: {width}px; height: {height}px;">
        {bar_element}
        {line_element}
    </div>
    """

    return html
```


Now that we've defined our `create_plot_*` formatting function, the call to [fmt()](../../reference/GT.fmt.md#great_tables.GT.fmt) is identical to the one above.


``` python
gt.fmt(fns=create_plot_html, columns="Plot")
```


<style>
#mgpmlsednk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mgpmlsednk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mgpmlsednk p { margin: 0; padding: 0; }
 #mgpmlsednk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mgpmlsednk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mgpmlsednk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mgpmlsednk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mgpmlsednk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mgpmlsednk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mgpmlsednk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mgpmlsednk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mgpmlsednk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mgpmlsednk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mgpmlsednk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mgpmlsednk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mgpmlsednk .gt_spanner_row { border-bottom-style: hidden; }
 #mgpmlsednk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mgpmlsednk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mgpmlsednk .gt_from_md> :first-child { margin-top: 0; }
 #mgpmlsednk .gt_from_md> :last-child { margin-bottom: 0; }
 #mgpmlsednk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mgpmlsednk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mgpmlsednk .gt_indent_1 { text-indent: 5px; }
 #mgpmlsednk .gt_indent_2 { text-indent: calc(5px * 2); }
 #mgpmlsednk .gt_indent_3 { text-indent: calc(5px * 3); }
 #mgpmlsednk .gt_indent_4 { text-indent: calc(5px * 4); }
 #mgpmlsednk .gt_indent_5 { text-indent: calc(5px * 5); }
 #mgpmlsednk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mgpmlsednk .gt_row_group_first td { border-top-width: 2px; }
 #mgpmlsednk .gt_row_group_first th { border-top-width: 2px; }
 #mgpmlsednk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mgpmlsednk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mgpmlsednk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mgpmlsednk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mgpmlsednk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mgpmlsednk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mgpmlsednk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mgpmlsednk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mgpmlsednk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mgpmlsednk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mgpmlsednk .gt_left { text-align: left; }
 #mgpmlsednk .gt_center { text-align: center; }
 #mgpmlsednk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mgpmlsednk .gt_font_normal { font-weight: normal; }
 #mgpmlsednk .gt_font_bold { font-weight: bold; }
 #mgpmlsednk .gt_font_italic { font-style: italic; }
 #mgpmlsednk .gt_super { font-size: 65%; }
 #mgpmlsednk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mgpmlsednk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mgpmlsednk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mgpmlsednk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mgpmlsednk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mgpmlsednk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="Animal" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Animal</th>
<th id="Legs" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Legs</th>
<th id="Plot" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Plot</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ostrich</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right"><div style="position: relative; width: 50px; height: 30px;">


</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Spider</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right"><div style="position: relative; width: 50px; height: 30px;">


</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Lion</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right"><div style="position: relative; width: 50px; height: 30px;">


</div></td>
</tr>
</tbody>
</table>


At first glance, encoding HTML in multi-line strings may not be aesthetically pleasing, nor is it particularly more lightweight than `svg.py`. Still, it provides a good alternative if you are like me and insist on being as close to the output as possible. Separately, I have found the inclusion of text to be simpler with HTML on account of the default text handling behavior that comes along with it.


# A Comprehensive Package: Plotnine


``` python
from io import StringIO
from plotnine import (
    ggplot,
    aes,
    coord_flip,
    geom_col,
    scale_y_continuous,
    scale_x_continuous,
    theme_void,
    geom_hline,
)

max_legs_value = df["Legs"].max()


def create_plot_plotnine(val: int) -> str:
    plot = (
        ggplot()
        + aes(x=1, y=val)
        + geom_col(width=0.5, fill="green", show_legend=False)
        + scale_y_continuous(limits=(0, max_legs_value))
        + scale_x_continuous(limits=(0.5, 1.5))
        + coord_flip()
        + theme_void()
        + geom_hline(yintercept=0)
    )

    buf = StringIO()
    plot.save(buf, format="svg", width=0.5, height=0.3, verbose=False)
    svg_content = buf.getvalue()
    buf.close()

    html = f"<div>{svg_content}</div>"
    return html


# This might be familiar by now
gt.fmt(fns=create_plot_plotnine, columns="Plot")
```


<style>
#snxuzdmouv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#snxuzdmouv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#snxuzdmouv p { margin: 0; padding: 0; }
 #snxuzdmouv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #snxuzdmouv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #snxuzdmouv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #snxuzdmouv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #snxuzdmouv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #snxuzdmouv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #snxuzdmouv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #snxuzdmouv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #snxuzdmouv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #snxuzdmouv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #snxuzdmouv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #snxuzdmouv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #snxuzdmouv .gt_spanner_row { border-bottom-style: hidden; }
 #snxuzdmouv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #snxuzdmouv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #snxuzdmouv .gt_from_md> :first-child { margin-top: 0; }
 #snxuzdmouv .gt_from_md> :last-child { margin-bottom: 0; }
 #snxuzdmouv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #snxuzdmouv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #snxuzdmouv .gt_indent_1 { text-indent: 5px; }
 #snxuzdmouv .gt_indent_2 { text-indent: calc(5px * 2); }
 #snxuzdmouv .gt_indent_3 { text-indent: calc(5px * 3); }
 #snxuzdmouv .gt_indent_4 { text-indent: calc(5px * 4); }
 #snxuzdmouv .gt_indent_5 { text-indent: calc(5px * 5); }
 #snxuzdmouv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #snxuzdmouv .gt_row_group_first td { border-top-width: 2px; }
 #snxuzdmouv .gt_row_group_first th { border-top-width: 2px; }
 #snxuzdmouv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #snxuzdmouv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #snxuzdmouv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #snxuzdmouv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #snxuzdmouv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #snxuzdmouv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #snxuzdmouv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #snxuzdmouv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #snxuzdmouv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #snxuzdmouv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #snxuzdmouv .gt_left { text-align: left; }
 #snxuzdmouv .gt_center { text-align: center; }
 #snxuzdmouv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #snxuzdmouv .gt_font_normal { font-weight: normal; }
 #snxuzdmouv .gt_font_bold { font-weight: bold; }
 #snxuzdmouv .gt_font_italic { font-style: italic; }
 #snxuzdmouv .gt_super { font-size: 65%; }
 #snxuzdmouv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #snxuzdmouv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #snxuzdmouv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #snxuzdmouv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #snxuzdmouv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #snxuzdmouv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="Animal" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Animal</th>
<th id="Legs" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Legs</th>
<th id="Plot" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Plot</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ostrich</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right"><div>
<img src="data:image/svg+xml;base64,PHN2ZyB4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgd2lkdGg9IjM2cHQiIGhlaWdodD0iMjEuNnB0IiB2aWV3Ym94PSIwIDAgMzYgMjEuNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiPgogPG1ldGFkYXRhPgogIDxyZGYgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICA8d29yaz4KICAgIDx0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3B1cmwub3JnL2RjL2RjbWl0eXBlL1N0aWxsSW1hZ2UiPjwvdHlwZT4KICAgIDxkYXRlPjIwMjYtMDctMjRUMjA6MzQ6MDQuNjM3NDY4PC9kYXRlPgogICAgPGZvcm1hdD5pbWFnZS9zdmcreG1sPC9mb3JtYXQ+CiAgICA8Y3JlYXRvcj4KICAgICA8YWdlbnQ+CiAgICAgIDx0aXRsZT5NYXRwbG90bGliIHYzLjExLjEsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvPC90aXRsZT4KICAgICA8L2FnZW50PgogICAgPC9jcmVhdG9yPgogICA8L3dvcms+CiAgPC9yZGY+CiA8L21ldGFkYXRhPgogPGRlZnM+CiAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4qe3N0cm9rZS1saW5lam9pbjogcm91bmQ7IHN0cm9rZS1saW5lY2FwOiBidXR0fTwvc3R5bGU+CiA8L2RlZnM+CiA8ZyBpZD0iZmlndXJlXzEiPgogIDxnIGlkPSJwYXRjaF8xIj4KICAgPHBhdGggZD0iTSAwIDIxLjYgCkwgMzYgMjEuNiAKTCAzNiAwIApMIDAgMCAKegoiIHN0eWxlPSJmaWxsOiAjZmZmZmZmIiAvPgogIDwvZz4KICA8ZyBpZD0iYXhlc18xIj4KICAgPGcgaWQ9Im1hdHBsb3RsaWIuYXhpc18xIj4KICAgIDxnIGlkPSJ4dGlja18xIj48L2c+CiAgICA8ZyBpZD0ieHRpY2tfMiI+PC9nPgogICAgPGcgaWQ9Inh0aWNrXzMiPjwvZz4KICAgIDxnIGlkPSJ4dGlja180Ij48L2c+CiAgICA8ZyBpZD0ieHRpY2tfNSI+PC9nPgogICAgPGcgaWQ9Inh0aWNrXzYiPjwvZz4KICAgIDxnIGlkPSJ4dGlja183Ij48L2c+CiAgICA8ZyBpZD0ieHRpY2tfOCI+PC9nPgogICAgPGcgaWQ9Inh0aWNrXzkiPjwvZz4KICAgPC9nPgogICA8ZyBpZD0ibWF0cGxvdGxpYi5heGlzXzIiPgogICAgPGcgaWQ9Inl0aWNrXzEiPjwvZz4KICAgIDxnIGlkPSJ5dGlja18yIj48L2c+CiAgICA8ZyBpZD0ieXRpY2tfMyI+PC9nPgogICAgPGcgaWQ9Inl0aWNrXzQiPjwvZz4KICAgIDxnIGlkPSJ5dGlja181Ij48L2c+CiAgICA8ZyBpZD0ieXRpY2tfNiI+PC9nPgogICAgPGcgaWQ9Inl0aWNrXzciPjwvZz4KICAgIDxnIGlkPSJ5dGlja184Ij48L2c+CiAgICA8ZyBpZD0ieXRpY2tfOSI+PC9nPgogICA8L2c+CiAgIDxnIGlkPSJQb2x5Q29sbGVjdGlvbl8xIj4KICAgIDxwYXRoIGQ9Ik0gMS42MzYzNjQgMTUuNzA5MDkxIApMIDEuNjM2MzY0IDUuODkwOTA5IApMIDkuODE4MTgyIDUuODkwOTA5IApMIDkuODE4MTgyIDE1LjcwOTA5MSAKegoiIGNsaXAtcGF0aD0idXJsKCNwYzExNWFlZjEyOCkiIHN0eWxlPSJmaWxsOiAjMDA4MDAwIiAvPgogICA8L2c+CiAgIDxnIGlkPSJMaW5lQ29sbGVjdGlvbl8xIj4KICAgIDxwYXRoIGQ9Ik0gMS42MzYzNjQgMjEuNiAKTCAxLjYzNjM2NCAtMCAKIiBjbGlwLXBhdGg9InVybCgjcGMxMTVhZWYxMjgpIiBzdHlsZT0iZmlsbDogbm9uZTsgc3Ryb2tlOiAjMDAwMDAwOyBzdHJva2Utd2lkdGg6IDAuODg2MjI3IiAvPgogICA8L2c+CiAgPC9nPgogPC9nPgogPGRlZnM+CiAgPGNsaXBwYXRoIGlkPSJwYzExNWFlZjEyOCI+CiAgIDxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSIzNiIgaGVpZ2h0PSIyMS42IiAvPgogIDwvY2xpcHBhdGg+CiA8L2RlZnM+Cjwvc3ZnPg==" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Spider</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right"><div>
<img src="data:image/svg+xml;base64,PHN2ZyB4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgd2lkdGg9IjM2cHQiIGhlaWdodD0iMjEuNnB0IiB2aWV3Ym94PSIwIDAgMzYgMjEuNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiPgogPG1ldGFkYXRhPgogIDxyZGYgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICA8d29yaz4KICAgIDx0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3B1cmwub3JnL2RjL2RjbWl0eXBlL1N0aWxsSW1hZ2UiPjwvdHlwZT4KICAgIDxkYXRlPjIwMjYtMDctMjRUMjA6MzQ6MDQuNzQ4NTE5PC9kYXRlPgogICAgPGZvcm1hdD5pbWFnZS9zdmcreG1sPC9mb3JtYXQ+CiAgICA8Y3JlYXRvcj4KICAgICA8YWdlbnQ+CiAgICAgIDx0aXRsZT5NYXRwbG90bGliIHYzLjExLjEsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvPC90aXRsZT4KICAgICA8L2FnZW50PgogICAgPC9jcmVhdG9yPgogICA8L3dvcms+CiAgPC9yZGY+CiA8L21ldGFkYXRhPgogPGRlZnM+CiAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4qe3N0cm9rZS1saW5lam9pbjogcm91bmQ7IHN0cm9rZS1saW5lY2FwOiBidXR0fTwvc3R5bGU+CiA8L2RlZnM+CiA8ZyBpZD0iZmlndXJlXzEiPgogIDxnIGlkPSJwYXRjaF8xIj4KICAgPHBhdGggZD0iTSAwIDIxLjYgCkwgMzYgMjEuNiAKTCAzNiAwIApMIDAgMCAKegoiIHN0eWxlPSJmaWxsOiAjZmZmZmZmIiAvPgogIDwvZz4KICA8ZyBpZD0iYXhlc18xIj4KICAgPGcgaWQ9Im1hdHBsb3RsaWIuYXhpc18xIj4KICAgIDxnIGlkPSJ4dGlja18xIj48L2c+CiAgICA8ZyBpZD0ieHRpY2tfMiI+PC9nPgogICAgPGcgaWQ9Inh0aWNrXzMiPjwvZz4KICAgIDxnIGlkPSJ4dGlja180Ij48L2c+CiAgICA8ZyBpZD0ieHRpY2tfNSI+PC9nPgogICAgPGcgaWQ9Inh0aWNrXzYiPjwvZz4KICAgIDxnIGlkPSJ4dGlja183Ij48L2c+CiAgICA8ZyBpZD0ieHRpY2tfOCI+PC9nPgogICAgPGcgaWQ9Inh0aWNrXzkiPjwvZz4KICAgPC9nPgogICA8ZyBpZD0ibWF0cGxvdGxpYi5heGlzXzIiPgogICAgPGcgaWQ9Inl0aWNrXzEiPjwvZz4KICAgIDxnIGlkPSJ5dGlja18yIj48L2c+CiAgICA8ZyBpZD0ieXRpY2tfMyI+PC9nPgogICAgPGcgaWQ9Inl0aWNrXzQiPjwvZz4KICAgIDxnIGlkPSJ5dGlja181Ij48L2c+CiAgICA8ZyBpZD0ieXRpY2tfNiI+PC9nPgogICAgPGcgaWQ9Inl0aWNrXzciPjwvZz4KICAgIDxnIGlkPSJ5dGlja184Ij48L2c+CiAgICA8ZyBpZD0ieXRpY2tfOSI+PC9nPgogICA8L2c+CiAgIDxnIGlkPSJQb2x5Q29sbGVjdGlvbl8xIj4KICAgIDxwYXRoIGQ9Ik0gMS42MzYzNjQgMTUuNzA5MDkxIApMIDEuNjM2MzY0IDUuODkwOTA5IApMIDM0LjM2MzYzNiA1Ljg5MDkwOSAKTCAzNC4zNjM2MzYgMTUuNzA5MDkxIAp6CiIgY2xpcC1wYXRoPSJ1cmwoI3AzMWRhZDc3YzM4KSIgc3R5bGU9ImZpbGw6ICMwMDgwMDAiIC8+CiAgIDwvZz4KICAgPGcgaWQ9IkxpbmVDb2xsZWN0aW9uXzEiPgogICAgPHBhdGggZD0iTSAxLjYzNjM2NCAyMS42IApMIDEuNjM2MzY0IC0wIAoiIGNsaXAtcGF0aD0idXJsKCNwMzFkYWQ3N2MzOCkiIHN0eWxlPSJmaWxsOiBub25lOyBzdHJva2U6ICMwMDAwMDA7IHN0cm9rZS13aWR0aDogMC44ODYyMjciIC8+CiAgIDwvZz4KICA8L2c+CiA8L2c+CiA8ZGVmcz4KICA8Y2xpcHBhdGggaWQ9InAzMWRhZDc3YzM4Ij4KICAgPHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjM2IiBoZWlnaHQ9IjIxLjYiIC8+CiAgPC9jbGlwcGF0aD4KIDwvZGVmcz4KPC9zdmc+" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Lion</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right"><div>
<img src="data:image/svg+xml;base64,PHN2ZyB4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgd2lkdGg9IjM2cHQiIGhlaWdodD0iMjEuNnB0IiB2aWV3Ym94PSIwIDAgMzYgMjEuNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiPgogPG1ldGFkYXRhPgogIDxyZGYgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICA8d29yaz4KICAgIDx0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3B1cmwub3JnL2RjL2RjbWl0eXBlL1N0aWxsSW1hZ2UiPjwvdHlwZT4KICAgIDxkYXRlPjIwMjYtMDctMjRUMjA6MzQ6MDQuODU4MTI3PC9kYXRlPgogICAgPGZvcm1hdD5pbWFnZS9zdmcreG1sPC9mb3JtYXQ+CiAgICA8Y3JlYXRvcj4KICAgICA8YWdlbnQ+CiAgICAgIDx0aXRsZT5NYXRwbG90bGliIHYzLjExLjEsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvPC90aXRsZT4KICAgICA8L2FnZW50PgogICAgPC9jcmVhdG9yPgogICA8L3dvcms+CiAgPC9yZGY+CiA8L21ldGFkYXRhPgogPGRlZnM+CiAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4qe3N0cm9rZS1saW5lam9pbjogcm91bmQ7IHN0cm9rZS1saW5lY2FwOiBidXR0fTwvc3R5bGU+CiA8L2RlZnM+CiA8ZyBpZD0iZmlndXJlXzEiPgogIDxnIGlkPSJwYXRjaF8xIj4KICAgPHBhdGggZD0iTSAwIDIxLjYgCkwgMzYgMjEuNiAKTCAzNiAwIApMIDAgMCAKegoiIHN0eWxlPSJmaWxsOiAjZmZmZmZmIiAvPgogIDwvZz4KICA8ZyBpZD0iYXhlc18xIj4KICAgPGcgaWQ9Im1hdHBsb3RsaWIuYXhpc18xIj4KICAgIDxnIGlkPSJ4dGlja18xIj48L2c+CiAgICA8ZyBpZD0ieHRpY2tfMiI+PC9nPgogICAgPGcgaWQ9Inh0aWNrXzMiPjwvZz4KICAgIDxnIGlkPSJ4dGlja180Ij48L2c+CiAgICA8ZyBpZD0ieHRpY2tfNSI+PC9nPgogICAgPGcgaWQ9Inh0aWNrXzYiPjwvZz4KICAgIDxnIGlkPSJ4dGlja183Ij48L2c+CiAgICA8ZyBpZD0ieHRpY2tfOCI+PC9nPgogICAgPGcgaWQ9Inh0aWNrXzkiPjwvZz4KICAgPC9nPgogICA8ZyBpZD0ibWF0cGxvdGxpYi5heGlzXzIiPgogICAgPGcgaWQ9Inl0aWNrXzEiPjwvZz4KICAgIDxnIGlkPSJ5dGlja18yIj48L2c+CiAgICA8ZyBpZD0ieXRpY2tfMyI+PC9nPgogICAgPGcgaWQ9Inl0aWNrXzQiPjwvZz4KICAgIDxnIGlkPSJ5dGlja181Ij48L2c+CiAgICA8ZyBpZD0ieXRpY2tfNiI+PC9nPgogICAgPGcgaWQ9Inl0aWNrXzciPjwvZz4KICAgIDxnIGlkPSJ5dGlja184Ij48L2c+CiAgICA8ZyBpZD0ieXRpY2tfOSI+PC9nPgogICA8L2c+CiAgIDxnIGlkPSJQb2x5Q29sbGVjdGlvbl8xIj4KICAgIDxwYXRoIGQ9Ik0gMS42MzYzNjQgMTUuNzA5MDkxIApMIDEuNjM2MzY0IDUuODkwOTA5IApMIDE4IDUuODkwOTA5IApMIDE4IDE1LjcwOTA5MSAKegoiIGNsaXAtcGF0aD0idXJsKCNwMThmZGFjZjI3MikiIHN0eWxlPSJmaWxsOiAjMDA4MDAwIiAvPgogICA8L2c+CiAgIDxnIGlkPSJMaW5lQ29sbGVjdGlvbl8xIj4KICAgIDxwYXRoIGQ9Ik0gMS42MzYzNjQgMjEuNiAKTCAxLjYzNjM2NCAtMCAKIiBjbGlwLXBhdGg9InVybCgjcDE4ZmRhY2YyNzIpIiBzdHlsZT0iZmlsbDogbm9uZTsgc3Ryb2tlOiAjMDAwMDAwOyBzdHJva2Utd2lkdGg6IDAuODg2MjI3IiAvPgogICA8L2c+CiAgPC9nPgogPC9nPgogPGRlZnM+CiAgPGNsaXBwYXRoIGlkPSJwMThmZGFjZjI3MiI+CiAgIDxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSIzNiIgaGVpZ2h0PSIyMS42IiAvPgogIDwvY2xpcHBhdGg+CiA8L2RlZnM+Cjwvc3ZnPg==" />
</div></td>
</tr>
</tbody>
</table>


Nice! But that was a sizable chunk of code just to create plots comprised of one bar each. If you're like me, you'll find it's not at all trivial to do, especially without experience using the plotting package.

However, this isn't the only graphic you might want to have on display - when you come across a use case that necessitates more detailed plots, a comprehensive plotting package like `plotnine` could very well be your best bet. Imagine we are passing in a list of tuples and want to generate a scatterplot, writing all of those as `svg.py` elements or direct HTML would be quite cumbersome.


# Conclusion

How you choose to add plots to Great Tables is up to you. In writing graphical plotting functions for [**gt-extras**](https://posit-dev.github.io/gt-extras/articles/intro.html), I've personally turned towards an HTML-only approach that I've felt comfortable with in other settings. With that said, I do believe converting table values to graphic output is a task best done with a little bit of help (whether it be `svg-py` or another plotting package will depend on how detailed your plots are).

The choice ultimately depends on your specific needs: simplicity and directness, versus abstraction and power. By understanding the trade-offs, you will be able to tailor your approach to the needs of your project.
