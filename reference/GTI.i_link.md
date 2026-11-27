# GTI.i_link()

Link the table to others on the page, so that the rows selected in one filter the others.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L1933-L2014)

``` python
GTI.i_link(
    group,
    on=None,
)
```

Tables with the same `group=` are linked by their `on=` column, which each of them has in its data (it can be a hidden one). When a reader selects rows in one of them (which [`i_selection()`](../reference/GTI.i_selection.md#great_tables.GTI.i_selection) lets them do), each of the others shows only its rows whose value in that column is one of the selected rows' values; clearing the selection shows them all again. A row with a missing value in the column isn't linked to any. A table whose rows can't be selected is only filtered, and tables whose rows can be filter each other (but not themselves). The tables link in the browser, without a server: in a Quarto document, a notebook (but not across the frames some show each cell's output in, as Colab does), or an HTML page with the tables in it.

A table filtered by another's selection says so in its control bar, with a token ("Selected in Makes: Ferrari, Lamborghini") that shows the rows again (until the selection changes), and in its info panel. The tables are named after their titles (see [`tab_header()`](../reference/GT.tab_header.md#great_tables.GT.tab_header)), or else their IDs. The filter is on top of the table's own search and filters, and isn't part of its view: it isn't kept with the view (see [`i_view_state()`](../reference/GTI.i_view_state.md#great_tables.GTI.i_view_state)), undone, or in the code an export copies.

## Parameters

`group: str | None`  
The name of the tables' group: tables with the same one are linked. With `None`, the table isn't linked.

`on: str | None = None`  
The column of the table's data whose values link its rows to those of the others in the group (each of which has a column of that name).

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here are two tables of cars, one of their makes and one of the cars themselves, linked by the make. Select some makes in the first, and the second shows only their cars.

``` python
from great_tables import GTI
from great_tables.data import gtcars

cars = gtcars[["mfr", "model", "year", "hp", "msrp"]]
makes = cars.groupby("mfr", as_index=False).agg(models=("model", "count"))

(
    GTI(makes, rowname_col="mfr")
    .tab_header(title="Makes")
    .i_selection("multiple")
    .i_link("cars", on="mfr")
)
```

| Makes         |        |
|---------------|--------|
|               | models |
| Acura         | 1      |
| Aston Martin  | 4      |
| Audi          | 5      |
| BMW           | 5      |
| Bentley       | 1      |
| Chevrolet     | 1      |
| Dodge         | 1      |
| Ferrari       | 9      |
| Ford          | 1      |
| Jaguar        | 1      |
| Lamborghini   | 3      |
| Lotus         | 1      |
| Maserati      | 3      |
| McLaren       | 1      |
| Mercedes-Benz | 2      |
| Nissan        | 1      |
| Porsche       | 4      |
| Rolls-Royce   | 2      |
| Tesla         | 1      |

``` python
(
    GTI(cars, rowname_col="model")
    .tab_header(title="Cars")
    .fmt_integer(columns=["year", "hp"], use_seps=False)
    .fmt_currency(columns="msrp", decimals=0)
    .i_link("cars", on="mfr")
)
```

| Cars           |               |      |     |             |
|----------------|---------------|------|-----|-------------|
|                | mfr           | year | hp  | msrp        |
| GT             | Ford          | 2017 | 647 | \$447,000   |
| 458 Speciale   | Ferrari       | 2015 | 597 | \$291,744   |
| 458 Spider     | Ferrari       | 2015 | 562 | \$263,553   |
| 458 Italia     | Ferrari       | 2014 | 562 | \$233,509   |
| 488 GTB        | Ferrari       | 2016 | 661 | \$245,400   |
| California     | Ferrari       | 2015 | 553 | \$198,973   |
| GTC4Lusso      | Ferrari       | 2017 | 680 | \$298,000   |
| FF             | Ferrari       | 2015 | 652 | \$295,000   |
| F12Berlinetta  | Ferrari       | 2015 | 731 | \$319,995   |
| LaFerrari      | Ferrari       | 2015 | 949 | \$1,416,362 |
| NSX            | Acura         | 2017 | 573 | \$156,000   |
| GT-R           | Nissan        | 2016 | 545 | \$101,770   |
| Aventador      | Lamborghini   | 2015 | 700 | \$397,500   |
| Huracan        | Lamborghini   | 2015 | 610 | \$237,250   |
| Gallardo       | Lamborghini   | 2014 | 550 | \$191,900   |
| Continental GT | Bentley       | 2016 | 500 | \$198,500   |
| Granturismo    | Maserati      | 2016 | 454 | \$132,825   |
| Quattroporte   | Maserati      | 2016 | 404 | \$99,900    |
| Ghibli         | Maserati      | 2016 | 345 | \$70,600    |
| 6-Series       | BMW           | 2016 | 315 | \$77,300    |
| i8             | BMW           | 2016 | 357 | \$140,700   |
| M4             | BMW           | 2016 | 425 | \$65,700    |
| M5             | BMW           | 2016 | 560 | \$94,100    |
| M6             | BMW           | 2016 | 560 | \$113,400   |
| DB11           | Aston Martin  | 2017 | 608 | \$211,195   |
| Rapide S       | Aston Martin  | 2016 | 552 | \$205,300   |
| Vanquish       | Aston Martin  | 2016 | 568 | \$287,250   |
| Vantage        | Aston Martin  | 2016 | 430 | \$103,300   |
| Corvette       | Chevrolet     | 2016 | 650 | \$88,345    |
| Viper          | Dodge         | 2017 | 645 | \$95,895    |
| R8             | Audi          | 2015 | 430 | \$115,900   |
| RS 7           | Audi          | 2016 | 560 | \$108,900   |
| S6             | Audi          | 2016 | 450 | \$70,900    |
| S7             | Audi          | 2016 | 450 | \$82,900    |
| S8             | Audi          | 2016 | 520 | \$114,900   |
| Evora          | Lotus         | 2017 | 400 | \$91,900    |
| F-Type         | Jaguar        | 2016 | 340 | \$65,000    |
| AMG GT         | Mercedes-Benz | 2016 | 503 | \$129,900   |
| SL-Class       | Mercedes-Benz | 2016 | 329 | \$85,050    |
| Model S        | Tesla         | 2017 | 259 | \$74,500    |
| 718 Boxster    | Porsche       | 2017 | 300 | \$56,000    |
| 718 Cayman     | Porsche       | 2017 | 300 | \$53,900    |
| 911            | Porsche       | 2016 | 350 | \$84,300    |
| Panamera       | Porsche       | 2016 | 310 | \$78,100    |
| 570            | McLaren       | 2016 | 570 | \$184,900   |
| Dawn           | Rolls-Royce   | 2016 | 563 | \$335,000   |
| Wraith         | Rolls-Royce   | 2016 | 624 | \$304,350   |
