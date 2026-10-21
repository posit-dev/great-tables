# google_font()

Specify a font from the *Google Fonts* service.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_helpers.py#L365-L427)

``` python
google_font(name)
```

The [google_font()](../reference/google_font.md#great_tables.google_font) helper function can be used wherever a font name might be specified. There are two instances where this helper can be used:

1.  `opt_table_font(font=...)` (for setting a table font)
2.  `style.text(font=...)` (itself used in [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style))

## Parameters

`name: str`  
The name of the Google Font to use.

## Returns

`GoogleFont`  
A GoogleFont object, which contains the name of the font and methods for incorporating the font in HTML output tables.

## Examples

Let's use the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset to create a table of two columns and eight rows. We'll replace missing values with em dashes using [`sub_missing()`](../reference/GT.sub_missing.md#great_tables.GT.sub_missing). For text in the time column, we will use the font called `"IBM Plex Mono"` which is available from Google Fonts. This is defined inside the [google_font()](../reference/google_font.md#great_tables.google_font) call, itself within the [`style.text()`](../reference/style.text.md#great_tables.style.text) method that's applied to the `style=` parameter of [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style).

``` python
from great_tables import GT, exibble, style, loc, google_font

(
    GT(exibble[["char", "time"]])
    .sub_missing()
    .tab_style(
        style=style.text(font=google_font(name="IBM Plex Mono")),
        locations=loc.body(columns="time")
    )
)
```

| char       | time  |
|------------|-------|
| apricot    | 13:35 |
| banana     | 14:40 |
| coconut    | 15:45 |
| durian     | 16:50 |
| --          | 17:55 |
| fig        | --     |
| grapefruit | 19:10 |
| honeydew   | 20:20 |

We can use a subset of the [sp500](../reference/data.sp500.md#great_tables.data.sp500) dataset to create a small table. With [`fmt_currency()`](../reference/GT.fmt_currency.md#great_tables.GT.fmt_currency), we can display values as monetary values. Then, we'll set a larger font size for the table and opt to use the `"Merriweather"` font by calling [google_font()](../reference/google_font.md#great_tables.google_font) within [`opt_table_font()`](../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font). In cases where that font may not materialize, we include two font fallbacks: `"Cochin"` and the catchall `"Serif"` group.

``` python
from great_tables import GT, google_font
from great_tables.data import sp500

(
    GT(sp500.drop(columns=["volume", "adj_close"]).head(10))
    .fmt_currency(columns=["open", "high", "low", "close"])
    .tab_options(table_font_size="20px")
    .opt_table_font(font=[google_font(name="Merriweather"), "Cochin", "Serif"])
)
```

| date       | open       | high       | low        | close      |
|------------|------------|------------|------------|------------|
| 2015-12-31 | \$2,060.59 | \$2,062.54 | \$2,043.62 | \$2,043.94 |
| 2015-12-30 | \$2,077.34 | \$2,077.34 | \$2,061.97 | \$2,063.36 |
| 2015-12-29 | \$2,060.54 | \$2,081.56 | \$2,060.54 | \$2,078.36 |
| 2015-12-28 | \$2,057.77 | \$2,057.77 | \$2,044.20 | \$2,056.50 |
| 2015-12-24 | \$2,063.52 | \$2,067.36 | \$2,058.73 | \$2,060.99 |
| 2015-12-23 | \$2,042.20 | \$2,064.73 | \$2,042.20 | \$2,064.29 |
| 2015-12-22 | \$2,023.15 | \$2,042.74 | \$2,020.49 | \$2,038.97 |
| 2015-12-21 | \$2,010.27 | \$2,022.90 | \$2,005.93 | \$2,021.15 |
| 2015-12-18 | \$2,040.81 | \$2,040.81 | \$2,005.33 | \$2,005.55 |
| 2015-12-17 | \$2,073.76 | \$2,076.37 | \$2,041.66 | \$2,041.89 |
