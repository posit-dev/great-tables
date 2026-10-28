# GT.tab_spanner_delim()

Insert spanners by splitting column names with a delimiter.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_spanners.py#L346-L466)

``` python
GT.tab_spanner_delim(
    delim=".",
    columns=None,
    split="last",
    limit=-1,
    reverse=False,
)
```

This generates one or more spanners (and sets column labels), by splitting the column name by the specified delimiter text (delim) and placing the fragments from top to bottom (i.e., higher-level spanners to the column labels) or vice versa.

For example, the three side-by-side column names rating_1, rating_2, and rating_3 will by default produce a spanner labeled "rating" above columns labeled "1", "2", and "3".

## Parameters

`delim: str = "."`  
Delimiter for splitting, default to `"."`.

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`split: Literal["first", "last"] = "last"`  
Should the delimiter splitting occur from the "last" instance of the delim character or from the "first"? The default here uses the "last" keyword, and splitting begins at the last instance of the delimiter in the column name. This option only has some consequence when there is a limit value applied that is lesser than the number of delimiter characters for a given column name (i.e., number of splits is not the maximum possible number).

`limit: int = -1`  
Limit for splitting. An optional limit to place on the splitting procedure. The default -1 means that a column name will be split as many times are there are delimiter characters. In other words, the default means there is no limit. If an integer value is given to limit then splitting will cease at the iteration given by limit. This works in tandem with split since we can adjust the number of splits from either the right side (split = "last") or left side (split = "first") of the column name.

`reverse: bool = False`  
Should the order of split names be reversed? By default, this is `False`.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's create a table table that includes the column names province.NL_ZH.pop, province.NL_ZH.gdp, province.NL_NH.pop, and province.NL_NH.gdp, we can see that we have a naming system that has a well-defined structure. We start with the more general to the left ("province") and move to the more specific on the right ("pop"). If the columns are in the table in this exact order, then things are in an ideal state as the eventual spanner labels will form from this neighboring. When using tab_spanner_delim() here with delim set as "." we get the following table:

``` python
import polars as pl
import polars.selectors as cs
from great_tables import GT

data = {
    "province.NL_ZH.pop": [1, 2, 3],
    "province.NL_ZH.gdp": [4, 5, 6],
    "province.NL_NH.pop": [7, 8, 9],
    "province.NL_NH.gdp": [10, 11, 12],
}

gt = GT(pl.DataFrame(data))
gt.tab_spanner_delim()
```

| province |     |       |     |
|----------|-----|-------|-----|
| NL_ZH    |     | NL_NH |     |
| pop      | gdp | pop   | gdp |
| 1        | 4   | 7     | 10  |
| 2        | 5   | 8     | 11  |
| 3        | 6   | 9     | 12  |

``` python
gt.tab_spanner_delim(limit=1)
```

| province.NL_ZH |     | province.NL_NH |     |
|----------------|-----|----------------|-----|
| pop            | gdp | pop            | gdp |
| 1              | 4   | 7              | 10  |
| 2              | 5   | 8              | 11  |
| 3              | 6   | 9              | 12  |

``` python
# the name "province" repeats in the styled table,
# because the first spanner is column names
gt.tab_spanner_delim(reverse=True)
```

| pop      | gdp      | pop      | gdp      |
|----------|----------|----------|----------|
| NL_ZH    |          | NL_NH    |          |
| province | province | province | province |
| 1        | 4        | 7        | 10       |
| 2        | 5        | 8        | 11       |
| 3        | 6        | 9        | 12       |

``` python
from great_tables.data import towny

lil_towny = (
    pl.DataFrame(towny)
    .select("name", cs.starts_with("population"))
    .head()
)

GT(lil_towny).tab_spanner_delim(delim="_")
```

| name                | population |       |       |        |        |        |
|---------------------|------------|-------|-------|--------|--------|--------|
|                     | 1996       | 2001  | 2006  | 2011   | 2016   | 2021   |
| Addington Highlands | 2429       | 2402  | 2512  | 2517   | 2318   | 2534   |
| Adelaide Metcalfe   | 3128       | 3149  | 3135  | 3028   | 2990   | 3011   |
| Adjala-Tosorontio   | 9359       | 10082 | 10695 | 10603  | 10975  | 10989  |
| Admaston/Bromley    | 2837       | 2824  | 2716  | 2844   | 2935   | 2995   |
| Ajax                | 64430      | 73753 | 90167 | 109600 | 119677 | 126666 |
