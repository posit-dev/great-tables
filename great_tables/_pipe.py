from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from typing_extensions import Concatenate, ParamSpec

if TYPE_CHECKING:
    from .gt import GT


P = ParamSpec("P")


def pipe(
    self: "GT", func: Callable[Concatenate["GT", P], "GT"], *args: P.args, **kwargs: P.kwargs
) -> "GT":
    """
    Provide a structured way to chain a function for a GT object.

    This function accepts a function that receives a GT object along with optional positional and
    keyword arguments, returning a GT object. This allows users to easily integrate a function
    into the chained API offered by **Great Tables**.

    Parameters
    ----------
    func
        A function that receives a GT object along with optional positional and keyword arguments,
        returning a GT object.

    *args
        Optional positional arguments to be passed to the function.

    **kwargs
        Optional keyword arguments to be passed to the function.

    Returns
    -------
    gt
        A GT object.

    Examples:
    ------
    Let's use the `name`, `land_area_km2`, and `density_2021` columns of the `towny` dataset to
    create a table. First, we'll demonstrate using two consecutive calls to the `.tab_style()`
    method to highlight the maximum value of the `land_area_km2` column with `"lightgray"` and the
    maximum value of the `density_2021` column with `"lightblue"`.

    ```{python}
    import polars as pl
    from great_tables import GT, loc, style
    from great_tables.data import towny


    towny_mini = pl.from_pandas(towny).head(10)

    (
        GT(
            towny_mini[["name", "land_area_km2", "density_2021"]],
            rowname_col="name",
        )
        .tab_style(
            style=style.fill(color="lightgray"),
            locations=loc.body(
                columns="land_area_km2",
                rows=pl.col("land_area_km2").eq(pl.col("land_area_km2").max()),
            ),
        )
        .tab_style(
            style=style.fill(color="lightblue"),
            locations=loc.body(
                columns="density_2021",
                rows=pl.col("density_2021").eq(pl.col("density_2021").max()),
            ),
        )
    )
    ```

    Next, we'll demonstrate how to achieve the same result using the `.pipe()` method to
    programmatically style each column.

    ```{python}
    columns = ["land_area_km2", "density_2021"]
    colors = ["lightgray", "lightblue"]


    def tbl_style(gtbl: GT, columns: list[str], colors: list[str]) -> GT:
        for column, color in zip(columns, colors):
            gtbl = gtbl.tab_style(
                style=style.fill(color=color),
                locations=loc.body(columns=column, rows=pl.col(column).eq(pl.col(column).max())),
            )
        return gtbl


    (
        GT(
            towny_mini[["name", "land_area_km2", "density_2021"]],
            rowname_col="name",
        ).pipe(tbl_style, columns, colors)
    )
    ```
    """
    return func(self, *args, **kwargs)
