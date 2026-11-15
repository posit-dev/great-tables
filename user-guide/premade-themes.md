# Premade Themes

Building a complete table theme from scratch with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) requires setting many individual options. For common styling needs, **Great Tables** offers a collection of `opt_*()` convenience methods that bundle these options into simple, one-line calls. This page demonstrates how to use premade themes and the various convenience methods available for quick table customization.

Premade themes are ideal for getting a polished look quickly, especially during exploratory work or when building dashboards where visual consistency matters more than pixel-perfect custom styling. For publication or brand-specific tables, you may want to start with a premade theme and then customize it further with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) to match your exact requirements.

Great Tables provides convenience methods starting with `opt_` (e.g., [opt_row_striping()](../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping)), as a shortcut for various styles that can be set via [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options).

There are two important kinds of `opt_*()` methods:

- [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize): allows setting one of six premade table themes.
- The remaining `opt_*()` methods: shortcuts for common uses of [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options).

We'll use the basic GT object below for most examples, since it marks some of the table parts.

``` python
from great_tables import GT, data, md

lil_exibble = data.pl.exibble.head(5).select("num", "char", "currency", "row", "group")

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

| Data listing from exibble              |          |         |             |
|----------------------------------------|----------|---------|-------------|
| This is a **Great Tables** dataset.    |          |         |             |
| row                                    | num      | char    | currency    |
| grp_a                                  |          |         |             |
| row_1                                  | 0.11     | apricot | \$49.95     |
| row_2                                  | 2.22     | banana  | \$17.95     |
| row_3                                  | 33.33    | coconut | \$1.39      |
| row_4                                  | 444.40   | durian  | \$65,100.00 |
| grp_b                                  |          |         |             |
| row_5                                  | 5,550.00 | None    | \$1,325.81  |
| This is only a portion of the dataset. |          |         |             |

## [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize): Premade Themes

Below are the first two premade styles. The first uses `color="blue"`, and the second uses `color="red"`.

``` python
gt_ex.opt_stylize(style=1, color="blue")
```

| Data listing from exibble              |          |         |             |
|----------------------------------------|----------|---------|-------------|
| This is a **Great Tables** dataset.    |          |         |             |
| row                                    | num      | char    | currency    |
| grp_a                                  |          |         |             |
| row_1                                  | 0.11     | apricot | \$49.95     |
| row_2                                  | 2.22     | banana  | \$17.95     |
| row_3                                  | 33.33    | coconut | \$1.39      |
| row_4                                  | 444.40   | durian  | \$65,100.00 |
| grp_b                                  |          |         |             |
| row_5                                  | 5,550.00 | None    | \$1,325.81  |
| This is only a portion of the dataset. |          |         |             |

``` python
gt_ex.opt_stylize(style=2, color="red")
```

| Data listing from exibble              |          |         |             |
|----------------------------------------|----------|---------|-------------|
| This is a **Great Tables** dataset.    |          |         |             |
| row                                    | num      | char    | currency    |
| grp_a                                  |          |         |             |
| row_1                                  | 0.11     | apricot | \$49.95     |
| row_2                                  | 2.22     | banana  | \$17.95     |
| row_3                                  | 33.33    | coconut | \$1.39      |
| row_4                                  | 444.40   | durian  | \$65,100.00 |
| grp_b                                  |          |         |             |
| row_5                                  | 5,550.00 | None    | \$1,325.81  |
| This is only a portion of the dataset. |          |         |             |

Notice that the first table (blue) emphasizes the row labels with a solid background color. The second table (red) emphasizes the column labels, and uses solid lines to separate the body cell values. There are six colors to choose from: `"blue"` (the default), `"cyan"`, `"pink"`, `"green"`, `"red"`, and `"gray"`.

There are six styles available, each emphasizing different table parts. The `style=` values are numbered from `1` to `6`:

1

Data listing from exibble

This is a Great Tables dataset.

row

num

char

currency

grp_a

row_1

0.11

apricot

\$49.95

row_2

2.22

banana

\$17.95

row_3

33.33

coconut

\$1.39

row_4

444.40

durian

\$65,100.00

grp_b

row_5

5,550.00

None

\$1,325.81

This is only a portion of the dataset.

2

Data listing from exibble

This is a Great Tables dataset.

row

num

char

currency

grp_a

row_1

0.11

apricot

\$49.95

row_2

2.22

banana

\$17.95

row_3

33.33

coconut

\$1.39

row_4

444.40

durian

\$65,100.00

grp_b

row_5

5,550.00

None

\$1,325.81

This is only a portion of the dataset.

3

Data listing from exibble

This is a Great Tables dataset.

row

num

char

currency

grp_a

row_1

0.11

apricot

\$49.95

row_2

2.22

banana

\$17.95

row_3

33.33

coconut

\$1.39

row_4

444.40

durian

\$65,100.00

grp_b

row_5

5,550.00

None

\$1,325.81

This is only a portion of the dataset.

4

Data listing from exibble

This is a Great Tables dataset.

row

num

char

currency

grp_a

row_1

0.11

apricot

\$49.95

row_2

2.22

banana

\$17.95

row_3

33.33

coconut

\$1.39

row_4

444.40

durian

\$65,100.00

grp_b

row_5

5,550.00

None

\$1,325.81

This is only a portion of the dataset.

5

Data listing from exibble

This is a Great Tables dataset.

row

num

char

currency

grp_a

row_1

0.11

apricot

\$49.95

row_2

2.22

banana

\$17.95

row_3

33.33

coconut

\$1.39

row_4

444.40

durian

\$65,100.00

grp_b

row_5

5,550.00

None

\$1,325.81

This is only a portion of the dataset.

6

Data listing from exibble

This is a Great Tables dataset.

row

num

char

currency

grp_a

row_1

0.11

apricot

\$49.95

row_2

2.22

banana

\$17.95

row_3

33.33

coconut

\$1.39

row_4

444.40

durian

\$65,100.00

grp_b

row_5

5,550.00

None

\$1,325.81

This is only a portion of the dataset.

When choosing a style, consider your audience and context. Styles 2, 4, and 5 draw vertical lines between the columns and an outline around the table, giving a gridded look, while styles 1, 3, and 6 leave those out for a more open layout (style 3 separates its rows with dashed lines). Every style but the first puts a solid fill behind the column labels, and the stub is filled with the theme color in styles 1 and 6, with gray in styles 3, 4, and 5, and not at all in style 2. Heavier styling works well for standalone presentations, while lighter styling is better suited for tables embedded in text-heavy reports where the table should complement rather than dominate the page. By default, each style also stripes the body rows (turn this off with `add_row_striping=False`).

## `opt_*()` Convenience Methods

This section shows the different `opt_*()` methods available. They serve as convenience methods for common [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) tasks.

### Align the Table Header

``` python
gt_ex.opt_align_table_header(align="left")
```

| Data listing from exibble              |          |         |             |
|----------------------------------------|----------|---------|-------------|
| This is a **Great Tables** dataset.    |          |         |             |
| row                                    | num      | char    | currency    |
| grp_a                                  |          |         |             |
| row_1                                  | 0.11     | apricot | \$49.95     |
| row_2                                  | 2.22     | banana  | \$17.95     |
| row_3                                  | 33.33    | coconut | \$1.39      |
| row_4                                  | 444.40   | durian  | \$65,100.00 |
| grp_b                                  |          |         |             |
| row_5                                  | 5,550.00 | None    | \$1,325.81  |
| This is only a portion of the dataset. |          |         |             |

The title and subtitle are now left-aligned rather than centered, which works well for tables embedded in text-heavy documents.

### Make Text ALL CAPS

``` python
gt_ex.opt_all_caps()
```

| Data listing from exibble              |          |         |             |
|----------------------------------------|----------|---------|-------------|
| This is a **Great Tables** dataset.    |          |         |             |
| row                                    | num      | char    | currency    |
| grp_a                                  |          |         |             |
| row_1                                  | 0.11     | apricot | \$49.95     |
| row_2                                  | 2.22     | banana  | \$17.95     |
| row_3                                  | 33.33    | coconut | \$1.39      |
| row_4                                  | 444.40   | durian  | \$65,100.00 |
| grp_b                                  |          |         |             |
| row_5                                  | 5,550.00 | None    | \$1,325.81  |
| This is only a portion of the dataset. |          |         |             |

Column labels, row labels in the stub, and row group labels are rendered in uppercase (and in a smaller, bolder font), giving the table a more formal, structured appearance.

### Reduce or Expand Padding

``` python
gt_ex.opt_vertical_padding(scale=0.3)
```

| Data listing from exibble              |          |         |             |
|----------------------------------------|----------|---------|-------------|
| This is a **Great Tables** dataset.    |          |         |             |
| row                                    | num      | char    | currency    |
| grp_a                                  |          |         |             |
| row_1                                  | 0.11     | apricot | \$49.95     |
| row_2                                  | 2.22     | banana  | \$17.95     |
| row_3                                  | 33.33    | coconut | \$1.39      |
| row_4                                  | 444.40   | durian  | \$65,100.00 |
| grp_b                                  |          |         |             |
| row_5                                  | 5,550.00 | None    | \$1,325.81  |
| This is only a portion of the dataset. |          |         |             |

Reducing vertical padding creates a more compact table that fits more data into less vertical space.

``` python
gt_ex.opt_horizontal_padding(scale=3)
```

| Data listing from exibble              |          |         |             |
|----------------------------------------|----------|---------|-------------|
| This is a **Great Tables** dataset.    |          |         |             |
| row                                    | num      | char    | currency    |
| grp_a                                  |          |         |             |
| row_1                                  | 0.11     | apricot | \$49.95     |
| row_2                                  | 2.22     | banana  | \$17.95     |
| row_3                                  | 33.33    | coconut | \$1.39      |
| row_4                                  | 444.40   | durian  | \$65,100.00 |
| grp_b                                  |          |         |             |
| row_5                                  | 5,550.00 | None    | \$1,325.81  |
| This is only a portion of the dataset. |          |         |             |

Increasing horizontal padding adds breathing room between columns, which improves readability when columns contain long values.

### Set a Table Outline

``` python
gt_ex.opt_table_outline()
```

| Data listing from exibble              |          |         |             |
|----------------------------------------|----------|---------|-------------|
| This is a **Great Tables** dataset.    |          |         |             |
| row                                    | num      | char    | currency    |
| grp_a                                  |          |         |             |
| row_1                                  | 0.11     | apricot | \$49.95     |
| row_2                                  | 2.22     | banana  | \$17.95     |
| row_3                                  | 33.33    | coconut | \$1.39      |
| row_4                                  | 444.40   | durian  | \$65,100.00 |
| grp_b                                  |          |         |             |
| row_5                                  | 5,550.00 | None    | \$1,325.81  |
| This is only a portion of the dataset. |          |         |             |

The outline's `style=`, `width=`, and `color=` can all be changed from their defaults (a solid, `3px`, light gray line).

### Stripe the Rows

``` python
gt_ex.opt_row_striping()
```

| Data listing from exibble              |          |         |             |
|----------------------------------------|----------|---------|-------------|
| This is a **Great Tables** dataset.    |          |         |             |
| row                                    | num      | char    | currency    |
| grp_a                                  |          |         |             |
| row_1                                  | 0.11     | apricot | \$49.95     |
| row_2                                  | 2.22     | banana  | \$17.95     |
| row_3                                  | 33.33    | coconut | \$1.39      |
| row_4                                  | 444.40   | durian  | \$65,100.00 |
| grp_b                                  |          |         |             |
| row_5                                  | 5,550.00 | None    | \$1,325.81  |
| This is only a portion of the dataset. |          |         |             |

Alternating row backgrounds help the eye follow a row across a wide table.

### Set the Table Font

``` python
gt_ex.opt_table_font(stack="humanist")
```

| Data listing from exibble              |          |         |             |
|----------------------------------------|----------|---------|-------------|
| This is a **Great Tables** dataset.    |          |         |             |
| row                                    | num      | char    | currency    |
| grp_a                                  |          |         |             |
| row_1                                  | 0.11     | apricot | \$49.95     |
| row_2                                  | 2.22     | banana  | \$17.95     |
| row_3                                  | 33.33    | coconut | \$1.39      |
| row_4                                  | 444.40   | durian  | \$65,100.00 |
| grp_b                                  |          |         |             |
| row_5                                  | 5,550.00 | None    | \$1,325.81  |
| This is only a portion of the dataset. |          |         |             |

The `font=` argument takes one or more font names (or a Google Font via [google_font()](../reference/google_font.md#great_tables.google_font)), and `stack=` takes the name of one of fifteen themed font stacks, like `"humanist"` or `"monospace-code"`, that have been tested to work across a wide range of systems.

The `opt_*()` methods give you quick access to common styling patterns without needing to remember the specific [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) argument names. For full control, you can always drop down to [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) directly, but these convenience methods cover the most frequent customization needs in just a single method call.
