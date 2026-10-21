# GT.tab_style_body()

Apply styles to body cells based on their data values.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_tab_create_modify.py#L156-L417)

``` python
GT.tab_style_body(
    style,
    columns=None,
    rows=None,
    values=None,
    pattern=None,
    fn=None,
    targets="cell",
    extents="body",
)
```

With [tab_style_body()](../reference/GT.tab_style_body.md#great_tables.GT.tab_style_body), we can target body cells for styling based on the *values* they contain rather than their positions. Three matching strategies are available: exact value matching (`values=`), regular-expression matching (`pattern=`), and arbitrary predicate functions (`fn=`). When more than one of these is supplied, the precedence is `fn` \> `pattern` \> `values`.

After matching cells are identified the styling can optionally be expanded to entire rows or columns via `targets=`, and projected into the stub region via `extents=`.

## Parameters

`style: CellStyle | list[CellStyle]`  
The styles to apply to matched cells. Use the [style.text()](../reference/style.text.md#great_tables.style.text), [style.fill()](../reference/style.fill.md#great_tables.style.fill), [style.borders()](../reference/style.borders.md#great_tables.style.borders), and [style.css()](../reference/style.css.md#great_tables.style.css) classes to define styles.

`columns: SelectExpr = None`  
The columns to consider for matching. Can be a single column name, a list of column names, or a column selection expression. By default, all columns in the body are considered.

`rows: RowSelectExpr = None`  
The rows to consider for matching. Can be a single row index or name, a list of row indices or names, or a row selection expression. By default, all rows are considered.

`values: list[Any] | None = None`  
A list of specific values to match against. A body cell whose value equals any element in this list will be styled. Ignored when `pattern` or `fn` is supplied.

`pattern: str | None = None`  
A regex pattern string. Body cells whose *string representation* matches this pattern will be styled. Takes precedence over `values`; ignored when `fn` is supplied.

`fn: Callable[[Any], bool] | None = None`  
A function that receives a cell's raw value and returns `True` (style the cell) or `False` (skip). This is the most flexible matching option and takes the highest precedence.

`targets: Literal["cell", "row", "column"] | list[Literal["cell", "row", "column"]] = "cell"`  
How to expand matched cells. `"cell"` (the default) styles only matched cells; `"row"` styles the entire row of each match; `"column"` styles the entire column. A list can combine these (e.g., `["cell", "row"]`).

`extents: Literal["body", "stub"] | list[Literal["body", "stub"]] = "body"`  
Where styling is applied. `"body"` (the default) styles only body cells; `"stub"` also projects the styling into the stub (row labels). A list can combine these (e.g., `["body", "stub"]`).

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Use [tab_style_body()](../reference/GT.tab_style_body.md#great_tables.GT.tab_style_body) to highlight specific values in a table. Here we color the background of cells that contain the values `49.95` or `33.33`.

``` python
from great_tables import GT, style, exibble

(
    GT(exibble, rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=style.fill(color="orange"),
        values=[49.95, 33.33],
    )
)
```

|       | num       | char       | fctr  | date       | time  | datetime         | currency |
|-------|-----------|------------|-------|------------|-------|------------------|----------|
| grp_a |           |            |       |            |       |                  |          |
| row_1 | 0.1111    | apricot    | one   | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95    |
| row_2 | 2.222     | banana     | two   | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95    |
| row_3 | 33.33     | coconut    | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39     |
| row_4 | 444.4     | durian     | four  | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0  |
| grp_b |           |            |       |            |       |                  |          |
| row_5 | 5550.0    | None       | five  | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81  |
| row_6 | None      | fig        | six   | 2015-06-15 | None  | 2018-06-06 16:11 | 13.255   |
| row_7 | 777000.0  | grapefruit | seven | None       | 19:10 | 2018-07-07 05:22 | None     |
| row_8 | 8880000.0 | honeydew   | eight | 2015-08-15 | 20:20 | None             | 0.44     |

Apply multiple styles to matched cells using a list of style objects.

``` python
from great_tables import GT, style, exibble

(
    GT(exibble, rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=[
            style.text(color="white", weight="bold"),
            style.fill(color="red"),
        ],
        values=[49.95, 33.33],
    )
)
```

|       | num       | char       | fctr  | date       | time  | datetime         | currency |
|-------|-----------|------------|-------|------------|-------|------------------|----------|
| grp_a |           |            |       |            |       |                  |          |
| row_1 | 0.1111    | apricot    | one   | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95    |
| row_2 | 2.222     | banana     | two   | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95    |
| row_3 | 33.33     | coconut    | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39     |
| row_4 | 444.4     | durian     | four  | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0  |
| grp_b |           |            |       |            |       |                  |          |
| row_5 | 5550.0    | None       | five  | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81  |
| row_6 | None      | fig        | six   | 2015-06-15 | None  | 2018-06-06 16:11 | 13.255   |
| row_7 | 777000.0  | grapefruit | seven | None       | 19:10 | 2018-07-07 05:22 | None     |
| row_8 | 8880000.0 | honeydew   | eight | 2015-08-15 | 20:20 | None             | 0.44     |

A predicate function (`fn=`) provides the most flexible matching. Below we style all numeric cells with a value between 0 and 50.

``` python
from great_tables import GT, style, exibble

(
    GT(exibble, rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=style.fill(color="pink"),
        fn=lambda x: isinstance(x, (int, float)) and 0 <= x < 50,
    )
)
```

|       | num       | char       | fctr  | date       | time  | datetime         | currency |
|-------|-----------|------------|-------|------------|-------|------------------|----------|
| grp_a |           |            |       |            |       |                  |          |
| row_1 | 0.1111    | apricot    | one   | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95    |
| row_2 | 2.222     | banana     | two   | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95    |
| row_3 | 33.33     | coconut    | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39     |
| row_4 | 444.4     | durian     | four  | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0  |
| grp_b |           |            |       |            |       |                  |          |
| row_5 | 5550.0    | None       | five  | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81  |
| row_6 | None      | fig        | six   | 2015-06-15 | None  | 2018-06-06 16:11 | 13.255   |
| row_7 | 777000.0  | grapefruit | seven | None       | 19:10 | 2018-07-07 05:22 | None     |
| row_8 | 8880000.0 | honeydew   | eight | 2015-08-15 | 20:20 | None             | 0.44     |

Use `pattern=` to target cells by regex. This matches any cell whose string value contains "ne" or "na".

``` python
from great_tables import GT, style, exibble

(
    GT(exibble, rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=style.fill(color="green"),
        pattern="ne|na",
    )
)
```

|       | num       | char       | fctr  | date       | time  | datetime         | currency |
|-------|-----------|------------|-------|------------|-------|------------------|----------|
| grp_a |           |            |       |            |       |                  |          |
| row_1 | 0.1111    | apricot    | one   | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95    |
| row_2 | 2.222     | banana     | two   | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95    |
| row_3 | 33.33     | coconut    | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39     |
| row_4 | 444.4     | durian     | four  | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0  |
| grp_b |           |            |       |            |       |                  |          |
| row_5 | 5550.0    | None       | five  | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81  |
| row_6 | None      | fig        | six   | 2015-06-15 | None  | 2018-06-06 16:11 | 13.255   |
| row_7 | 777000.0  | grapefruit | seven | None       | 19:10 | 2018-07-07 05:22 | None     |
| row_8 | 8880000.0 | honeydew   | eight | 2015-08-15 | 20:20 | None             | 0.44     |

Expand the styling to entire rows using `targets="row"`, and project into the stub with `extents=["body", "stub"]`.

``` python
from great_tables import GT, style, exibble

(
    GT(exibble, rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=style.fill(color="lightblue"),
        values=[49.95],
        targets="row",
        extents=["body", "stub"],
    )
)
```

|       | num       | char       | fctr  | date       | time  | datetime         | currency |
|-------|-----------|------------|-------|------------|-------|------------------|----------|
| grp_a |           |            |       |            |       |                  |          |
| row_1 | 0.1111    | apricot    | one   | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95    |
| row_2 | 2.222     | banana     | two   | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95    |
| row_3 | 33.33     | coconut    | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39     |
| row_4 | 444.4     | durian     | four  | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0  |
| grp_b |           |            |       |            |       |                  |          |
| row_5 | 5550.0    | None       | five  | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81  |
| row_6 | None      | fig        | six   | 2015-06-15 | None  | 2018-06-06 16:11 | 13.255   |
| row_7 | 777000.0  | grapefruit | seven | None       | 19:10 | 2018-07-07 05:22 | None     |
| row_8 | 8880000.0 | honeydew   | eight | 2015-08-15 | 20:20 | None             | 0.44     |
