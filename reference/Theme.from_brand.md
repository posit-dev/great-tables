# Theme.from_brand()

Build a [Theme](../reference/Theme.md#great_tables.Theme) from a brand.yml file.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_theme.py#L233-L356)

``` python
Theme.from_brand(
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

## Parameters

`brand: str | Path | Brand | None = None`  
The brand to use: the path to a brand.yml file, a `brand_yml.Brand` object, or `None` to have `brand_yml` find a brand file itself (see `brand_yml.Brand.from_yaml()`).

`dark: str | Path | Brand | None = None`  
A brand to use in dark mode, given in the same ways as `brand`. Only its `background` and `foreground` colors are used, as the colors of the theme's `dark=` theme.

## Returns

`Theme`  
A [Theme](../reference/Theme.md#great_tables.Theme) that can be applied to a table with [GT.opt_theme()](../reference/GT.opt_theme.md#great_tables.GT.opt_theme).

## Examples

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
