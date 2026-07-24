# Great Tables is now BYODF (Bring Your Own DataFrame)

A few months ago, we released a [blog post](./polars-styling) about how much we loved the combination of Polars and Great Tables. We found that Polars lazy expression system opened up convenient ways to conditionally format tables for presentation. However, excited as we were, we were harboring a shameful secret: Great Tables enabled Polars as an optional dependency, but had a hard dependency on the alternative DataFrame library Pandas.

We're happy to share that [Great Tables](https://github.com/posit-dev/great-tables) v0.5.0 makes Pandas an optional dependency. Using Pandas DataFrames as inputs is still fully supported. The optional dependency simply allows users of one DataFrame library to not have to install the other.

In this post, I'll cover three important pieces:

- Where we are today on dependencies
- The challenge of removing hard dependencies
- How we made Pandas optional

This may seem over the top, but many DataFrame implementations exist in the Python world. Enabling folks to BYODF (Bring Your Own DataFrame) is a tricky, rewarding challenge!


# The state of Great Tables dependencies

Currently, Great Tables has two "sizes" of libraries it depends on:

- **Small**: utility libraries for things like datetime localization.
- **Big**: a lingering dependency on numpy in a few places (like nanoplots).

For small utilities, we depend on Babel, which makes it easier to say things like, "format this number as if I'm in Germany".

For big dependencies, numpy should be fairly straightforward to remove (see [this issue](https://github.com/posit-dev/great-tables/issues/296)). We also still rely on Pandas for datasets in `great_tables.data`, but we will remove it soon (see [this issue](https://github.com/posit-dev/great-tables/issues/91)).

Removing dependencies like numpy and Pandas helps people who are in restricted computing environments, want a more lightweight install, or who are stuck depending on a much earlier version of a package. It also helps us keep a clean separation of concerns. Without clear boundaries, it's too tempting to reach for things like `pd.isna()` in a pinch, or smear library specific versions of missingness across our code (e.g. `pd.NA`, `np.nan`, `polars.NullType`).


# The challenge of removing hard dependencies

Removing hard dependencies on DataFrame libraries is worthwhile, but requires special handling for all DataFrame specific actions. To illustrate consider the Great Tables output below, which is produced from a Pandas DataFrame:


``` python
import pandas as pd
import polars as pl
from great_tables import GT

df_pandas = pd.DataFrame({"x": ["a", "b"], "y": [1.01, 2.0]})
df_polars = pl.from_pandas(df_pandas)

GT(df_pandas)
```


<style>
#bjmhhcvojn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bjmhhcvojn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bjmhhcvojn p { margin: 0; padding: 0; }
 #bjmhhcvojn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bjmhhcvojn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bjmhhcvojn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bjmhhcvojn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bjmhhcvojn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bjmhhcvojn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bjmhhcvojn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bjmhhcvojn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bjmhhcvojn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bjmhhcvojn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bjmhhcvojn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bjmhhcvojn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bjmhhcvojn .gt_spanner_row { border-bottom-style: hidden; }
 #bjmhhcvojn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bjmhhcvojn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bjmhhcvojn .gt_from_md> :first-child { margin-top: 0; }
 #bjmhhcvojn .gt_from_md> :last-child { margin-bottom: 0; }
 #bjmhhcvojn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bjmhhcvojn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bjmhhcvojn .gt_indent_1 { text-indent: 5px; }
 #bjmhhcvojn .gt_indent_2 { text-indent: calc(5px * 2); }
 #bjmhhcvojn .gt_indent_3 { text-indent: calc(5px * 3); }
 #bjmhhcvojn .gt_indent_4 { text-indent: calc(5px * 4); }
 #bjmhhcvojn .gt_indent_5 { text-indent: calc(5px * 5); }
 #bjmhhcvojn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bjmhhcvojn .gt_row_group_first td { border-top-width: 2px; }
 #bjmhhcvojn .gt_row_group_first th { border-top-width: 2px; }
 #bjmhhcvojn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bjmhhcvojn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bjmhhcvojn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bjmhhcvojn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bjmhhcvojn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bjmhhcvojn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bjmhhcvojn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bjmhhcvojn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bjmhhcvojn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bjmhhcvojn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bjmhhcvojn .gt_left { text-align: left; }
 #bjmhhcvojn .gt_center { text-align: center; }
 #bjmhhcvojn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bjmhhcvojn .gt_font_normal { font-weight: normal; }
 #bjmhhcvojn .gt_font_bold { font-weight: bold; }
 #bjmhhcvojn .gt_font_italic { font-style: italic; }
 #bjmhhcvojn .gt_super { font-size: 65%; }
 #bjmhhcvojn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bjmhhcvojn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bjmhhcvojn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bjmhhcvojn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bjmhhcvojn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bjmhhcvojn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| x   | y    |
|-----|------|
| a   | 1.01 |
| b   | 2.0  |


Producing this table includes two actions on the DataFrame:

- **Get column names**: these are used for column labels (and other things).
- **Get column types**: these are used for alignment (e.g. numeric column is right aligned).

While these actions may seem simple, they require different methods for different DataFrame implementations. In this post, we'll focus specifically on the challenge of getting column names.


## Getting column names

The code below shows the different methods required to get column names as a list from Pandas and Polars.


``` python
df_pandas.columns.tolist()  # pandas
df_polars.columns           # polars
```


    ['x', 'y']


Notice that the two lines of code aren't too different--Pandas just requires an extra `.tolist()` piece. We could create a special function, that returns a list of names, depending on the type of the input DataFrame.


``` python
def get_column_names(data) -> list[str]:

    # pandas specific ----
    if isinstance(data, pd.DataFrame):
        return data.columns.tolist()

    # polars specific ----
    elif isinstance(data, pl.DataFrame):
        return data.columns

    raise TypeError(f"Unsupported type {type(data)}")
```


The function works great, in that we can call it on either DataFrame, but it lacks two things. The first is **dependency inversion**, since it requires importing both Pandas and Polars (creating a hard dependency). The second is **separation of concerns**, since Pandas and Polars code is mixed together. In this case adding more DataFrame implementations would create a hot stew of logic.


# How we made Pandas optional

We were able to make Pandas optional in a sane manner through two moves:

- [databackend](https://github.com/machow/databackend): perform `isinstance` checks without importing anything.
- singledispatch: split out functions like `get_column_names()` into DataFrame specific versions.


## Inverting dependency with databackend

Inverting dependency on DataFrame libraries means that we check whether something is a specific type of DataFrame, without using imports. This is done through the package `databackend`, which we copied into Great Tables.

It works by creating placeholder classes, which stand in for the DataFrames they're detecting:


``` python
from great_tables._databackend import AbstractBackend


class PdDataFrame(AbstractBackend):
    _backends = [("pandas", "DataFrame")]


class PlDataFrame(AbstractBackend):
    _backends = [("polars", "DataFrame")]


if isinstance(df_pandas, PdDataFrame):
    print("I'm a pandas DataFrame!!!")
```


    I'm a pandas DataFrame!!!


Note that the `PdDataFrame` above is able to detect a Pandas DataFrame without importing Pandas, by taking advantage of a bit of logic called a counterfactual:

- assumption: if `df_pandas` is a Pandas DataFrame, then Pandas has been imported.
- counterfactual: if Pandas has not been imported, then `df_pandas` is not a Pandas DataFrame.

This lets it quickly rule out a potential Pandas object by checking whether Pandas has been imported. Since this can be done by looking inside `sys.modules`, no imports are required. For more on this approach, see the [databackend README](https://github.com/machow/databackend).


## Separating concerns with singledispatch

While databackend removes dependencies, the use of singledispatch from the built-in `functools` module separates out the logic for handling Polars DataFrames from the logic for Pandas DataFrames. This makes it easier to think one DataFrame at a time, and also gets us better type hinting.

Here's a basic example, showing the `get_column_names()` function re-written using singledispatch:


``` python
from functools import singledispatch


# define the generic function ----
#
@singledispatch
def get_column_names(data) -> list[str]:
    raise TypeError(f"Unsupported type {type(data)}")


# register a pandas implementation on it ----
#
@get_column_names.register
def _(data: PdDataFrame):
    return data.columns.tolist()


# register a polars implementation on it ----
#
@get_column_names.register
def _(data: PlDataFrame):
    return data.columns
```


Note three important pieces:

- The initial `@singledispatch` decorates `def get_column_names(...)`. This creates a special "generic function", which can define DataFrame specific implementations.
- `@get_column_names.register` implements the Pandas DataFrame.
- The use of `PdDataFrame` is what signifies "run this for Pandas DataFrames".

With the `get_column_names` implementations defined, we can call it like a normal function:


``` python
get_column_names(df_pandas)  # pandas version
get_column_names(df_polars)  # polars version
```


    ['x', 'y']


For more on the benefits of singledispatch in data tooling, see the blog post [Single Dispatch for Data Science Tools](https://mchow.com/posts/2020-02-24-single-dispatch-data-science/). For the nitty gritty on our DataFrame processing, see the Great Tables [`_tbl_data.py` submodule](https://github.com/posit-dev/great-tables/blob/main/great_tables/_tbl_data.py).


# See you in the Polarsverse

This was a long diversion into the strategy behind supporting both Pandas and Polars, but the results are worth it. Users are able to bring their DataFrame of choice without the collective baggage of every DataFrame option.

For more on the special things you can do with Polars expressions, see these resources:

- [Guide: basic styling using Polars expressions](../../user-guide/styling-the-table-body.md#using-polars-expressions)
- [Post: Great Tables, the Polars DataFrame Styler of Your Dreams](../../blog/polars-styling/index.md)
- [The narwhals library](https://github.com/MarcoGorelli/narwhals): a neat library for running Polars expressions on Pandas DataFrames.

Hope you make some stylish, publication ready tables!
