from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Any

if TYPE_CHECKING:
    from .gt import GT


def pipe(self: "GT", func: Callable[..., "GT"], *args: Any, **kwargs: Any) -> "GT":
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
    Let's use the "name", "land_area_km2," and "density_2021" columns of the `towny` dataset to
    create a table. First, we'll demonstrate using two consecutive calls to the `.tab_style()`
    method to highlight the maximum value of the "land_area_km2" column with "lightgray" and the
    maximum value of the "density_2021" column with "lightblue".

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


def pipes(self: "GT", *funcs: Callable["GT", "GT"] | list[Callable["GT", "GT"]]) -> "GT":
    """
    Provide a structured way to chain functions for a GT object.

    This function accepts multiple functions, each of which receives a GT object and returns a GT
    object. This allows users to easily integrate functions into the chained API offered by
    **Great Tables**. It serves as a helper function for chaining multiple functions at once.

    Parameters
    ----------
    *funcs
        Multiple functions or a list of functions, each receiving a GT object and returning a GT
        object.

    Returns
    -------
    gt
        A GT object.

    Examples:
    ------
    Let's use the "name", "land_area_km2," and "density_2021" columns of the `towny` dataset to
    create a table. First, we'll demonstrate using two consecutive calls to the `.tab_style()`
    method to highlight the maximum value of the "land_area_km2" column with "lightgray" and the
    maximum value of the "density_2021" column with "lightblue".

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

    Next, we'll demonstrate achieving the same result using the `.pipes()` method to
    programmatically style each column. You might find leveraging `partial` to bind the other
    parameters in advance handy.

    ```{python}
    from functools import partial


    columns = ["land_area_km2", "density_2021"]
    colors = ["lightgray", "lightblue"]


    def tbl_style(gtbl: GT, column: str, color: str) -> GT:
        return gtbl.tab_style(
            style=style.fill(color=color),
            locations=loc.body(columns=column, rows=pl.col(column).eq(pl.col(column).max())),
        )


    (
        GT(
            towny_mini[["name", "land_area_km2", "density_2021"]],
            rowname_col="name",
        ).pipes(
            *[partial(tbl_style, column=column, color=color)
              for column, color in zip(columns, colors)]
        )
    )
    ```

    Alternatively, you can collect all the functions in a list like this:

    ```{python}
    (
        GT(
            towny_mini[["name", "land_area_km2", "density_2021"]],
            rowname_col="name",
        ).pipes(
            [partial(tbl_style, column=column, color=color)
             for column, color in zip(columns, colors)]
        )
    )
    ```
    """
    if isinstance(funcs[0], list) and len(funcs) == 1:
        funcs = funcs[0]
    for func in funcs:
        self = pipe(self, func)
    return self
