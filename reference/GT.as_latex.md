# GT.as_latex()

Output a GT object as LaTeX

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_export.py#L272-L381)

``` python
GT.as_latex(
    use_longtable=False,
    tbl_pos=None,
)
```

The [as_latex()](../reference/GT.as_latex.md#great_tables.GT.as_latex) method outputs a GT object as a LaTeX fragment. This method is useful for when you need to include a table as part of a LaTeX document. The LaTeX fragment contains the table as a string.

> **Warning**
>
> [as_latex()](../reference/GT.as_latex.md#great_tables.GT.as_latex) is still experimental.

## Parameters

`use_longtable: bool = False`  
An option to use the `longtable` environment in LaTeX output. This is useful for tables that span multiple pages and don't require precise positioning.

`tbl_pos: str | None = None`  
The position of the table in the LaTeX output when `use_longtable=False`. Valid values for positioning include `"!t"` (top of page), `"!b"` (bottom of the page), `"!h"` (here), `"!p"` (on a separate page), and `"!H"` (exactly here). If a value is not provided then the table will be placed at the top of the page; if in the Quarto render then the table positioning option will be ignored in favor of any setting within the Quarto rendering environment.

## Returns

`str`  
A LaTeX fragment that contains the table.

## Latex Packages

The LaTeX fragment uses commands from these packages, which need to be loaded in the document's preamble:

- `booktabs` (always)
- `longtable`, with `use_longtable=True`
- `hyperref`, if the table has links from [`fmt_url()`](../reference/GT.fmt_url.md#great_tables.GT.fmt_url) or [`fmt_email()`](../reference/GT.fmt_email.md#great_tables.GT.fmt_email)
- `anyfontsize` (optional), so that a `table_font_size=` set with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) is used at exactly that size rather than the nearest available one

For example, `\usepackage{booktabs}` and `\usepackage{longtable}`. Some currency symbols (e.g., `"₹"` for `"INR"`) need XeLaTeX or LuaLaTeX rather than pdfLaTeX (see [`fmt_currency()`](../reference/GT.fmt_currency.md#great_tables.GT.fmt_currency)).

## Limitations

The [as_latex()](../reference/GT.as_latex.md#great_tables.GT.as_latex) method is still experimental and has some limitations. The following functionality that is supported in HTML output tables is not currently supported in LaTeX output tables:

- footnotes (via the [tab_footnote()](../reference/GT.tab_footnote.md#great_tables.GT.tab_footnote) method), which raise an error
- the [fmt_nanoplot()](../reference/GT.fmt_nanoplot.md#great_tables.GT.fmt_nanoplot) method, which raises an error
- the [`fmt_image()`](../reference/GT.fmt_image.md#great_tables.GT.fmt_image), [fmt_flag()](../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag), and [fmt_icon()](../reference/GT.fmt_icon.md#great_tables.GT.fmt_icon) methods, which issue a warning and leave the cell values unformatted
- styles, whether set with the [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) or [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) methods (a warning is issued and the table is rendered without them)
- most options in the [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) method, particularly those that are specific to styling text, borders, or adding fill colors to cells (the ones that are used are `table_width=`, `table_font_size=`, `stub_indent_length=`, and `row_group_as_column=`), and so also the `opt_*()` methods that set them, such as [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize)
- interactive tables (via the `opt_interactive()` method), which are rendered as static tables

As development continues, we will work to expand the capabilities of the [as_latex()](../reference/GT.as_latex.md#great_tables.GT.as_latex) method to reduce these limitations and more clearly document what is and is not supported.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset to create a new table.

``` python
from great_tables import GT
from great_tables.data import gtcars
import polars as pl

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select(["mfr", "model", "msrp"])
    .head(5)
)

gt_tbl = (
    GT(gtcars_mini)
    .tab_header(
        title="Data Listing from the gtcars Dataset",
        subtitle="Only five rows from the dataset are shown here."
    )
    .fmt_currency(columns="msrp")
)

gt_tbl
```

| Data Listing from the gtcars Dataset            |              |              |
|-------------------------------------------------|--------------|--------------|
| Only five rows from the dataset are shown here. |              |              |
| mfr                                             | model        | msrp         |
| Ford                                            | GT           | \$447,000.00 |
| Ferrari                                         | 458 Speciale | \$291,744.00 |
| Ferrari                                         | 458 Spider   | \$263,553.00 |
| Ferrari                                         | 458 Italia   | \$233,509.00 |
| Ferrari                                         | 488 GTB      | \$245,400.00 |

Now we can return the table as string of LaTeX code using the [as_latex()](../reference/GT.as_latex.md#great_tables.GT.as_latex) method.

``` python
gt_tbl.as_latex()
```

    '\\begin{table}\n\\caption*{\n{\\large Data Listing from the gtcars Dataset} \\\\\n{\\small Only five rows from the dataset are shown here.}\n} \n\n\\fontsize{12.0pt}{14.4pt}\\selectfont\n\n\\begin{tabular*}{\\linewidth}{@{\\extracolsep{\\fill}}llr}\n\\toprule\nmfr & model & msrp \\\\ \n\\midrule\\addlinespace[2.5pt]\nFord & GT & \\$447,000.00 \\\\\nFerrari & 458 Speciale & \\$291,744.00 \\\\\nFerrari & 458 Spider & \\$263,553.00 \\\\\nFerrari & 458 Italia & \\$233,509.00 \\\\\nFerrari & 488 GTB & \\$245,400.00 \\\\\n\\bottomrule\n\\end{tabular*}\n\n\\end{table}\n'

The LaTeX string contains the code just for the table (it's not a complete LaTeX document). This output can be useful for embedding a GT table in an existing LaTeX document.
