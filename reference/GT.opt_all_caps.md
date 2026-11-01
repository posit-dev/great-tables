# GT.opt_all_caps()

Option to use all caps in select table locations.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_options.py#L1142-L1310)

``` python
GT.opt_all_caps(
    all_caps=True,
    locations=None,
)
```

Sometimes an all-capitalized look is suitable for a table. By using [opt_all_caps()](../reference/GT.opt_all_caps.md#great_tables.GT.opt_all_caps), we can transform characters in the column labels, the stub, and in all row groups in this way (and there's control over which of these locations are transformed). This method serves as a convenient shortcut for `tab_options(<location>_text_transform="uppercase", <location>_font_size="80%", <location>_font_weight="bolder")` (for all `locations` selected).

## Parameters

`all_caps: bool = True`  
Indicates whether the text transformation to all caps should be performed (`True`, the default) or reset to default values (`False`) for the `locations` targeted.

`locations: (     type[LocColumnLabels | LocRowGroups | LocStub]     | list[type[LocColumnLabels | LocRowGroups | LocStub]]     | str     | list[str]     | None ) = None`  
Which locations should undergo this text transformation? By default it includes all of the [loc.column_labels](../reference/loc.column_labels.md#great_tables.loc.column_labels), the [loc.stub](../reference/loc.stub.md#great_tables.loc.stub), and the [loc.row_groups](../reference/loc.row_groups.md#great_tables.loc.row_groups) locations. However, we could just choose one or two of those.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using select columns from the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll ensure that all text in the column labels, the stub, and in all row groups is transformed to all caps using the [opt_all_caps()](../reference/GT.opt_all_caps.md#great_tables.GT.opt_all_caps) method.

``` python
from great_tables import GT, exibble, loc, md

(
  GT(
    exibble[["num", "char", "currency", "row", "group"]],
    rowname_col="row",
    groupname_col="group"
  )
  .tab_header(
    title=md("Data listing from **exibble**"),
    subtitle=md("`exibble` is a **Great Tables** dataset.")
  )
  .fmt_number(columns="num")
  .fmt_currency(columns="currency")
  .tab_source_note(source_note="This is only a subset of the dataset.")
  .opt_all_caps()
)
```

| Data listing from **exibble** |  |  |  |
|----|----|----|----|
| `exibble` is a **Great Tables** dataset. |  |  |  |
|  | num | char | currency |
| grp_a |  |  |  |
| row_1 | 0.11 | apricot | \$49.95 |
| row_2 | 2.22 | banana | \$17.95 |
| row_3 | 33.33 | coconut | \$1.39 |
| row_4 | 444.40 | durian | \$65,100.00 |
| grp_b |  |  |  |
| row_5 | 5,550.00 | None | \$1,325.81 |
| row_6 | None | fig | \$13.26 |
| row_7 | 777,000.00 | grapefruit | None |
| row_8 | 8,880,000.00 | honeydew | \$0.44 |
| This is only a subset of the dataset. |  |  |  |

[opt_all_caps()](../reference/GT.opt_all_caps.md#great_tables.GT.opt_all_caps) accepts a `locations` parameter that allows us to specify which components should be transformed. For example, if we only want to ensure that all text in the stub and all row groups is converted to all caps:

``` python
(
  GT(
    exibble[["num", "char", "currency", "row", "group"]],
    rowname_col="row",
    groupname_col="group"
  )
  .tab_header(
    title=md("Data listing from **exibble**"),
    subtitle=md("`exibble` is a **Great Tables** dataset.")
  )
  .fmt_number(columns="num")
  .fmt_currency(columns="currency")
  .tab_source_note(source_note="This is only a subset of the dataset.")
  .opt_all_caps(locations=[loc.stub, loc.row_groups])
)
```

| Data listing from **exibble** |  |  |  |
|----|----|----|----|
| `exibble` is a **Great Tables** dataset. |  |  |  |
|  | num | char | currency |
| grp_a |  |  |  |
| row_1 | 0.11 | apricot | \$49.95 |
| row_2 | 2.22 | banana | \$17.95 |
| row_3 | 33.33 | coconut | \$1.39 |
| row_4 | 444.40 | durian | \$65,100.00 |
| grp_b |  |  |  |
| row_5 | 5,550.00 | None | \$1,325.81 |
| row_6 | None | fig | \$13.26 |
| row_7 | 777,000.00 | grapefruit | None |
| row_8 | 8,880,000.00 | honeydew | \$0.44 |
| This is only a subset of the dataset. |  |  |  |
