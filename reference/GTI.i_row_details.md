# GTI.i_row_details()

Let readers show more about each row, under it.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L1818-L1924)

``` python
GTI.i_row_details(content)
```

Each row with details gets a button (in its first cell) that shows them under the row, across the table, and hides them again; on a touch screen, tapping the row does too (with [`i_selection()`](../reference/GTI.i_selection.md#great_tables.GTI.i_selection), its checkbox selects it then). A row's details are a table (a [GT](../reference/GT.md#great_tables.GT) table, shown as it is on its own) or text ([html()](../reference/html.md#great_tables.md) or [md()](../reference/md.md#great_tables.md) text, or a string, shown as it is). They're made from `content=`: a function, which gets each row's values and returns the row's details, or the name of a column with each row's details in it, which is left out of the table. The info panel (from the (i) button in the control bar) has buttons that show and hide the details of every row.

The function gets a row's values as the data has them (not as they're formatted), as a dict of the data's column names to the row's values, with those of the columns the table hides (with [`cols_hide()`](../reference/GT.cols_hide.md#great_tables.GT.cols_hide)), so they can be what the details are made of. With `None` (or, in a column, a missing value or an empty string), a row has no details, and no button.

The details are made as the table is rendered, and are in its HTML, but aren't shown until a reader opens them (nor without the table's script running); they aren't searched, filtered, or exported. Open details follow their row as the rows are sorted, filtered and paged. They're shown apart from the page's styles (in a shadow root), so that a table in them looks as it does on its own, in the table's font and text color. Each [GT](../reference/GT.md#great_tables.GT) table has its own CSS, so a table with many of them in its rows' details is a larger page. In a table that drops columns to fit a narrow container (see [`i_responsive()`](../reference/GTI.i_responsive.md#great_tables.GTI.i_responsive)), the details are under the columns dropped from the row.

## Parameters

`content: Callable[[dict[str, Any]], Any] | str | None`  
A function that takes a row's values (a dict) and returns its details: a [GT](../reference/GT.md#great_tables.GT) table (not an interactive one), [html()](../reference/html.md#great_tables.md) or [md()](../reference/md.md#great_tables.md) text, a string, or `None` (no details). Or the name of a column with each row's details in it. With `None`, the rows have no details.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table of cars, each with a sentence about its engine under it, made from columns that the table hides.

``` python
from great_tables import GTI, md
from great_tables.data import gtcars

cars = gtcars[["mfr", "model", "year", "trim", "hp", "hp_rpm", "trq", "msrp"]].head(10)


def engine(row):
    return md(
        f"The **{row['trim']}** makes {row['hp']:.0f} hp at {row['hp_rpm']:,.0f} rpm, "
        f"and {row['trq']:.0f} lb-ft of torque."
    )


(
    GTI(cars, rowname_col="model")
    .cols_hide(columns=["trim", "hp", "hp_rpm", "trq"])
    .fmt_currency(columns="msrp", decimals=0)
    .i_row_details(engine)
)
```

|               | mfr     | year | msrp        |
|---------------|---------|------|-------------|
| GT            | Ford    | 2017 | \$447,000   |
| 458 Speciale  | Ferrari | 2015 | \$291,744   |
| 458 Spider    | Ferrari | 2015 | \$263,553   |
| 458 Italia    | Ferrari | 2014 | \$233,509   |
| 488 GTB       | Ferrari | 2016 | \$245,400   |
| California    | Ferrari | 2015 | \$198,973   |
| GTC4Lusso     | Ferrari | 2017 | \$298,000   |
| FF            | Ferrari | 2015 | \$295,000   |
| F12Berlinetta | Ferrari | 2015 | \$319,995   |
| LaFerrari     | Ferrari | 2015 | \$1,416,362 |

The **Base Coupe** makes 647 hp at 6,250 rpm, and 550 lb-ft of torque. The **Base Coupe** makes 597 hp at 9,000 rpm, and 398 lb-ft of torque. The **Base** makes 562 hp at 9,000 rpm, and 398 lb-ft of torque. The **Base Coupe** makes 562 hp at 9,000 rpm, and 398 lb-ft of torque. The **Base Coupe** makes 661 hp at 8,000 rpm, and 561 lb-ft of torque. The **Base Convertible** makes 553 hp at 7,500 rpm, and 557 lb-ft of torque. The **Base Coupe** makes 680 hp at 8,250 rpm, and 514 lb-ft of torque. The **Base Coupe** makes 652 hp at 8,000 rpm, and 504 lb-ft of torque. The **Base Coupe** makes 731 hp at 8,250 rpm, and 509 lb-ft of torque. The **Base Coupe** makes 949 hp at 9,000 rpm, and 664 lb-ft of torque.

A row's details can be a table of their own. Here, each of Ontario's ten largest municipalities has a table of its population at each census.

``` python
import pandas as pd
from great_tables import GT
from great_tables.data import towny

years = [1996, 2001, 2006, 2011, 2016, 2021]
counts = [f"population_{year}" for year in years]
largest = towny.nlargest(10, "population_2021")[["name", "status", *counts]]


def populations(row):
    census = pd.DataFrame({"census": years, "population": [row[c] for c in counts]})
    return (
        GT(census)
        .cols_label(census="Census", population="Population")
        .fmt_integer(columns="population")
    )


(
    GTI(largest, rowname_col="name")
    .cols_hide(columns=counts[:-1])
    .fmt_integer(columns="population_2021")
    .i_row_details(populations)
)
```

|             | status      | population_2021 |
|-------------|-------------|-----------------|
| Toronto     | single-tier | 2,794,356       |
| Ottawa      | single-tier | 1,017,449       |
| Mississauga | lower-tier  | 717,961         |
| Brampton    | lower-tier  | 656,480         |
| Hamilton    | single-tier | 569,353         |
| London      | single-tier | 422,324         |
| Markham     | lower-tier  | 338,503         |
| Vaughan     | lower-tier  | 323,103         |
| Kitchener   | lower-tier  | 256,885         |
| Windsor     | single-tier | 229,660         |

| Census | Population |
|--------|------------|
| 1996   | 2,385,421  |
| 2001   | 2,481,494  |
| 2006   | 2,503,281  |
| 2011   | 2,615,060  |
| 2016   | 2,731,571  |
| 2021   | 2,794,356  |

| Census | Population |
|--------|------------|
| 1996   | 721,136    |
| 2001   | 774,072    |
| 2006   | 812,129    |
| 2011   | 883,391    |
| 2016   | 934,243    |
| 2021   | 1,017,449  |

| Census | Population |
|--------|------------|
| 1996   | 544,382    |
| 2001   | 612,925    |
| 2006   | 668,599    |
| 2011   | 713,443    |
| 2016   | 721,599    |
| 2021   | 717,961    |

| Census | Population |
|--------|------------|
| 1996   | 268,251    |
| 2001   | 325,428    |
| 2006   | 433,806    |
| 2011   | 523,906    |
| 2016   | 593,638    |
| 2021   | 656,480    |

| Census | Population |
|--------|------------|
| 1996   | 467,799    |
| 2001   | 490,268    |
| 2006   | 504,559    |
| 2011   | 519,949    |
| 2016   | 536,917    |
| 2021   | 569,353    |

| Census | Population |
|--------|------------|
| 1996   | 325,699    |
| 2001   | 336,359    |
| 2006   | 352,395    |
| 2011   | 366,151    |
| 2016   | 383,822    |
| 2021   | 422,324    |

| Census | Population |
|--------|------------|
| 1996   | 173,383    |
| 2001   | 208,615    |
| 2006   | 261,573    |
| 2011   | 301,709    |
| 2016   | 328,966    |
| 2021   | 338,503    |

| Census | Population |
|--------|------------|
| 1996   | 132,549    |
| 2001   | 182,022    |
| 2006   | 238,866    |
| 2011   | 288,301    |
| 2016   | 306,233    |
| 2021   | 323,103    |

| Census | Population |
|--------|------------|
| 1996   | 178,420    |
| 2001   | 190,399    |
| 2006   | 204,668    |
| 2011   | 219,153    |
| 2016   | 233,222    |
| 2021   | 256,885    |

| Census | Population |
|--------|------------|
| 1996   | 197,694    |
| 2001   | 208,402    |
| 2006   | 216,473    |
| 2011   | 210,891    |
| 2016   | 217,188    |
| 2021   | 229,660    |
