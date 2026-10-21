# Great Tables `v0.12.0`: Google Fonts and zebra stripes

In Great Tables `0.12.0` we focused on adding options for customizing the appearance of a table. In this post, we'll present two new features:

- using typefaces from Google Fonts via [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) and [opt_table_font()](../../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font)
- adding table striping via [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options) and [opt_row_striping()](../../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping)

Let's have a look at how these new features can be used!

### Using fonts from Google Fonts

Google Fonts is a free service that allows use of hosted typefaces in your own websites. In Great Tables, we added the [google_font()](../../reference/google_font.md#great_tables.google_font) helper function to easily incorporate such fonts in your tables. There are two ways to go about this:

1.  use [google_font()](../../reference/google_font.md#great_tables.google_font) with [opt_table_font()](../../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font) to set a Google Font for the entire table
2.  invoke [google_font()](../../reference/google_font.md#great_tables.google_font) within `tab_style(styles=style.text(font=...))` to set the font within a location

Let's start with this small table that uses the default set of fonts for the entire table.

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

| A small piece of the exibble dataset      |        |                  |          |
|-------------------------------------------|--------|------------------|----------|
| Displaying the first five rows (of eight) |        |                  |          |
|                                           | num    | datetime         | currency |
| grp_a                                     |        |                  |          |
| row_1                                     | 0.1111 | 2018-01-01 02:22 | 49.95    |
| row_2                                     | 2.222  | 2018-02-02 14:33 | 17.95    |
| row_3                                     | 33.33  | 2018-03-03 03:44 | 1.39     |
| row_4                                     | 444.4  | 2018-04-04 15:55 | 65100.0  |
| grp_b                                     |        |                  |          |
| row_5                                     | 5550.0 | 2018-05-05 04:00 | 1325.81  |
| This dataset is included in Great Tables. |        |                  |          |

Now, with [opt_table_font()](../../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font) + [google_font()](../../reference/google_font.md#great_tables.google_font), we'll change the table's font to one from Google Fonts. I like [`Noto Serif`](https://fonts.google.com/noto/specimen/Noto+Serif) so let's use that here!

``` python
from great_tables import GT, exibble, style, loc, google_font

(
    gt_tbl
    .opt_table_font(font=google_font(name="Noto Serif"))
)
```

| A small piece of the exibble dataset      |        |                  |          |
|-------------------------------------------|--------|------------------|----------|
| Displaying the first five rows (of eight) |        |                  |          |
|                                           | num    | datetime         | currency |
| grp_a                                     |        |                  |          |
| row_1                                     | 0.1111 | 2018-01-01 02:22 | 49.95    |
| row_2                                     | 2.222  | 2018-02-02 14:33 | 17.95    |
| row_3                                     | 33.33  | 2018-03-03 03:44 | 1.39     |
| row_4                                     | 444.4  | 2018-04-04 15:55 | 65100.0  |
| grp_b                                     |        |                  |          |
| row_5                                     | 5550.0 | 2018-05-05 04:00 | 1325.81  |
| This dataset is included in Great Tables. |        |                  |          |

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

| A small piece of the exibble dataset      |        |                  |          |
|-------------------------------------------|--------|------------------|----------|
| Displaying the first five rows (of eight) |        |                  |          |
|                                           | num    | datetime         | currency |
| grp_a                                     |        |                  |          |
| row_1                                     | 0.1111 | 2018-01-01 02:22 | 49.95    |
| row_2                                     | 2.222  | 2018-02-02 14:33 | 17.95    |
| row_3                                     | 33.33  | 2018-03-03 03:44 | 1.39     |
| row_4                                     | 444.4  | 2018-04-04 15:55 | 65100.0  |
| grp_b                                     |        |                  |          |
| row_5                                     | 5550.0 | 2018-05-05 04:00 | 1325.81  |
| This dataset is included in Great Tables. |        |                  |          |

Nice! And it's refreshing to see tables with fonts different from default set, as good as it might be. We kept the [google_font()](../../reference/google_font.md#great_tables.google_font) helper function as simple as possible, requiring only the font name in its `name=` argument. There are hundreds of fonts hosted on [Google Fonts](https://fonts.google.com) so look through the site, experiment, and find the fonts that you think look best in your tables!

### Striping rows in your table

Some people like having row striping (a.k.a. zebra stripes) in their display tables. We also know that some [advise against the practice](https://www.darkhorseanalytics.com/blog/clear-off-the-table/). We understand it's a controversial table issue, however, we also want to give you the creative freedom to just include the stripes. To that end, we now have that option in the package. There are two ways to enable this look:

1.  invoking [opt_row_striping()](../../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping) to quickly set row stripes in the table body
2.  using some combination of three `row_striping_*` arguments in [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options)

Let's use that example table with [opt_row_striping()](../../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping).

``` python
gt_tbl.opt_row_striping()
```

| A small piece of the exibble dataset      |        |                  |          |
|-------------------------------------------|--------|------------------|----------|
| Displaying the first five rows (of eight) |        |                  |          |
|                                           | num    | datetime         | currency |
| grp_a                                     |        |                  |          |
| row_1                                     | 0.1111 | 2018-01-01 02:22 | 49.95    |
| row_2                                     | 2.222  | 2018-02-02 14:33 | 17.95    |
| row_3                                     | 33.33  | 2018-03-03 03:44 | 1.39     |
| row_4                                     | 444.4  | 2018-04-04 15:55 | 65100.0  |
| grp_b                                     |        |                  |          |
| row_5                                     | 5550.0 | 2018-05-05 04:00 | 1325.81  |
| This dataset is included in Great Tables. |        |                  |          |

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

| A small piece of the exibble dataset      |        |                  |          |
|-------------------------------------------|--------|------------------|----------|
| Displaying the first five rows (of eight) |        |                  |          |
|                                           | num    | datetime         | currency |
| grp_a                                     |        |                  |          |
| row_1                                     | 0.1111 | 2018-01-01 02:22 | 49.95    |
| row_2                                     | 2.222  | 2018-02-02 14:33 | 17.95    |
| row_3                                     | 33.33  | 2018-03-03 03:44 | 1.39     |
| row_4                                     | 444.4  | 2018-04-04 15:55 | 65100.0  |
| grp_b                                     |        |                  |          |
| row_5                                     | 5550.0 | 2018-05-05 04:00 | 1325.81  |
| This dataset is included in Great Tables. |        |                  |          |

These alternating fills can be a good idea in some table display circumstances. Now, you can make that call and the functionality is there to support your decision.

### Wrapping up

We are excited that this new functionality is now available in Great Tables. As ever, please let us know through [GitHub Issues](https://github.com/posit-dev/great-tables/issues) whether you ran into problems with any feature (new or old), or, if you have suggestions for further improvement!
