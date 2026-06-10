## GT.tab_footnote()


Add a table footnote.


Usage

``` python
GT.tab_footnote(
    footnote,
    locations=None,
    placement="auto",
)
```


[tab_footnote()](GT.tab_footnote.md#great_tables.GT.tab_footnote) can make it a painless process to add a footnote to a table. There are commonly two components to a footnote: (1) a footnote mark that is attached to the targeted cell content, and (2) the footnote text itself that is placed in the table's footer area. Each unit of footnote text in the footer is linked to an element of text or otherwise through the footnote mark.

The footnote system in **Great Tables** presents footnotes in a way that matches the usual expectations, where:

1.  footnote marks have a sequence, whether they are symbols, numbers, or letters
2.  multiple footnotes can be applied to the same content (and marks are always presented in an ordered fashion)
3.  footnote text in the footer is never exactly repeated, **Great Tables** reuses footnote marks where needed throughout the table
4.  footnote marks are ordered across the table in a consistent manner (left to right, top to bottom)

Each call of [tab_footnote()](GT.tab_footnote.md#great_tables.GT.tab_footnote) will either add a different footnote to the footer or reuse existing footnote text therein. One or more cells outside of the footer are targeted using location classes from the `loc` module (e.g., [loc.body()](loc.body.md#great_tables.loc.body), [loc.column_labels()](loc.column_labels.md#great_tables.loc.column_labels), etc.). You can choose to *not* attach a footnote mark by simply not specifying anything in the `locations` argument.

By default, **Great Tables** will choose which side of the text to place the footnote mark via the `placement="auto"` option. You are, however, always free to choose the placement of the footnote mark (either to the `"left"` or `"right"` of the targeted cell content).


## Parameters


`footnote: str | Text`  
The text to be used in the footnote. We can optionally use <a href="md.html#great_tables.md" class="gdls-link"><code>md()</code></a> or <a href="html.html#great_tables.html" class="gdls-link"><code>html()</code></a> to style the text as Markdown or to retain HTML elements in the footnote text.

`locations: Loc | None | list[Loc | None] = None`  
The cell or set of cells to be associated with the footnote. Supplying any of the location classes from the `loc` module is a useful way to target the location cells that are associated with the footnote text. These location classes are: [loc.title](loc.title.md#great_tables.loc.title), [loc.stubhead](loc.stubhead.md#great_tables.loc.stubhead), [loc.spanner_labels](loc.spanner_labels.md#great_tables.loc.spanner_labels), [loc.column_labels](loc.column_labels.md#great_tables.loc.column_labels), [loc.row_groups](loc.row_groups.md#great_tables.loc.row_groups), [loc.stub](loc.stub.md#great_tables.loc.stub), [loc.body](loc.body.md#great_tables.loc.body), etc. Additionally, we can enclose several location calls within a `list()` if we wish to link the footnote text to different types of locations (e.g., body cells, row group labels, the table title, etc.).

`placement: PlacementOptions = ``"auto"`  
Where to affix footnote marks to the table content. Two options for this are `"left"` or `"right"`, where the placement is either to the absolute left or right of the cell content. By default, however, this option is set to `"auto"` whereby **Great Tables** will choose a preferred left-or-right placement depending on the alignment of the cell content.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

This example table will be based on the [towny](data.towny.md#great_tables.data.towny) dataset. We have a header part, with a title and a subtitle. We can choose which of these could be associated with a footnote and in this case it is the `"subtitle"`. This table has a stub with row labels and some of those labels are associated with a footnote. So long as row labels are unique, they can be easily used as row identifiers in [loc.stub()](loc.stub.md#great_tables.loc.stub). The third footnote is placed on the `"Density"` column label. Here, changing the order of the [tab_footnote()](GT.tab_footnote.md#great_tables.GT.tab_footnote) calls has no effect on the final table rendering.


``` python
import polars as pl
from great_tables import GT, loc, md
from great_tables.data import towny

towny_mini = (
    pl.from_pandas(towny)
    .filter(pl.col("csd_type") == "city")
    .select(["name", "density_2021", "population_2021"])
    .top_k(10, by="population_2021")
    .sort("population_2021", descending=True)
)

(
    GT(towny_mini, rowname_col="name")
    .tab_header(
        title=md("The 10 Largest Municipalities in `towny`"),
        subtitle="Population values taken from the 2021 census."
    )
    .fmt_integer()
    .cols_label(
        density_2021="Density",
        population_2021="Population"
    )
    .tab_footnote(
        footnote="Part of the Greater Toronto Area.",
        locations=loc.stub(rows=[
            "Toronto", "Mississauga", "Brampton", "Markham", "Vaughan"
        ])
    )
    .tab_footnote(
        footnote=md("Density is in terms of persons per {{km^2}}."),
        locations=loc.column_labels(columns="density_2021")
    )
    .tab_footnote(
        footnote="Census results made public on February 9, 2022.",
        locations=loc.subtitle()
    )
    .tab_source_note(
        source_note=md("Data taken from the `towny` dataset.")
    )
    .opt_footnote_marks(marks="letters")
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">The 10 Largest Municipalities in [towny](data.towny.md#great_tables.data.towny)</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Population values taken from the 2021 census.<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">a</span></th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="density_2021" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Density<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">b</span></th>
<th id="population_2021" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Population</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">Toronto<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">c</span></th>
<td class="gt_row gt_right">4,428</td>
<td class="gt_row gt_right">2,794,356</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Ottawa</th>
<td class="gt_row gt_right">365</td>
<td class="gt_row gt_right">1,017,449</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Mississauga<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">c</span></th>
<td class="gt_row gt_right">2,453</td>
<td class="gt_row gt_right">717,961</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Brampton<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">c</span></th>
<td class="gt_row gt_right">2,469</td>
<td class="gt_row gt_right">656,480</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Hamilton</th>
<td class="gt_row gt_right">509</td>
<td class="gt_row gt_right">569,353</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">London</th>
<td class="gt_row gt_right">1,004</td>
<td class="gt_row gt_right">422,324</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Markham<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">c</span></th>
<td class="gt_row gt_right">1,605</td>
<td class="gt_row gt_right">338,503</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Vaughan<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">c</span></th>
<td class="gt_row gt_right">1,186</td>
<td class="gt_row gt_right">323,103</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Kitchener</th>
<td class="gt_row gt_right">1,878</td>
<td class="gt_row gt_right">256,885</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Windsor</th>
<td class="gt_row gt_right">1,573</td>
<td class="gt_row gt_right">229,660</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">Data taken from the [towny](data.towny.md#great_tables.data.towny) dataset.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="3" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">a</span> Census results made public on February 9, 2022.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="3" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">b</span> Density is in terms of persons per km<span style="white-space:nowrap;"><sup>2</sup>.</span></td>
</tr>
<tr class="gt_footnotes">
<td colspan="3" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">c</span> Part of the Greater Toronto Area.</td>
</tr>
</tfoot>

</table>
