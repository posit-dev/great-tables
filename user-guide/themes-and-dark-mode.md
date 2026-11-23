# Themes and Dark Mode

A table follows the light or dark look of the page it is shown in, with no code from you. When you want to change more than that, a [Theme](../reference/Theme.md#great_tables.Theme) is a reusable set of colors, fonts, and [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) values that you apply to one table with [opt_theme()](../reference/GT.opt_theme.md#great_tables.GT.opt_theme). This page covers the automatic light and dark behavior, how to write a theme, which value wins when several apply, the CSS variables that make this work in HTML, and how to build a theme from a [brand.yml](https://posit-dev.github.io/brand-yml/) file.

The examples use a small piece of [exibble](../reference/data.exibble.md#great_tables.data.exibble).

``` python
from great_tables import GT, Theme, data

small = data.pl.exibble.select("num", "char", "currency", "row")

gt_small = GT(small, rowname_col="row").tab_header("A small table")
```

## Automatic Light and Dark

By default a table is in `"auto"` mode. It is light, and it turns dark when the page around it is dark. It reads that from two places:

- The page's own theme, when the page is one of these hosts: JupyterLab and Notebook 7, VS Code notebooks, Quarto, marimo, or a page using Bootstrap 5.3's `data-bs-theme` attribute. A host that says it is light keeps the table light, whatever the operating system prefers.
- The reader's operating system or browser preference (`prefers-color-scheme`), when the page does not say.

You do not need to do anything for this. The table below is a default table, so it changes with the page it is shown in.

``` python
gt_small
```

| A small table |           |            |          |
|---------------|-----------|------------|----------|
|               | num       | char       | currency |
| row_1         | 0.1111    | apricot    | 49.95    |
| row_2         | 2.222     | banana     | 17.95    |
| row_3         | 33.33     | coconut    | 1.39     |
| row_4         | 444.4     | durian     | 65100.0  |
| row_5         | 5550.0    | None       | 1325.81  |
| row_6         | None      | fig        | 13.255   |
| row_7         | 777000.0  | grapefruit | None     |
| row_8         | 8880000.0 | honeydew   | 0.44     |

[opt_theme()](../reference/GT.opt_theme.md#great_tables.GT.opt_theme) takes a `mode=` to pin the table instead:

- `"light"`: always the light colors.
- `"dark"`: always the dark colors.
- `"auto"`: the default.

``` python
gt_small.opt_theme(mode="dark")
```

| A small table |           |            |          |
|---------------|-----------|------------|----------|
|               | num       | char       | currency |
| row_1         | 0.1111    | apricot    | 49.95    |
| row_2         | 2.222     | banana     | 17.95    |
| row_3         | 33.33     | coconut    | 1.39     |
| row_4         | 444.4     | durian     | 65100.0  |
| row_5         | 5550.0    | None       | 1325.81  |
| row_6         | None      | fig        | 13.255   |
| row_7         | 777000.0  | grapefruit | None     |
| row_8         | 8880000.0 | honeydew   | 0.44     |

``` python
gt_small.opt_theme(mode="light")
```

| A small table |           |            |          |
|---------------|-----------|------------|----------|
|               | num       | char       | currency |
| row_1         | 0.1111    | apricot    | 49.95    |
| row_2         | 2.222     | banana     | 17.95    |
| row_3         | 33.33     | coconut    | 1.39     |
| row_4         | 444.4     | durian     | 65100.0  |
| row_5         | 5550.0    | None       | 1325.81  |
| row_6         | None      | fig        | 13.255   |
| row_7         | 777000.0  | grapefruit | None     |
| row_8         | 8880000.0 | honeydew   | 0.44     |

Use `mode="light"` when your table sits on a page with no dark theme of its own. Such a page shown to a reader whose system prefers dark would otherwise get a dark table on a light page.

A table with a background color set through [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) or [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize) stays light in `"auto"` mode. Those colors were picked for a light table, and they apply in both modes, so switching would give pale stripes on a dark table. `mode="dark"` still forces dark. A background set in a [Theme](../reference/Theme.md#great_tables.Theme) does not pin the table, because a theme can carry its own dark colors.

## Writing a Theme

A [Theme](../reference/Theme.md#great_tables.Theme) holds values for a few tokens, plus any option that [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) accepts. Give only what you want to change. Everything else keeps its built-in value.

| Argument | CSS variable | What it sets |
|----|----|----|
| `background` | `--gt-color-background` | The table background. Sections without a color of their own use it. |
| `foreground` | `--gt-color-foreground` | The text color on that background. |
| `border` | `--gt-color-border` | The lines and borders that are light gray (`#D3D3D3`) by default. |
| `border_strong` | `--gt-color-border-strong` | The top and bottom table borders. |
| `stripe` | `--gt-color-stripe` | The background of striped rows. |
| `accent` | `--gt-color-accent` | For your own CSS. Interactive tables' controls get it as `--gt-i-accent`. |
| `font` | `--gt-font-family` | The font, one name or a list. It goes ahead of the default font stack. |
| `font_size` | `--gt-font-size` | The base font size, as a CSS length or a number of pixels. |

Any other argument is the name of a [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) option, checked the same way. An unknown name raises an error.

A theme that sets `background` but not `foreground` keeps the built-in text colors, and the table picks the light or the dark one for that background, as it does for `~~GT.tab_options(table_background_color=...)`.

``` python
compact = Theme(
    border="#9AA5B1",
    font="Georgia",
    data_row_padding="3px",
    column_labels_font_weight="bold",
)

gt_small.opt_theme(compact)
```

| A small table |           |            |          |
|---------------|-----------|------------|----------|
|               | num       | char       | currency |
| row_1         | 0.1111    | apricot    | 49.95    |
| row_2         | 2.222     | banana     | 17.95    |
| row_3         | 33.33     | coconut    | 1.39     |
| row_4         | 444.4     | durian     | 65100.0  |
| row_5         | 5550.0    | None       | 1325.81  |
| row_6         | None      | fig        | 13.255   |
| row_7         | 777000.0  | grapefruit | None     |
| row_8         | 8880000.0 | honeydew   | 0.44     |

There are no tokens for spacing, since the default padding differs by table part. Set the padding options (`data_row_padding`, `column_labels_padding`, and so on) in the theme instead.

### Colors for dark mode

`dark=` takes a second [Theme](../reference/Theme.md#great_tables.Theme) with the values to use in dark mode. It can hold the five color tokens (`background`, `foreground`, `border`, `border_strong`, `stripe`) and options that are written to the table's stylesheet, such as `table_body_hlines_color`. Anything else raises an error, because it cannot vary by mode in CSS. A `dark` theme cannot have its own `dark=`.

``` python
navy = Theme(
    border="#9AA5B1",
    font="Georgia",
    dark=Theme(background="#101418", border="#2A3038"),
)

gt_small.opt_theme(navy)
```

| A small table |           |            |          |
|---------------|-----------|------------|----------|
|               | num       | char       | currency |
| row_1         | 0.1111    | apricot    | 49.95    |
| row_2         | 2.222     | banana     | 17.95    |
| row_3         | 33.33     | coconut    | 1.39     |
| row_4         | 444.4     | durian     | 65100.0  |
| row_5         | 5550.0    | None       | 1325.81  |
| row_6         | None      | fig        | 13.255   |
| row_7         | 777000.0  | grapefruit | None     |
| row_8         | 8880000.0 | honeydew   | 0.44     |

The built-in dark theme supplies a background, text, border, strong border, and stripe color. A theme's light color tokens are not used in dark mode. A theme that sets `background` and has no `dark=` still goes dark with the built-in dark background, and `mode="light"` keeps it light. Spacing, fonts, the accent, and any color option the theme sets directly carry over to dark mode unless `dark=` replaces them.

## What Wins

When several things set the same option, the first of these that exists is used:

1.  A value set with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) or an `opt_*()` method. It applies in both modes.
2.  In dark mode, the option in the theme's `dark=`.
3.  The option in the theme.
4.  In dark mode, for an option fed by a color token: the token in the theme's `dark=`, then the built-in dark token.
5.  The token in the theme.
6.  The built-in value.

Setting an option to its default value with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) still counts as setting it.

Values from [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) and the `opt_*()` methods are absolute. They are not scaled from the theme. [opt_vertical_padding()](../reference/GT.opt_vertical_padding.md#great_tables.GT.opt_vertical_padding), [opt_horizontal_padding()](../reference/GT.opt_horizontal_padding.md#great_tables.GT.opt_horizontal_padding), and [opt_table_font()](../reference/GT.opt_table_font.md#great_tables.GT.opt_table_font) with `add=True` compute from the built-in values, and what they compute then replaces the theme's value. Below, the theme asks for `3px` of padding, and the `scale=2` in [opt_vertical_padding()](../reference/GT.opt_vertical_padding.md#great_tables.GT.opt_vertical_padding) doubles the built-in `8px`, so the rows get `16px`.

``` python
gt_small.opt_theme(Theme(data_row_padding="3px")).opt_vertical_padding(scale=2)
```

| A small table |           |            |          |
|---------------|-----------|------------|----------|
|               | num       | char       | currency |
| row_1         | 0.1111    | apricot    | 49.95    |
| row_2         | 2.222     | banana     | 17.95    |
| row_3         | 33.33     | coconut    | 1.39     |
| row_4         | 444.4     | durian     | 65100.0  |
| row_5         | 5550.0    | None       | 1325.81  |
| row_6         | None      | fig        | 13.255   |
| row_7         | 777000.0  | grapefruit | None     |
| row_8         | 8880000.0 | honeydew   | 0.44     |

The order of the calls does not matter. A theme is stored apart from the table's options, so [opt_theme()](../reference/GT.opt_theme.md#great_tables.GT.opt_theme) before or after [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) gives the same table.

## CSS Variables

In HTML, every option that is written to the table's stylesheet is a CSS variable on that table. The name is `--gt-` followed by the option name, with underscores turned into hyphens: `data_row_padding` is `--gt-data-row-padding`, and `table_body_hlines_color` is `--gt-table-body-hlines-color`. The tokens use the names in the table above. These options are not part of the stylesheet and have no variable: the footnote marks, order, and spec (`footnotes_marks`, `footnotes_order`, `footnotes_spec_ref`, `footnotes_spec_ftr`); the source note separator and multiline setting (`source_notes_sep`, `source_notes_multiline`); the container options (`container_width`, `container_height`, `container_padding_x`, `container_padding_y`, `container_overflow_x`, `container_overflow_y`); the Quarto options (`quarto_disable_processing`, `quarto_use_bootstrap`); the options that say whether a part is included or shown (`table_border_top_include`, `table_border_bottom_include`, `row_striping_include_stub`, `row_striping_include_table_body`, `column_labels_hidden`, `row_group_as_column`); `table_id`, `table_caption`, and `table_additional_css`; and the `ihtml_*` options. `table_font_names` has no variable of its own: it is written through `--gt-font-family`.

`--gt-color-accent` is not read by any CSS. A static table has no accent, and an interactive table reads `--gt-i-accent`: a theme's `accent` is written to that variable on the interactive table's element, and page CSS can set `--gt-i-accent` itself.

A table declares a variable only for a value that was set from Python. Every other value is a fallback in the CSS, so page CSS can set the variables on a parent of the table, and this works for anything the Python code left alone. The page below sets a border color and tighter padding on every table inside `.tight`.

``` python
gt_small
```

| A small table |           |            |          |
|---------------|-----------|------------|----------|
|               | num       | char       | currency |
| row_1         | 0.1111    | apricot    | 49.95    |
| row_2         | 2.222     | banana     | 17.95    |
| row_3         | 33.33     | coconut    | 1.39     |
| row_4         | 444.4     | durian     | 65100.0  |
| row_5         | 5550.0    | None       | 1325.81  |
| row_6         | None      | fig        | 13.255   |
| row_7         | 777000.0  | grapefruit | None     |
| row_8         | 8880000.0 | honeydew   | 0.44     |

A value set from Python wins over the page's CSS, because the table declares it on its own element. In the next table `data_row_padding` is set in Python, so the `2px` from the page CSS is not used, while the border color from the page still is.

``` python
gt_small.tab_options(data_row_padding="10px")
```

| A small table |           |            |          |
|---------------|-----------|------------|----------|
|               | num       | char       | currency |
| row_1         | 0.1111    | apricot    | 49.95    |
| row_2         | 2.222     | banana     | 17.95    |
| row_3         | 33.33     | coconut    | 1.39     |
| row_4         | 444.4     | durian     | 65100.0  |
| row_5         | 5550.0    | None       | 1325.81  |
| row_6         | None      | fig        | 13.255   |
| row_7         | 777000.0  | grapefruit | None     |
| row_8         | 8880000.0 | honeydew   | 0.44     |

The same holds for a theme: its values count as set from Python. A table cannot be restyled from page CSS for any value its theme sets.

Custom properties are inherited. A table placed inside another table (for example, one pasted into a cell as raw HTML) reads the variables that Python set on the outer table. The row details of interactive tables are the exception: the outer table's variables are reset around them. That reset also blocks page CSS, so a variable that the outer table sets does not reach a table in its row details from the page either.

## brand.yml

If your organization describes its colors and fonts in a brand.yml file, [Theme.from_brand()](../reference/Theme.md#great_tables.Theme.from_brand) turns it into a [Theme](../reference/Theme.md#great_tables.Theme). This needs the [brand_yml](https://pypi.org/project/brand-yml/) package, which is installed with `pip install great_tables[brand]`. Without it, [Theme.from_brand()](../reference/Theme.md#great_tables.Theme.from_brand) raises an `ImportError` that names the extra.

Take this `_brand.yml`.

``` yaml
color:
  palette:
    navy: "#001F3F"
  background: "#FDF6E3"
  foreground: "#073642"
  primary: navy
typography:
  fonts:
    - family: Inter
      source: system
  base:
    family: Inter
    size: 14px
```

Pass its path to [Theme.from_brand()](../reference/Theme.md#great_tables.Theme.from_brand) and apply the result like any other theme.

``` python
from great_tables import GT, Theme, data

theme = Theme.from_brand("_brand.yml")

GT(data.pl.exibble).opt_theme(theme)
```

These fields are used:

| brand.yml field | [Theme](../reference/Theme.md#great_tables.Theme) argument |
|----|----|
| `color.background` | `background` |
| `color.foreground` | `foreground` |
| `color.primary` | `accent` |
| `typography.base.family` | `font` |
| `typography.base.size` | `font_size` |

A color that names an entry of `color.palette` becomes that entry's color. A field the file does not have is left out of the theme. The `border`, `border_strong`, and `stripe` tokens are not taken from the brand, so they keep their built-in values. Font files and Google Font imports are not loaded; only the family name is used.

A brand.yml file has one set of colors. For dark mode, pass a second file with `dark=`. Only its `background` and `foreground` are used, as the colors of the theme's `dark=`.

``` python
theme = Theme.from_brand("_brand.yml", dark="_brand-dark.yml")
```

Each argument can also be a `brand_yml.Brand` object. With no argument, [Theme.from_brand()](../reference/Theme.md#great_tables.Theme.from_brand) leaves the search for a file to `brand_yml`. In `brand_yml` 0.2.0 that needs the `BRAND_YML_PATH` environment variable to be set, so pass a path when you can.

## Limits

- **Colors you set on cells are not themed.** Literal colors from [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style), [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color), and [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize) are written as you gave them, in both modes. A few cases are adjusted so the text stays readable:
  - A cell with a fill and no text color gets a text color chosen for contrast with the fill. In light mode this changes cells whose fill is dark or mid-tone (red, blue, or green, for example), not only dark fills. A text color you write with [style.css()](../reference/style.css.md#great_tables.style.css) still wins.
  - A text color on a cell with no fill is blended toward the section's text color in dark mode, and is left as written in light mode.
  - A cell with both a fill and a text color is left as written, and so is a fill from [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) with its defaults.
  - A fill that is translucent or a keyword (`transparent`, `inherit`, and so on) is left alone.
  - `~~GT.data_color(autocolor_text=False)` fills get no contrast text, so in dark mode they show the table's light text.
- **Forced dark can lower contrast.** In `mode="dark"`, text on a mid-tone fill that you set (the header of an [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize) table, for example) uses the dark theme's text color. It can have lower contrast than in light mode.
- **Content in a cell keeps its own colors.** Plots from extension packages, raw HTML or SVG, and images inside a cell are not adapted to dark mode.
- **[as_raw_html()](../reference/GT.as_raw_html.md#great_tables.GT.as_raw_html) needs CSS custom properties.** Its output only renders as intended where the renderer supports them. `as_raw_html(inline_css=True)` writes literal styles instead, for one mode.
- **Some output has one mode.** Email HTML (`inline_css=True`), images, LaTeX, Word, and Typst output cannot follow a preference. In email HTML, `"auto"` gives the light table and `"dark"` the dark one. Output made through gridwell (`as_gridwell()`, and [gtsave()](../reference/GT.gtsave.md#great_tables.GT.gtsave) to formats such as SVG or Word) and LaTeX ignores the mode and is light, even with `mode="dark"`; the theme values those outputs can express, such as border colors, still apply.
- **Quarto renders use literal styles unless the format is HTML.** HTML shown in a Quarto render is written the same way as email HTML when the format is not HTML, and for any format when Quarto does not report it (older Quarto versions).
- **Iframes and shadow roots follow the system preference only.** The page's theme cannot be seen from inside them, so a table there goes by `prefers-color-scheme`.
- **A page with no dark theme of its own can show a dark table.** If a reader's system prefers dark and the page is not one of the recognized hosts in light mode, the default table is dark on a light page. Pin it with `mode="light"`.
- **Other pages follow the system setting.** A standalone page from [show()](../reference/GT.show.md#great_tables.GT.show), Colab, and Databricks give no theme signal. Sites built with Sphinx or MkDocs may have a dark theme of their own, but the table does not read it. On all of these the table follows the reader's system setting.
