# Theme

A set of design tokens and table options that style a table.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_theme.py#L97-L356)

``` python
Theme(
    *,
    background=None,
    foreground=None,
    border=None,
    border_strong=None,
    stripe=None,
    accent=None,
    font=None,
    font_size=None,
    dark=None,
    **options,
)
```

A [Theme](../reference/Theme.md#great_tables.Theme) collects values for a small set of semantic tokens, plus any option accepted by [GT.tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options), so that they can be applied to a table together with [GT.opt_theme()](../reference/GT.opt_theme.md#great_tables.GT.opt_theme). Only the tokens and options that are given are stored. Each token is exposed in the table's CSS as a custom property:

| Token           | CSS variable               |
|-----------------|----------------------------|
| `background`    | `--gt-color-background`    |
| `foreground`    | `--gt-color-foreground`    |
| `border`        | `--gt-color-border`        |
| `border_strong` | `--gt-color-border-strong` |
| `stripe`        | `--gt-color-stripe`        |
| `accent`        | `--gt-color-accent`        |
| `font`          | `--gt-font-family`         |
| `font_size`     | `--gt-font-size`           |

## Parameters

`background: str | None = None`  
The background color of the table.

`foreground: str | None = None`  
The color of text in the table.

`border: str | None = None`  
The color of the table's regular lines.

`border_strong: str | None = None`  
The color of the table's emphasized lines, such as the one under the column labels.

`stripe: str | None = None`  
The background color of striped rows.

`accent: str | None = None`  
The accent color, used for interactive elements.

`font: str | list[str] | None = None`  
The font or fonts of the table, as a single name or a list of names in order of preference.

`font_size: str | int | None = None`  
The base font size of the table, as a CSS length or a number of pixels.

`dark: Theme | None = None`  
A [Theme](../reference/Theme.md#great_tables.Theme) with the values to use instead when the table is shown in dark mode. It can hold only the color tokens `background`, `foreground`, `border`, `border_strong` and `stripe`, and color options that are written to the table's stylesheet (such as `table_body_hlines_color`). A background option of the theme with no value here keeps an `"auto"` table light, and a border color option with no value here is blended toward the text color in dark mode.

`**options: Any`  
Any option accepted by [GT.tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options), for example `data_row_padding`.

## Examples

A theme that sets a border color and font, with its own colors for dark mode.

``` python
from great_tables import GT, Theme, data

theme = Theme(
    border="#CCCCCC",
    font="Inter",
    dark=Theme(background="#101418", border="#2A3038"),
)

GT(data.pl.exibble.select("num", "char", "currency")).opt_theme(theme)
```

| num       | char       | currency |
|-----------|------------|----------|
| 0.1111    | apricot    | 49.95    |
| 2.222     | banana     | 17.95    |
| 33.33     | coconut    | 1.39     |
| 444.4     | durian     | 65100.0  |
| 5550.0    | None       | 1325.81  |
| None      | fig        | 13.255   |
| 777000.0  | grapefruit | None     |
| 8880000.0 | honeydew   | 0.44     |

## Methods

| Name | Description |
|----|----|
| [from_brand()](#great_tables.Theme.from_brand) | Build a [Theme](../reference/Theme.md#great_tables.Theme) from a brand.yml file. |

### from_brand()

Build a [Theme](../reference/Theme.md#great_tables.Theme) from a brand.yml file.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_theme.py#L233-L356)

``` python
from_brand(
    brand=None,
    dark=None,
)
```

A [brand.yml](https://posit-dev.github.io/brand-yml/) file describes the colors and fonts of a brand. [Theme.from_brand()](../reference/Theme.md#great_tables.Theme.from_brand) reads one and maps these fields to the tokens of a [Theme](../reference/Theme.md#great_tables.Theme):

| brand.yml field | [Theme](../reference/Theme.md#great_tables.Theme) token |
|----|----|
| `color.background` | `background` |
| `color.foreground` | `foreground` |
| `color.primary` | `accent` |
| `typography.base.family` | `font` |
| `typography.base.size` | `font_size` |

Colors that name an entry of `color.palette` are used as the color of that entry. Fields that the brand does not have are left out of the theme. This method requires the [brand_yml](https://pypi.org/project/brand-yml/) package, which is installed with `pip install great_tables[brand]`.

#### Parameters

`brand: str | Path | Brand | None = None`  
The brand to use: the path to a brand.yml file, a `brand_yml.Brand` object, or `None` to have `brand_yml` find a brand file itself (see `brand_yml.Brand.from_yaml()`).

`dark: str | Path | Brand | None = None`  
A brand to use in dark mode, given in the same ways as `brand`. Only its `background` and `foreground` colors are used, as the colors of the theme's `dark=` theme.

#### Returns

`Theme`  
A [Theme](../reference/Theme.md#great_tables.Theme) that can be applied to a table with [GT.opt_theme()](../reference/GT.opt_theme.md#great_tables.GT.opt_theme).

#### Examples

Take a brand file `_brand.yml` with these contents.

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

Building a theme from it and applying the theme to a table looks like this.

``` python
from great_tables import GT, Theme, data

theme = Theme.from_brand("_brand.yml")

GT(data.pl.exibble).opt_theme(theme)
```

The result is the same as the theme made directly with `Theme(background="#FDF6E3", foreground="#073642", accent="#001F3F", font="Inter", font_size="14px")`. A second brand file can supply colors for dark mode with `Theme.from_brand("_brand.yml", dark="_brand-dark.yml")`.
