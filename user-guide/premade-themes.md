# Premade Themes

Building a complete table theme from scratch with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) requires setting many individual options. For common styling needs, **Great Tables** offers a collection of `opt_*()` convenience methods that bundle these options into simple, one-line calls. This page demonstrates how to use premade themes and the various convenience methods available for quick table customization.

Premade themes are ideal for getting a polished look quickly, especially during exploratory work or when building dashboards where visual consistency matters more than pixel-perfect custom styling. For publication or brand-specific tables, you may want to start with a premade theme and then customize it further with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) to match your exact requirements.

Great Tables provides convenience methods starting with `opt_` (e.g. [opt_row_striping()](../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping)), as a shortcut for various styles that can be set via [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options).

There are two important kinds of `GT.opt_*()` methods:

- [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize): allows setting one of six premade table themes.
- The remaining `opt_*()` methods: shortcuts for common uses of [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options).

We'll use the basic GT object below for most examples, since it marks some of the table parts.

``` python
from great_tables import GT, exibble, md

lil_exibble = exibble.head(5)[["num", "char", "row", "group"]]

gt_ex = (
    GT(lil_exibble, rowname_col="row", groupname_col="group")
    .tab_header(
        title=md("Data listing from exibble"),
        subtitle=md("This is a **Great Tables** dataset."),
    )
    .tab_stubhead(label="row")
    .fmt_number(columns="num")
    .fmt_currency(columns="currency")
    .tab_source_note(source_note="This is only a portion of the dataset.")
    .opt_vertical_padding(scale=0.5)
)

gt_ex
```

| Data listing from exibble              |          |         |
|----------------------------------------|----------|---------|
| This is a **Great Tables** dataset.    |          |         |
| row                                    | num      | char    |
| grp_a                                  |          |         |
| row_1                                  | 0.11     | apricot |
| row_2                                  | 2.22     | banana  |
| row_3                                  | 33.33    | coconut |
| row_4                                  | 444.40   | durian  |
| grp_b                                  |          |         |
| row_5                                  | 5,550.00 | None    |
| This is only a portion of the dataset. |          |         |

## [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize): premade themes

Below are the first two premade styles. The first uses `color="blue"`, and the second uses `color="red"`.

``` python
gt_ex.opt_stylize(style=1, color="blue")
```

| Data listing from exibble              |          |         |
|----------------------------------------|----------|---------|
| This is a **Great Tables** dataset.    |          |         |
| row                                    | num      | char    |
| grp_a                                  |          |         |
| row_1                                  | 0.11     | apricot |
| row_2                                  | 2.22     | banana  |
| row_3                                  | 33.33    | coconut |
| row_4                                  | 444.40   | durian  |
| grp_b                                  |          |         |
| row_5                                  | 5,550.00 | None    |
| This is only a portion of the dataset. |          |         |

``` python
gt_ex.opt_stylize(style=2, color="red")
```

| Data listing from exibble              |          |         |
|----------------------------------------|----------|---------|
| This is a **Great Tables** dataset.    |          |         |
| row                                    | num      | char    |
| grp_a                                  |          |         |
| row_1                                  | 0.11     | apricot |
| row_2                                  | 2.22     | banana  |
| row_3                                  | 33.33    | coconut |
| row_4                                  | 444.40   | durian  |
| grp_b                                  |          |         |
| row_5                                  | 5,550.00 | None    |
| This is only a portion of the dataset. |          |         |

Notice that first table (blue) emphasizes the row labels with a solid background color. The second table (red) emphasizes the column labels, and uses solid lines to separate the body cell values. See [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize) for all available color options.

There are six styles available, each emphasizing different table parts. The `style=` values are numbered from `1` to `6`:

1

Data listing from exibble

This is a Great Tables dataset.

row

num

char

grp_a

row_1

0.11

apricot

row_2

2.22

banana

row_3

33.33

coconut

row_4

444.40

durian

grp_b

row_5

5,550.00

None

This is only a portion of the dataset.

2

Data listing from exibble

This is a Great Tables dataset.

row

num

char

grp_a

row_1

0.11

apricot

row_2

2.22

banana

row_3

33.33

coconut

row_4

444.40

durian

grp_b

row_5

5,550.00

None

This is only a portion of the dataset.

3

Data listing from exibble

This is a Great Tables dataset.

row

num

char

grp_a

row_1

0.11

apricot

row_2

2.22

banana

row_3

33.33

coconut

row_4

444.40

durian

grp_b

row_5

5,550.00

None

This is only a portion of the dataset.

4

Data listing from exibble

This is a Great Tables dataset.

row

num

char

grp_a

row_1

0.11

apricot

row_2

2.22

banana

row_3

33.33

coconut

row_4

444.40

durian

grp_b

row_5

5,550.00

None

This is only a portion of the dataset.

5

Data listing from exibble

This is a Great Tables dataset.

row

num

char

grp_a

row_1

0.11

apricot

row_2

2.22

banana

row_3

33.33

coconut

row_4

444.40

durian

grp_b

row_5

5,550.00

None

This is only a portion of the dataset.

6

Data listing from exibble

This is a Great Tables dataset.

row

num

char

grp_a

row_1

0.11

apricot

row_2

2.22

banana

row_3

33.33

coconut

row_4

444.40

durian

grp_b

row_5

5,550.00

None

This is only a portion of the dataset.

When choosing a style, consider your audience and context. Styles 1 and 2 emphasize structure through color, making table regions visually distinct. Styles 3 and 4 use lines and shading for a more traditional look. Styles 5 and 6 are more minimal, relying on subtle separation. Heavier styling works well for standalone presentations, while lighter styling is better suited for tables embedded in text-heavy reports where the table should complement rather than dominate the page.

## `opt_*()` convenience methods

This section shows the different `opt_*()` methods available. They serve as convenience methods for common [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) tasks.

### Align table header

``` python
gt_ex.opt_align_table_header(align="left")
```

| Data listing from exibble              |          |         |
|----------------------------------------|----------|---------|
| This is a **Great Tables** dataset.    |          |         |
| row                                    | num      | char    |
| grp_a                                  |          |         |
| row_1                                  | 0.11     | apricot |
| row_2                                  | 2.22     | banana  |
| row_3                                  | 33.33    | coconut |
| row_4                                  | 444.40   | durian  |
| grp_b                                  |          |         |
| row_5                                  | 5,550.00 | None    |
| This is only a portion of the dataset. |          |         |

The title and subtitle are now left-aligned rather than centered, which works well for tables embedded in text-heavy documents.

### Make text ALL CAPS

``` python
gt_ex.opt_all_caps()
```

| Data listing from exibble              |          |         |
|----------------------------------------|----------|---------|
| This is a **Great Tables** dataset.    |          |         |
| row                                    | num      | char    |
| grp_a                                  |          |         |
| row_1                                  | 0.11     | apricot |
| row_2                                  | 2.22     | banana  |
| row_3                                  | 33.33    | coconut |
| row_4                                  | 444.40   | durian  |
| grp_b                                  |          |         |
| row_5                                  | 5,550.00 | None    |
| This is only a portion of the dataset. |          |         |

Column labels and row group labels are rendered in uppercase, giving the table a more formal, structured appearance.

### Reduce or expand padding

``` python
gt_ex.opt_vertical_padding(scale=0.3)
```

| Data listing from exibble              |          |         |
|----------------------------------------|----------|---------|
| This is a **Great Tables** dataset.    |          |         |
| row                                    | num      | char    |
| grp_a                                  |          |         |
| row_1                                  | 0.11     | apricot |
| row_2                                  | 2.22     | banana  |
| row_3                                  | 33.33    | coconut |
| row_4                                  | 444.40   | durian  |
| grp_b                                  |          |         |
| row_5                                  | 5,550.00 | None    |
| This is only a portion of the dataset. |          |         |

Reducing vertical padding creates a more compact table that fits more data into less vertical space.

``` python
gt_ex.opt_horizontal_padding(scale=3)
```

| Data listing from exibble              |          |         |
|----------------------------------------|----------|---------|
| This is a **Great Tables** dataset.    |          |         |
| row                                    | num      | char    |
| grp_a                                  |          |         |
| row_1                                  | 0.11     | apricot |
| row_2                                  | 2.22     | banana  |
| row_3                                  | 33.33    | coconut |
| row_4                                  | 444.40   | durian  |
| grp_b                                  |          |         |
| row_5                                  | 5,550.00 | None    |
| This is only a portion of the dataset. |          |         |

Increasing horizontal padding adds breathing room between columns, which improves readability when columns contain long values.

### Set table outline

``` python
gt_ex.opt_table_outline()
```

| Data listing from exibble              |          |         |
|----------------------------------------|----------|---------|
| This is a **Great Tables** dataset.    |          |         |
| row                                    | num      | char    |
| grp_a                                  |          |         |
| row_1                                  | 0.11     | apricot |
| row_2                                  | 2.22     | banana  |
| row_3                                  | 33.33    | coconut |
| row_4                                  | 444.40   | durian  |
| grp_b                                  |          |         |
| row_5                                  | 5,550.00 | None    |
| This is only a portion of the dataset. |          |         |

The `opt_*()` methods give you quick access to common styling patterns without needing to remember the specific [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) argument names. For full control, you can always drop down to [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) directly, but these convenience methods cover the most frequent customization needs in just a single method call.
