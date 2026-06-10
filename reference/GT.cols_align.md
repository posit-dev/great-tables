## GT.cols_align()


Set the alignment of one or more columns.


Usage

``` python
GT.cols_align(
    align="left",
    columns=None,
)
```


The [cols_align()](GT.cols_align.md#great_tables.GT.cols_align) method sets the alignment of one or more columns. The [align](style.text.md#great_tables.style.text.align) argument can be set to one of `"left"`, `"center"`, or `"right"` and the [columns](loc.body.md#great_tables.loc.body.columns) argument can be used to specify which columns to apply the alignment to. If [columns](loc.body.md#great_tables.loc.body.columns) is not specified, the alignment is applied to all columns.


## Parameters


`align: str = ``"left"`  
The alignment to apply. Must be one of `"left"`, `"center"`, or `"right"`.

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list. If `None`, the alignment is applied to all columns.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [countrypops](data.countrypops.md#great_tables.data.countrypops) to create a small table. We can change the alignment of the `population` column with [cols_align()](GT.cols_align.md#great_tables.GT.cols_align). In this example, the column label and body cells of `population` will be aligned to the left.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "San Marino"][
    ["country_name", "year", "population"]
].tail(5)

(
    GT(countrypops_mini, rowname_col="year", groupname_col="country_name")
    .cols_align(align="left", columns="population")
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="population" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">population</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading">San Marino</th>
</tr>

<tr>
<th class="gt_row gt_left gt_stub">2018</th>
<td class="gt_row gt_left">34156</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">2019</th>
<td class="gt_row gt_left">34178</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">2020</th>
<td class="gt_row gt_left">34007</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">2021</th>
<td class="gt_row gt_left">33745</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">2022</th>
<td class="gt_row gt_left">33660</td>
</tr>
</tbody>
</table>
