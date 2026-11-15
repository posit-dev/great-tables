# Location Selection

The `loc` module is what connects your styling intentions to specific parts of the table. Each location specifier identifies a region of the table (such as the header, body, stub, or footer) and many of them also support targeting specific columns or rows within that region. This page provides a comprehensive overview of all available location specifiers and how to use them effectively.

Understanding the `loc` module is valuable because it provides a single, consistent vocabulary for addressing any part of the table. Rather than learning separate APIs for styling the header vs. the body vs. the stub, you use the same `loc.*()` specifiers everywhere. This means that once you know how to style a column label, the pattern for styling a row group label or a source note is immediately familiar.

## Overview

**Great Tables** uses the `loc` module to specify locations for styling in [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style). Some location specifiers also allow selecting specific columns and rows of data.

For example, you might style a particular row name, group, column, or spanner label.

The table below shows the different location specifiers, along with the types of column or row selection they allow.

| table part | name                     | selection                 |
|------------|--------------------------|---------------------------|
| header     | loc.header()             | composite                 |
|            | loc.title()              |                           |
|            | loc.subtitle()           |                           |
| stubhead   | loc.stubhead()           |                           |
| boxhead    | loc.column_header()      | composite                 |
|            | loc.spanner_labels()     | columns                   |
|            | loc.column_labels()      | columns                   |
| row stub   | loc.stub()               | rows                      |
|            | loc.row_groups()         | rows                      |
|            | loc.summary_stub()       | groups and rows           |
|            | loc.grand_summary_stub() | rows                      |
| table body | loc.body()               | columns, rows, and mask   |
|            | loc.summary()            | groups, columns, and rows |
|            | loc.grand_summary()      | columns, rows, and mask   |
| footer     | loc.footer()             | composite                 |
|            | loc.footnotes()          |                           |
|            | loc.source_notes()       |                           |

Note that composite specifiers are ones that target multiple locations. For example, [loc.header()](../reference/loc.header.md#great_tables.loc.header) specifies both [loc.title()](../reference/loc.title.md#great_tables.loc.title) and [loc.subtitle()](../reference/loc.subtitle.md#great_tables.loc.subtitle).

## Setting Up the Data

The examples below will use this small dataset to show selecting different locations, as well as specific rows and columns within a location (where supported).

``` python
import polars as pl
import polars.selectors as cs

from great_tables import GT, data, loc, style

pl_exibble = data.pl.exibble[[0, 1, 4], ["num", "char", "group"]]

pl_exibble
```

shape: (3, 3)

| num    | char      | group   |
|--------|-----------|---------|
| f64    | str       | str     |
| 0.1111 | "apricot" | "grp_a" |
| 2.222  | "banana"  | "grp_a" |
| 5550.0 | null      | "grp_b" |

This small three-row, three-column dataset gives us enough structure to demonstrate row and column targeting without cluttering the output.

## Simple Locations

Simple locations don't take any arguments.

For example, styling the title uses [loc.title()](../reference/loc.title.md#great_tables.loc.title).

``` python
(
    GT(pl_exibble)
    .tab_header("A title", "A subtitle")
    .tab_style(
        style.fill("yellow"),
        loc.title(),
    )
)
```

| A title    |         |       |
|------------|---------|-------|
| A subtitle |         |       |
| num        | char    | group |
| 0.1111     | apricot | grp_a |
| 2.222      | banana  | grp_a |
| 5550.0     | None    | grp_b |

Only the title receives the yellow fill; the subtitle and the rest of the table remain unstyled. Simple locations are useful when you want precise control over a single element.

## Composite Locations

Composite locations target multiple simple locations.

For example, [loc.header()](../reference/loc.header.md#great_tables.loc.header) includes both [loc.title()](../reference/loc.title.md#great_tables.loc.title) and [loc.subtitle()](../reference/loc.subtitle.md#great_tables.loc.subtitle).

``` python
(
    GT(pl_exibble)
    .tab_header("A title", "A subtitle")
    .tab_style(
        style.fill("yellow"),
        loc.header(),
    )
)
```

| A title    |         |       |
|------------|---------|-------|
| A subtitle |         |       |
| num        | char    | group |
| 0.1111     | apricot | grp_a |
| 2.222      | banana  | grp_a |
| 5550.0     | None    | grp_b |

Both the title and subtitle are filled with yellow because [loc.header()](../reference/loc.header.md#great_tables.loc.header) targets the entire header region. Composite locations are a convenient shorthand when you want the same style on all sub-parts.

## Body Columns, Rows, and Mask

Use `columns=` and `rows=` in [loc.body()](../reference/loc.body.md#great_tables.loc.body) to style specific cells in the table body.

``` python
(
    GT(pl_exibble).tab_style(
        style.fill("yellow"),
        loc.body(
            columns=cs.starts_with("cha"),
            rows=pl.col("char").str.contains("a"),
        ),
    )
)
```

| num    | char    | group |
|--------|---------|-------|
| 0.1111 | apricot | grp_a |
| 2.222  | banana  | grp_a |
| 5550.0 | None    | grp_b |

Alternatively, use `mask=` in [loc.body()](../reference/loc.body.md#great_tables.loc.body) to apply conditional styling to rows on a per-column basis.

``` python
(
    GT(pl_exibble).tab_style(
        style.fill("yellow"),
        loc.body(mask=cs.string().str.contains("p")),
    )
)
```

| num    | char    | group |
|--------|---------|-------|
| 0.1111 | apricot | grp_a |
| 2.222  | banana  | grp_a |
| 5550.0 | None    | grp_b |

This is discussed in detail in [Styling the Table Body](styling-the-table-body.md).

## Column Labels

Locations like [loc.spanner_labels()](../reference/loc.spanner_labels.md#great_tables.loc.spanner_labels) and [loc.column_labels()](../reference/loc.column_labels.md#great_tables.loc.column_labels) can select specific column and spanner labels.

You can use name strings, index positions, or Polars selectors.

``` python
GT(pl_exibble).tab_style(
    style.fill("yellow"),
    loc.column_labels(
        cs.starts_with("cha"),
    ),
)
```

| num    | char    | group |
|--------|---------|-------|
| 0.1111 | apricot | grp_a |
| 2.222  | banana  | grp_a |
| 5550.0 | None    | grp_b |

However, note that [loc.spanner_labels()](../reference/loc.spanner_labels.md#great_tables.loc.spanner_labels) currently only accepts a list of spanner IDs.

## Row and Group Names

Row and group names in [loc.stub()](../reference/loc.stub.md#great_tables.loc.stub) and [loc.row_groups()](../reference/loc.row_groups.md#great_tables.loc.row_groups) may be specified three ways:

- by name
- by index
- by Polars expression

``` python
gt_stub = GT(pl_exibble).tab_stub(
    rowname_col="char",
    groupname_col="group",
)

gt_stub.tab_style(style.fill("yellow"), loc.stub())
```

|         | num    |
|---------|--------|
| grp_a   |        |
| apricot | 0.1111 |
| banana  | 2.222  |
| grp_b   |        |
| None    | 5550.0 |

All row labels in the stub are highlighted in yellow.

``` python
gt_stub.tab_style(style.fill("yellow"), loc.stub("banana"))
```

|         | num    |
|---------|--------|
| grp_a   |        |
| apricot | 0.1111 |
| banana  | 2.222  |
| grp_b   |        |
| None    | 5550.0 |

Only the `"banana"` row label is styled, demonstrating name-based targeting.

``` python
gt_stub.tab_style(style.fill("yellow"), loc.stub(["apricot", 2]))
```

|         | num    |
|---------|--------|
| grp_a   |        |
| apricot | 0.1111 |
| banana  | 2.222  |
| grp_b   |        |
| None    | 5550.0 |

You can mix names and integer indices in a list to target multiple specific rows at once.

### Groups by Name and Position

Note that for specifying row groups, the group corresponding to the group name or row number in the original data is used.

For example, the code below styles the group corresponding to the row at index 1 (i.e., the second row) in the data.

``` python
gt_stub.tab_style(
    style.fill("yellow"),
    loc.row_groups(1),
)
```

|         | num    |
|---------|--------|
| grp_a   |        |
| apricot | 0.1111 |
| banana  | 2.222  |
| grp_b   |        |
| None    | 5550.0 |

Since the second row (starting with "banana") is in "grp_a", that is the group that gets styled.

This means you can use a Polars expression to select groups:

``` python
gt_stub.tab_style(
    style.fill("yellow"),
    loc.row_groups(pl.col("group") == "grp_b"),
)
```

|         | num    |
|---------|--------|
| grp_a   |        |
| apricot | 0.1111 |
| banana  | 2.222  |
| grp_b   |        |
| None    | 5550.0 |

You can also specify group names using a string (or list of strings).

``` python
gt_stub.tab_style(
    style.fill("yellow"),
    loc.row_groups("grp_b"),
)
```

|         | num    |
|---------|--------|
| grp_a   |        |
| apricot | 0.1111 |
| banana  | 2.222  |
| grp_b   |        |
| None    | 5550.0 |

The `loc` module provides a complete vocabulary for addressing any part of your table. By combining location specifiers with column selectors, row filters, and Polars expressions, you can apply styles to exactly the right cells. For more details on styling itself, see [Styling the Table Body](styling-the-table-body.md) and [Styling the Whole Table](styling-the-whole-table.md).
