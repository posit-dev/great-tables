# Great Tables `v0.12.0`: Google Fonts and zebra stripes

In Great Tables `0.12.0` we focused on adding options for customizing the appearance of a table. In this post, we'll present two new features:

- using typefaces from Google Fonts via [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) and [opt_table_font()](../../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font)
- adding table striping via [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options) and [opt_row_striping()](../../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping)

Let's have a look at how these new features can be used!


## Using fonts from Google Fonts

Google Fonts is a free service that allows use of hosted typefaces in your own websites. In Great Tables, we added the [google_font()](../../reference/google_font.md#great_tables.google_font) helper function to easily incorporate such fonts in your tables. There are two ways to go about this:

1.  use [google_font()](../../reference/google_font.md#great_tables.google_font) with [opt_table_font()](../../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font) to set a Google Font for the entire table
2.  invoke [google_font()](../../reference/google_font.md#great_tables.google_font) within `tab_style(styles=style.text(font=...))` to set the font within a location

Let's start with this small table that uses the default set of fonts for the entire table.


Show the code

``` python
from great_tables import GT, exibble, style, loc

gt_tbl = (
    GT(exibble.head(), rowname_col="row", groupname_col="group")
    .cols_hide(columns=["char", "fctr", "date", "time"])
    .tab_header(
        title="A small piece of the exibble dataset",
        subtitle="Displaying the first five rows (of eight)",
    )
    .tab_source_note(
        source_note="This dataset is included in Great Tables."
    )
)

gt_tbl
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>

</table>


Now, with [opt_table_font()](../../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font) + [google_font()](../../reference/google_font.md#great_tables.google_font), we'll change the table's font to one from Google Fonts. I like [`Noto Serif`](https://fonts.google.com/noto/specimen/Noto+Serif) so let's use that here!


``` python
from great_tables import GT, exibble, style, loc, google_font

(
    gt_tbl
    .opt_table_font(font=google_font(name="Noto Serif"))
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>

</table>


Looking good! And we don't have to apply the font to the entire table. We might just wanted to use a Google Font in the table body. For that use case, [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) is the preferred method. Here's an example that uses the [`IBM Plex Mono`](https://fonts.google.com/specimen/IBM+Plex+Mono) typeface.


``` python
(
    gt_tbl
    .tab_style(
        style=style.text(font=google_font(name="IBM Plex Mono")),
        locations=loc.body()
    )
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">0.1111</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-01-01 02:22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2.222</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-02-02 14:33</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">33.33</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-03-03 03:44</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">444.4</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-04-04 15:55</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">5550.0</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-05-05 04:00</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">1325.81</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>

</table>


Nice! And it's refreshing to see tables with fonts different from default set, as good as it might be. We kept the [google_font()](../../reference/google_font.md#great_tables.google_font) helper function as simple as possible, requiring only the font name in its `name=` argument. There are hundreds of fonts hosted on [Google Fonts](https://fonts.google.com) so look through the site, experiment, and find the fonts that you think look best in your tables!


## Striping rows in your table

Some people like having row striping (a.k.a. zebra stripes) in their display tables. We also know that some [advise against the practice](https://www.darkhorseanalytics.com/blog/clear-off-the-table/). We understand it's a controversial table issue, however, we also want to give you the creative freedom to just include the stripes. To that end, we now have that option in the package. There are two ways to enable this look:

1.  invoking [opt_row_striping()](../../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping) to quickly set row stripes in the table body
2.  using some combination of three `row_striping_*` arguments in [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options)

Let's use that example table with [opt_row_striping()](../../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping).


``` python
gt_tbl.opt_row_striping()
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.222</td>
<td class="gt_row gt_right gt_striped">2018-02-02 14:33</td>
<td class="gt_row gt_right gt_striped">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.4</td>
<td class="gt_row gt_right gt_striped">2018-04-04 15:55</td>
<td class="gt_row gt_right gt_striped">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>

</table>


It's somewhat subtle but there is an alternating, slightly gray background (starting on the `"row_2"` row). The color is `#808080` but with an alpha (transparency) value of `0.05`.

If this is not exactly what you want, there is an alternative to this. The [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options) method has three new arguments:

- `row_striping_background_color`: color to use for row striping
- `row_striping_include_stub`: should striping include cells in the stub?
- `row_striping_include_table_body`: should striping include cells in the body?

With these new options, we can choose to stripe the *entire* row (stub cells + body cells) and use a darker color like `"lightblue"`.


``` python
(
    gt_tbl
    .tab_options(
        row_striping_background_color="lightblue",
        row_striping_include_stub=True,
        row_striping_include_table_body=True,
    )
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_striped">row_2</td>
<td class="gt_row gt_right gt_striped">2.222</td>
<td class="gt_row gt_right gt_striped">2018-02-02 14:33</td>
<td class="gt_row gt_right gt_striped">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_striped">row_4</td>
<td class="gt_row gt_right gt_striped">444.4</td>
<td class="gt_row gt_right gt_striped">2018-04-04 15:55</td>
<td class="gt_row gt_right gt_striped">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>

</table>


These alternating fills can be a good idea in some table display circumstances. Now, you can make that call and the functionality is there to support your decision.


## Wrapping up

We are excited that this new functionality is now available in Great Tables. As ever, please let us know through [GitHub Issues](https://github.com/posit-dev/great-tables/issues) whether you ran into problems with any feature (new or old), or, if you have suggestions for further improvement!
