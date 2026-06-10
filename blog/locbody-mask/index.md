# Style Table Body with `mask=` in [loc.body()](../../reference/loc.body.md#great_tables.loc.body)

In Great Tables `0.16.0`, we introduced the `mask=` parameter in [loc.body()](../../reference/loc.body.md#great_tables.loc.body), enabling users to apply conditional styling to rows on a per-column basis more efficiently when working with a Polars DataFrame. This post will demonstrate how it works and compare it with the "old-fashioned" approach:

- **Leveraging the `mask=` parameter in [loc.body()](../../reference/loc.body.md#great_tables.loc.body):** Use Polars expressions for streamlined styling.
- **Utilizing the `locations=` parameter in [GT.tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style):** Pass a list of [loc.body()](../../reference/loc.body.md#great_tables.loc.body) objects.

Let's dive in.


## Preparations

We'll use the built-in dataset [gtcars](../../reference/data.gtcars.md#great_tables.data.gtcars) to create a Polars DataFrame. Next, we'll select the columns `mfr`, `drivetrain`, `year`, and `hp` to create a small pivoted table named `df_mini`. Finally, we'll pass `df_mini` to the [GT](../../reference/GT.md#great_tables.GT) object to create a table named `gt`, using `drivetrain` as the `rowname_col=` and `mfr` as the `groupname_col=`, as shown below:


Show the Code

``` python
import polars as pl
from great_tables import GT, loc, style
from great_tables.data import gtcars
from polars import selectors as cs

year_cols = ["2014", "2015", "2016", "2017"]
df_mini = (
    pl.from_pandas(gtcars)
    .filter(pl.col("mfr").is_in(["Ferrari", "Lamborghini", "BMW"]))
    .sort("drivetrain")
    .pivot(on="year", index=["mfr", "drivetrain"], values="hp", aggregate_function="mean")
    .select(["mfr", "drivetrain", *year_cols])
)

gt = GT(df_mini).tab_stub(rowname_col="drivetrain", groupname_col="mfr").opt_stylize(color="cyan")
gt
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="2014" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2014</th>
<th id="2015" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2015</th>
<th id="2016" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2016</th>
<th id="2017" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2017</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="5" class="gt_group_heading">Ferrari</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">680.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">562.0</td>
<td class="gt_row gt_right gt_striped">678.4</td>
<td class="gt_row gt_right gt_striped">661.0</td>
<td class="gt_row gt_right gt_striped">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">Lamborghini</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">700.0</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">550.0</td>
<td class="gt_row gt_right gt_striped">610.0</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">BMW</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">357.0</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">465.0</td>
<td class="gt_row gt_right gt_striped">None</td>
</tr>
</tbody>
</table>


The numbers in the cells represent the average horsepower for each combination of `mfr` and `drivetrain` for a specific year.


## Leveraging the `mask=` parameter in [loc.body()](../../reference/loc.body.md#great_tables.loc.body)

The `mask=` parameter in [loc.body()](../../reference/loc.body.md#great_tables.loc.body) accepts a Polars expression that evaluates to a boolean result for each cell.

Here's how we can use it to achieve the two goals:

- Highlight the cell text in red if the column datatype is numerical and the cell value exceeds 650.
- Fill the background color as lightgrey if the cell value is missing in the last two columns (`2016` and `2017`).


``` python
(
    gt.tab_style(
        style=style.text(color="red"),
        locations=loc.body(mask=cs.numeric().gt(650))
    ).tab_style(
        style=style.fill(color="lightgrey"),
        locations=loc.body(mask=pl.nth(-2, -1).is_null()),
    )
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="2014" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2014</th>
<th id="2015" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2015</th>
<th id="2016" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2016</th>
<th id="2017" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2017</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="5" class="gt_group_heading">Ferrari</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right" style="color: red">652.0</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
<td class="gt_row gt_right" style="color: red">680.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">562.0</td>
<td class="gt_row gt_right gt_striped" style="color: red">678.4</td>
<td class="gt_row gt_right gt_striped" style="color: red">661.0</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">Lamborghini</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right" style="color: red">700.0</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">550.0</td>
<td class="gt_row gt_right gt_striped">610.0</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">BMW</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">357.0</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">rwd</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">465.0</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
</tr>
</tbody>
</table>


In this example:

- `cs.numeric()` targets numerical columns, and `.gt(650)` checks if the cell value is greater than 650.
- `pl.nth(-2, -1)` targets the last two columns, and `.is_null()` identifies missing values.

Did you notice that we can use Polars selectors and expressions to dynamically identify columns at runtime? This is definitely a killer feature when working with pivoted operations.

The `mask=` parameter acts as a syntactic sugar, streamlining the process and removing the need to loop through columns manually.

> **Warning: Using `mask=` Independently**
>
> `mask=` should not be used in combination with the [columns](../../reference/loc.body.md#great_tables.loc.body.columns) or [rows](../../reference/loc.stub.md#great_tables.loc.stub.rows) arguments. Attempting to do so will raise a `ValueError`.


## Utilizing the `locations=` parameter in [GT.tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style)

A more "old-fashioned" approach involves passing a list of [loc.body()](../../reference/loc.body.md#great_tables.loc.body) objects to the `locations=` parameter in [GT.tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style):


``` python
(
    gt.tab_style(
        style=style.text(color="red"),
        locations=[loc.body(columns=col, rows=pl.col(col).gt(650))
                   for col in year_cols],
    ).tab_style(
        style=style.fill(color="lightgrey"),
        locations=[loc.body(columns=col, rows=pl.col(col).is_null())
                   for col in year_cols[-2:]],
    )
)
```


This approach, though functional, demands additional effort:

- Explicitly preparing the column names in advance.
- Specifying the `columns=` and `rows=` arguments for each [loc.body()](../../reference/loc.body.md#great_tables.loc.body) in the loop.

While effective, it is less efficient and more verbose compared to the first approach.


## Wrapping up

With the introduction of the `mask=` parameter in [loc.body()](../../reference/loc.body.md#great_tables.loc.body), users can now style the table body in a more vectorized-like manner, akin to using `df.apply()` in Pandas, enhancing the overall user experience.

We extend our gratitude to [<span class="citation" cites="igorcalabria">@igorcalabria</span>](https://github.com/igorcalabria) for suggesting this feature in [\#389](https://github.com/posit-dev/great-tables/issues/389) and providing an insightful explanation of its utility. A special thanks to [<span class="citation" cites="henryharbeck">@henryharbeck</span>](https://github.com/henryharbeck) for providing the second approach.

We hope you enjoy this new functionality as much as we do! Have ideas to make Great Tables even better? Share them with us via [GitHub Issues](https://github.com/posit-dev/great-tables/issues). We're always amazed by the creativity of our users! See you, until the next great table.
