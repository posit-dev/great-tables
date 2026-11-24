# GT.cols_label_rotate()

Rotate the column label for one or more columns.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_boxhead.py#L512-L645)

``` python
GT.cols_label_rotate(
    columns=None,
    dir="sideways-lr",
    align=None,
    padding=8,
)
```

The [cols_label_rotate()](../reference/GT.cols_label_rotate.md#great_tables.GT.cols_label_rotate) method sets the orientation of the column label text to make it flow vertically. The `dir` argument can be set to one of `"sideways-lr"`, `"sideways-rl"`, or `"vertical-lr"`, and the `columns` argument can be used to specify which columns to apply the alignment to. If `columns` is not specified, the alignment is applied to all columns.

A rotated label is kept on one line and centered across its column. Line breaks in a label made with [html()](../reference/html.md#great_tables.md) aren't supported, since Safari shows only the first line.

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list. If `None`, the alignment is applied to all columns.

`dir: Literal["sideways-lr", "sideways-rl", "vertical-lr"] = "sideways-lr"`  
A string that gives the direction of the text. Options: `"sideways-lr"`, `"sideways-rl"`, `"vertical-lr"`. See note for information on text layout.

`align: Literal["left", "center", "right"] | None = None`  
The alignment to apply along the height of the column labels row. Must be one of `"left"`, `"center"`, `"right"`, or `None`. `"left"` places the label where its text starts (the bottom for `"sideways-lr"`, the top otherwise), `"right"` where it ends, and `"center"` in the middle. With `None`, the label is placed at the bottom.

`padding: int = 8`  
The vertical padding to apply to the column labels.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

The example below rotates column labels such that the text is set to the left.

``` python
from great_tables import GT, style, loc, exibble

exibble_sm = exibble[["num", "fctr", "row", "group"]]

(
    GT(exibble_sm, rowname_col="row", groupname_col="group")
    .cols_label_rotate(columns=["num", "fctr"])
)
```

|       | num       | fctr  |
|-------|-----------|-------|
| grp_a |           |       |
| row_1 | 0.1111    | one   |
| row_2 | 2.222     | two   |
| row_3 | 33.33     | three |
| row_4 | 444.4     | four  |
| grp_b |           |       |
| row_5 | 5550.0    | five  |
| row_6 | None      | six   |
| row_7 | 777000.0  | seven |
| row_8 | 8880000.0 | eight |

Other styles you provide won't override the column label rotation directives. Here we set the text to the right.

``` python
(
    GT(exibble_sm, rowname_col="row", groupname_col="group")
    .cols_label_rotate(columns=["num", "fctr"], dir="vertical-lr")
    .tab_style(style=style.text(weight="bold"), locations=loc.column_labels(["fctr"]))
)
```

|       | num       | fctr  |
|-------|-----------|-------|
| grp_a |           |       |
| row_1 | 0.1111    | one   |
| row_2 | 2.222     | two   |
| row_3 | 33.33     | three |
| row_4 | 444.4     | four  |
| grp_b |           |       |
| row_5 | 5550.0    | five  |
| row_6 | None      | six   |
| row_7 | 777000.0  | seven |
| row_8 | 8880000.0 | eight |

A long label makes the column labels row taller, since a rotated label isn't wrapped. The `align=` argument places a shorter label along that height. Here `"center"` puts the `num` label in the middle.

``` python
(
    GT(exibble_sm, rowname_col="row", groupname_col="group")
    .cols_label({"fctr": "A longer description of the values"})
    .cols_label_rotate(columns="fctr")
    .cols_label_rotate(columns="num", align="center")
)
```

|       | num       | A longer description of the values |
|-------|-----------|------------------------------------|
| grp_a |           |                                    |
| row_1 | 0.1111    | one                                |
| row_2 | 2.222     | two                                |
| row_3 | 33.33     | three                              |
| row_4 | 444.4     | four                               |
| grp_b |           |                                    |
| row_5 | 5550.0    | five                               |
| row_6 | None      | six                                |
| row_7 | 777000.0  | seven                              |
| row_8 | 8880000.0 | eight                              |

## Note

The `dir` parameter uses the following keywords to alter the direction of the column label text.

##### `"sideways-lr"`

For ltr scripts, content flows vertically from bottom to top. For rtl scripts, content flows vertically from top to bottom. Characters are set sideways toward the left. Overflow lines are appended to the right.

##### `"sideways-rl"`

For ltr scripts, content flows vertically from top to bottom. For rtl scripts, content flows vertically from bottom to top. Characters are set sideways toward the right. Overflow lines are appended to the left.

##### `"vertical-lr"`

Identical to `"sideways-rl"`, but overflow lines are appended to the right.
