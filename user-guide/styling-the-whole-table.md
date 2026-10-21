# Styling the Whole Table

In [Styling the Table Body](styling-the-table-body.md), we discussed styling table data with [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style). In this article we'll cover how the same method can be used to style many other parts of the table, like the header, specific spanner labels, the footer, and more. By targeting different location specifiers, you can apply fill colors, borders, and text styles to virtually any region of your table.

Whole-table styling is valuable when you want to establish visual hierarchy or brand consistency across the table. For example, giving the header a distinct background separates it from the data, while styling the stub helps readers distinguish identifiers from values. This kind of structural styling works well alongside the cell-level techniques covered on the previous page.

## All locations example

Below is a comprehensive example that shows all possible `loc` specifiers being used. Each table part receives a distinct background color so you can see exactly which region each specifier targets.

``` python
from great_tables import GT, exibble, loc, style

# https://colorbrewer2.org/#type=qualitative&scheme=Paired&n=12 and grey
brewer_colors = [
    "#a6cee3",
    "#1f78b4",
    "#b2df8a",
    "#33a02c",
    "#fb9a99",
    "#e31a1c",
    "#fdbf6f",
    "#ff7f00",
    "#cab2d6",
    "#6a3d9a",
    "#ffff99",
    "#b15928",
    "#808080",
]

c = iter(brewer_colors)

gt = (
    GT(exibble.loc[[0, 1, 4], ["num", "char", "fctr", "row", "group"]])
    .tab_header("title", "subtitle")
    .tab_stub(rowname_col="row", groupname_col="group")
    .tab_source_note("yo")
    .tab_spanner("spanner", ["char", "fctr"])
    .tab_stubhead("stubhead")
    .grand_summary_rows(fns={"Total": lambda x: x.sum(numeric_only=True)})
)

(
    gt.tab_style(style.fill(next(c)), loc.body())
    # Columns -----------
    # TODO: appears in browser, but not vs code
    .tab_style(style.fill(next(c)), loc.column_labels(columns="num"))
    .tab_style(style.fill(next(c)), loc.column_header())
    .tab_style(style.fill(next(c)), loc.spanner_labels(ids=["spanner"]))
    # Header -----------
    .tab_style(style.fill(next(c)), loc.header())
    .tab_style(style.fill(next(c)), loc.subtitle())
    .tab_style(style.fill(next(c)), loc.title())
    # Footer -----------
    .tab_style(style.borders(weight="3px"), loc.source_notes())
    .tab_style(style.fill(next(c)), loc.footer())
    # Stub --------------
    .tab_style(style.fill(next(c)), loc.row_groups())
    .tab_style(style.borders(weight="3px"), loc.stub(rows=1))
    .tab_style(style.fill(next(c)), loc.stub())
    .tab_style(style.fill(next(c)), loc.stubhead())
    # Summary Rows --------------
    .tab_style(style.fill(next(c)), loc.grand_summary())
    .tab_style(style.fill(next(c)), loc.grand_summary_stub())
)
```

| title    |           |         |      |
|----------|-----------|---------|------|
| subtitle |           |         |      |
| stubhead | num       | spanner |      |
|          |           | char    | fctr |
| grp_a    |           |         |      |
| row_1    | 0.1111    | apricot | one  |
| row_2    | 2.222     | banana  | two  |
| grp_b    |           |         |      |
| row_5    | 5550.0    | None    | five |
| Total    | 5552.3331 | ---     | ---  |
| yo       |           |         |      |

Each color in the output maps to a specific table region, making it easy to identify the scope of every location specifier available in **Great Tables**.

This comprehensive example is useful as a reference, but in practice you would style only the parts that need visual distinction. The goal is to guide the reader's eye, not to color every region differently. Most tables benefit from styling just two or three regions (enough to create clear visual separation without overwhelming the content).

## Body

The table body is styled using [loc.body()](../reference/loc.body.md#great_tables.loc.body), which targets all data cells at once.

``` python
gt.tab_style(style.fill("yellow"), loc.body())
```

| title    |           |         |      |
|----------|-----------|---------|------|
| subtitle |           |         |      |
| stubhead | num       | spanner |      |
|          |           | char    | fctr |
| grp_a    |           |         |      |
| row_1    | 0.1111    | apricot | one  |
| row_2    | 2.222     | banana  | two  |
| grp_b    |           |         |      |
| row_5    | 5550.0    | None    | five |
| Total    | 5552.3331 | ---     | ---  |
| yo       |           |         |      |

The yellow fill is applied to every data cell in the table body, leaving headers, stubs, and footers unchanged.

## Column labels

Column labels can be styled broadly with [loc.column_header()](../reference/loc.column_header.md#great_tables.loc.column_header), or you can target individual column labels and spanner labels separately for more precise control.

``` python
(
    gt
    .tab_style(style.fill("yellow"), loc.column_header())
    .tab_style(style.fill("blue"), loc.column_labels(columns="num"))
    .tab_style(style.fill("red"), loc.spanner_labels(ids=["spanner"]))
)
```

| title    |           |         |      |
|----------|-----------|---------|------|
| subtitle |           |         |      |
| stubhead | num       | spanner |      |
|          |           | char    | fctr |
| grp_a    |           |         |      |
| row_1    | 0.1111    | apricot | one  |
| row_2    | 2.222     | banana  | two  |
| grp_b    |           |         |      |
| row_5    | 5550.0    | None    | five |
| Total    | 5552.3331 | ---     | ---  |
| yo       |           |         |      |

Here, [loc.column_header()](../reference/loc.column_header.md#great_tables.loc.column_header) applies a yellow background to the entire column labels row, then individual labels and spanners are overridden with more specific colors. This layered approach lets you set a base style and refine as needed.

## Header

The header area includes both the title and subtitle. You can style the entire header as one unit with [loc.header()](../reference/loc.header.md#great_tables.loc.header), or target the title and subtitle individually.

``` python
(
    gt.tab_style(style.fill("yellow"), loc.header())
    .tab_style(style.fill("blue"), loc.title())
    .tab_style(style.fill("red"), loc.subtitle())
)
```

| title    |           |         |      |
|----------|-----------|---------|------|
| subtitle |           |         |      |
| stubhead | num       | spanner |      |
|          |           | char    | fctr |
| grp_a    |           |         |      |
| row_1    | 0.1111    | apricot | one  |
| row_2    | 2.222     | banana  | two  |
| grp_b    |           |         |      |
| row_5    | 5550.0    | None    | five |
| Total    | 5552.3331 | ---     | ---  |
| yo       |           |         |      |

The yellow covers the full header area, while the blue and red target the title and subtitle independently. When styles overlap, the more specific location wins.

## Footer

The footer contains source notes and can be styled as a whole with [loc.footer()](../reference/loc.footer.md#great_tables.loc.footer) or at the individual source note level with [loc.source_notes()](../reference/loc.source_notes.md#great_tables.loc.source_notes).

``` python
(
    gt.tab_style(
        style.fill("yellow"),
        loc.source_notes(),
    ).tab_style(
        style.borders(weight="3px"),
        loc.footer(),
    )
)
```

| title    |           |         |      |
|----------|-----------|---------|------|
| subtitle |           |         |      |
| stubhead | num       | spanner |      |
|          |           | char    | fctr |
| grp_a    |           |         |      |
| row_1    | 0.1111    | apricot | one  |
| row_2    | 2.222     | banana  | two  |
| grp_b    |           |         |      |
| row_5    | 5550.0    | None    | five |
| Total    | 5552.3331 | ---     | ---  |
| yo       |           |         |      |

The source notes receive a yellow fill, while the entire footer region gets a heavy border. Both [loc.footer()](../reference/loc.footer.md#great_tables.loc.footer) and [loc.source_notes()](../reference/loc.source_notes.md#great_tables.loc.source_notes) target the same visual area but at different levels of granularity.

## Stub

The stub region includes row labels and row group labels. You can style these elements together or individually, and even target specific rows within the stub.

``` python
(
    gt.tab_style(style.fill("yellow"), loc.stub())
    .tab_style(style.fill("blue"), loc.row_groups())
    .tab_style(
        style.borders(style="dashed", weight="3px", color="red"),
        loc.stub(rows=[1]),
    )
)
```

| title    |           |         |      |
|----------|-----------|---------|------|
| subtitle |           |         |      |
| stubhead | num       | spanner |      |
|          |           | char    | fctr |
| grp_a    |           |         |      |
| row_1    | 0.1111    | apricot | one  |
| row_2    | 2.222     | banana  | two  |
| grp_b    |           |         |      |
| row_5    | 5550.0    | None    | five |
| Total    | 5552.3331 | ---     | ---  |
| yo       |           |         |      |

The stub fills yellow, row group labels turn blue, and a dashed red border highlights a specific row in the stub. Using `rows=` within [loc.stub()](../reference/loc.stub.md#great_tables.loc.stub) lets you target individual row labels.

## Stubhead

The stubhead label sits above the stub column and can be styled with [loc.stubhead()](../reference/loc.stubhead.md#great_tables.loc.stubhead).

``` python
gt.tab_style(style.fill("yellow"), loc.stubhead())
```

| title    |           |         |      |
|----------|-----------|---------|------|
| subtitle |           |         |      |
| stubhead | num       | spanner |      |
|          |           | char    | fctr |
| grp_a    |           |         |      |
| row_1    | 0.1111    | apricot | one  |
| row_2    | 2.222     | banana  | two  |
| grp_b    |           |         |      |
| row_5    | 5550.0    | None    | five |
| Total    | 5552.3331 | ---     | ---  |
| yo       |           |         |      |

The stubhead label cell receives the yellow background. This is useful for visually linking the stubhead to the stub column below it.

## Grand Summary Rows

Grand summary rows appear at the bottom of the table. You can style the summary data cells and the summary stub area independently.

``` python
(
    gt.tab_style(
        style.fill("yellow"),
        loc.grand_summary_stub(),
    ).tab_style(
        style.fill("lightblue"),
        loc.grand_summary(),
    )
)
```

| title    |           |         |      |
|----------|-----------|---------|------|
| subtitle |           |         |      |
| stubhead | num       | spanner |      |
|          |           | char    | fctr |
| grp_a    |           |         |      |
| row_1    | 0.1111    | apricot | one  |
| row_2    | 2.222     | banana  | two  |
| grp_b    |           |         |      |
| row_5    | 5550.0    | None    | five |
| Total    | 5552.3331 | ---     | ---  |
| yo       |           |         |      |

With [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) and the full set of `loc` specifiers, you can style every part of a **Great Tables** output. This gives you the ability to create cohesive visual themes, draw attention to specific structural elements, and ensure your table communicates effectively at every level.
