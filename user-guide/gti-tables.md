# GTI Tables

When readers need more than [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive) gives them (see [Making Tables Interactive](interactive-tables.md)), make the table a [GTI](../reference/GTI.md#great_tables.GTI) table. Here, the `Make` column gets a list of its values to choose from and `HP` a range, the table is first shown with the most powerful cars at the top, and readers can download the rows they've filtered as CSV.

``` python
import polars as pl
from great_tables import GTI, data

gtcars_pl = data.pl.gtcars.select(["mfr", "model", "year", "hp", "trq", "msrp"])

(
    GTI(gtcars_pl)
    .tab_header(title="GT Cars: as a GTI table")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .i_cols_filter(columns="mfr", type="facet")
    .i_cols_filter(columns="hp")
    .i_view(sort="-hp")
    .i_export("csv")
)
```

| GT Cars: as a GTI table |                |      |     |        |                |
|-------------------------|----------------|------|-----|--------|----------------|
| Make                    | Model          | Year | HP  | Torque | MSRP           |
| Ford                    | GT             | 2017 | 647 | 550    | \$447,000.00   |
| Ferrari                 | 458 Speciale   | 2015 | 597 | 398    | \$291,744.00   |
| Ferrari                 | 458 Spider     | 2015 | 562 | 398    | \$263,553.00   |
| Ferrari                 | 458 Italia     | 2014 | 562 | 398    | \$233,509.00   |
| Ferrari                 | 488 GTB        | 2016 | 661 | 561    | \$245,400.00   |
| Ferrari                 | California     | 2015 | 553 | 557    | \$198,973.00   |
| Ferrari                 | GTC4Lusso      | 2017 | 680 | 514    | \$298,000.00   |
| Ferrari                 | FF             | 2015 | 652 | 504    | \$295,000.00   |
| Ferrari                 | F12Berlinetta  | 2015 | 731 | 509    | \$319,995.00   |
| Ferrari                 | LaFerrari      | 2015 | 949 | 664    | \$1,416,362.00 |
| Acura                   | NSX            | 2017 | 573 | 476    | \$156,000.00   |
| Nissan                  | GT-R           | 2016 | 545 | 436    | \$101,770.00   |
| Lamborghini             | Aventador      | 2015 | 700 | 507    | \$397,500.00   |
| Lamborghini             | Huracan        | 2015 | 610 | 413    | \$237,250.00   |
| Lamborghini             | Gallardo       | 2014 | 550 | 398    | \$191,900.00   |
| Bentley                 | Continental GT | 2016 | 500 | 487    | \$198,500.00   |
| Maserati                | Granturismo    | 2016 | 454 | 384    | \$132,825.00   |
| Maserati                | Quattroporte   | 2016 | 404 | 406    | \$99,900.00    |
| Maserati                | Ghibli         | 2016 | 345 | 369    | \$70,600.00    |
| BMW                     | 6-Series       | 2016 | 315 | 330    | \$77,300.00    |
| BMW                     | i8             | 2016 | 357 | 420    | \$140,700.00   |
| BMW                     | M4             | 2016 | 425 | 406    | \$65,700.00    |
| BMW                     | M5             | 2016 | 560 | 500    | \$94,100.00    |
| BMW                     | M6             | 2016 | 560 | 500    | \$113,400.00   |
| Aston Martin            | DB11           | 2017 | 608 | 516    | \$211,195.00   |
| Aston Martin            | Rapide S       | 2016 | 552 | 465    | \$205,300.00   |
| Aston Martin            | Vanquish       | 2016 | 568 | 465    | \$287,250.00   |
| Aston Martin            | Vantage        | 2016 | 430 | 361    | \$103,300.00   |
| Chevrolet               | Corvette       | 2016 | 650 | 650    | \$88,345.00    |
| Dodge                   | Viper          | 2017 | 645 | 600    | \$95,895.00    |
| Audi                    | R8             | 2015 | 430 | 317    | \$115,900.00   |
| Audi                    | RS 7           | 2016 | 560 | 516    | \$108,900.00   |
| Audi                    | S6             | 2016 | 450 | 406    | \$70,900.00    |
| Audi                    | S7             | 2016 | 450 | 406    | \$82,900.00    |
| Audi                    | S8             | 2016 | 520 | 481    | \$114,900.00   |
| Lotus                   | Evora          | 2017 | 400 | 302    | \$91,900.00    |
| Jaguar                  | F-Type         | 2016 | 340 | 332    | \$65,000.00    |
| Mercedes-Benz           | AMG GT         | 2016 | 503 | 479    | \$129,900.00   |
| Mercedes-Benz           | SL-Class       | 2016 | 329 | 354    | \$85,050.00    |
| Tesla                   | Model S        | 2017 | 259 | 243    | \$74,500.00    |
| Porsche                 | 718 Boxster    | 2017 | 300 | 280    | \$56,000.00    |
| Porsche                 | 718 Cayman     | 2017 | 300 | 280    | \$53,900.00    |
| Porsche                 | 911            | 2016 | 350 | 287    | \$84,300.00    |
| Porsche                 | Panamera       | 2016 | 310 | 295    | \$78,100.00    |
| McLaren                 | 570            | 2016 | 570 | 443    | \$184,900.00   |
| Rolls-Royce             | Dawn           | 2016 | 563 | 575    | \$335,000.00   |
| Rolls-Royce             | Wraith         | 2016 | 624 | 590    | \$304,350.00   |

A table you've already made with [GT()](../reference/GT.md#great_tables.GT), including one with [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive), becomes a [GTI](../reference/GTI.md#great_tables.GTI) table with [GTI.from_gt()](../reference/GTI.from_gt.md#great_tables.GTI.from_gt), keeping what [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive) set. Each of the `i_` methods has examples on its reference page (e.g., [i_cols_filter()](../reference/GTI.i_cols_filter.md#great_tables.GTI.i_cols_filter)), and the [API Reference](../reference/index.md#interactive-table-controls) has them all.

## The parts of a [GTI](../reference/GTI.md#great_tables.GTI) table

A [GTI](../reference/GTI.md#great_tables.GTI) table is the table GT made, with a few parts added around it. Here they are in teal, on a table that's filtered by `mfr`, sorted by `hp` and scrolls within a set height:

![A GTI table with its parts labelled. The table GT made (its column labels and body) is in gray; the parts GTI adds are in teal: the status line, column controls, column profiles, row numbers, height handle, filter tokens, and the control bar with its search, keyboard shortcuts, page controls and counter, filters as text, panels, and undo and redo.](../assets/gti_parts_of_a_table.light.svg)

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cG9seWxpbmUgcG9pbnRzPSIxNSAzIDIxIDMgMjEgOSI+PC9wb2x5bGluZT48cG9seWxpbmUgcG9pbnRzPSI5IDIxIDMgMjEgMyAxNSI+PC9wb2x5bGluZT48bGluZSB4MT0iMjEiIHkxPSIzIiB4Mj0iMTQiIHkyPSIxMCI+PC9saW5lPjxsaW5lIHgxPSIzIiB5MT0iMjEiIHgyPSIxMCIgeTI9IjE0Ij48L2xpbmU+PC9zdmc+)

From the top:

- The **status line**, just above the table, says what the data is and how much of it is shown ("Polars DataFrame · 12 of 47 rows × 4 columns"). It's there with [i_inspect()](../reference/GTI.i_inspect.md#great_tables.GTI.i_inspect) (and in an explorer). In a table made with `opt_interactive(use_search=True)`, the search box is here too.
- The **column controls**, under each column label: the column's dtype (with [i_inspect()](../reference/GTI.i_inspect.md#great_tables.GTI.i_inspect)), its sort arrows (with [i_sorting()](../reference/GTI.i_sorting.md#great_tables.GTI.i_sorting), on by default), and its filter button (with [i_cols_filter()](../reference/GTI.i_cols_filter.md#great_tables.GTI.i_cols_filter)).
- The **column profiles**, under the labels of the columns [i_cols_profile()](../reference/GTI.i_cols_profile.md#great_tables.GTI.i_cols_profile) chose: a small plot of how their values are spread.
- The **row numbers**, at the start of each row (with [i_inspect()](../reference/GTI.i_inspect.md#great_tables.GTI.i_inspect)), which stay with the rows as they're sorted and filtered. A DataFrame's rows are numbered from 0, as its index is, and a DuckDB relation's or an Ibis table's from 1, as a database numbers them; `row_start=` in [i_inspect()](../reference/GTI.i_inspect.md#great_tables.GTI.i_inspect) sets either one.
- The **height handle**, at the foot of a body that scrolls (with [i_scroll()](../reference/GTI.i_scroll.md#great_tables.GTI.i_scroll)), dragged for a taller or shorter body.
- The **filter tokens**, one for each filter the rows are filtered by, which say what it keeps; a token's ✕ removes its filter.
- The **control bar**, just below the table, which brings together what readers can do with the table as a whole. From its left, it has:
  - the **search** (with [i_search()](../reference/GTI.i_search.md#great_tables.GTI.i_search), on by default) and the table's **keyboard shortcuts**
  - the **page controls**, around the **page counter** ("1 / 2"), which can be clicked to type a page to go to
  - the **filters as text** button (`{ }`, in a table with filters), which opens the filters as a query to edit, in the form [i_view()](../reference/GTI.i_view.md#great_tables.GTI.i_view) takes them (with `filter=`)
  - the buttons that open the table's **panels**: its columns, grouping its rows and exporting them (when the table has these), and its info
  - **undo and redo** (with [i_view_state()](../reference/GTI.i_view_state.md#great_tables.GTI.i_view_state)), and a **Reset** button once the view has changed

A table made with [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive) has a **pager** below it instead of the control bar: its page buttons, and the number of rows shown.

The status line and the control bar are close to the table, and the space that GT (or the page) leaves around the table is kept past them, so that they read as part of it rather than of the text around it.

## Row details

With [i_row_details()](../reference/GTI.i_row_details.md#great_tables.GTI.i_row_details), each row can have more to show under it, when the reader asks for it. A function makes a row's details from its values (including those of columns the table hides): as text, with [md()](../reference/md.md#great_tables.md) or [html()](../reference/html.md#great_tables.md), or as a [GT](../reference/GT.md#great_tables.GT) table of their own. Here, each car has a few lines about its engine. Click the arrow by a car's name to show them, or use **Expand all** in the table's info panel to show every car's.

``` python
from great_tables import md


def engine(row):
    economy = (
        "" if row["mpg_c"] is None else f" It gets {row['mpg_c']:.0f} mpg in the city, "
        f"and {row['mpg_h']:.0f} on the highway."
    )
    return md(
        f"The **{row['trim']}** ({row['bdy_style']}, {row['drivetrain'].upper()}) makes "
        f"{row['hp']:.0f} hp at {row['hp_rpm']:,.0f} rpm, and {row['trq']:.0f} lb-ft of torque."
        f"{economy}"
    )


(
    GTI(data.pl.gtcars, rowname_col="model")
    .tab_header(title="GT Cars: with row details")
    .cols_hide(
        columns=["trim", "bdy_style", "hp_rpm", "trq_rpm", "mpg_c", "mpg_h", "drivetrain", "trsmn"]
    )
    .cols_label(mfr="Make", year="Year", hp="HP", trq="Torque", ctry_origin="Country", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp", decimals=0)
    .i_row_details(engine)
)
```

| GT Cars: with row details |  |  |  |  |  |  |
|----|----|----|----|----|----|----|
|  | Make | Year | HP | Torque | Country | MSRP |
| GT | Ford | 2017 | 647 | 550 | United States | \$447,000 |
| 458 Speciale | Ferrari | 2015 | 597 | 398 | Italy | \$291,744 |
| 458 Spider | Ferrari | 2015 | 562 | 398 | Italy | \$263,553 |
| 458 Italia | Ferrari | 2014 | 562 | 398 | Italy | \$233,509 |
| 488 GTB | Ferrari | 2016 | 661 | 561 | Italy | \$245,400 |
| California | Ferrari | 2015 | 553 | 557 | Italy | \$198,973 |
| GTC4Lusso | Ferrari | 2017 | 680 | 514 | Italy | \$298,000 |
| FF | Ferrari | 2015 | 652 | 504 | Italy | \$295,000 |
| F12Berlinetta | Ferrari | 2015 | 731 | 509 | Italy | \$319,995 |
| LaFerrari | Ferrari | 2015 | 949 | 664 | Italy | \$1,416,362 |
| NSX | Acura | 2017 | 573 | 476 | Japan | \$156,000 |
| GT-R | Nissan | 2016 | 545 | 436 | Japan | \$101,770 |
| Aventador | Lamborghini | 2015 | 700 | 507 | Italy | \$397,500 |
| Huracan | Lamborghini | 2015 | 610 | 413 | Italy | \$237,250 |
| Gallardo | Lamborghini | 2014 | 550 | 398 | Italy | \$191,900 |
| Continental GT | Bentley | 2016 | 500 | 487 | United Kingdom | \$198,500 |
| Granturismo | Maserati | 2016 | 454 | 384 | Italy | \$132,825 |
| Quattroporte | Maserati | 2016 | 404 | 406 | Italy | \$99,900 |
| Ghibli | Maserati | 2016 | 345 | 369 | Italy | \$70,600 |
| 6-Series | BMW | 2016 | 315 | 330 | Germany | \$77,300 |
| i8 | BMW | 2016 | 357 | 420 | Germany | \$140,700 |
| M4 | BMW | 2016 | 425 | 406 | Germany | \$65,700 |
| M5 | BMW | 2016 | 560 | 500 | Germany | \$94,100 |
| M6 | BMW | 2016 | 560 | 500 | Germany | \$113,400 |
| DB11 | Aston Martin | 2017 | 608 | 516 | United Kingdom | \$211,195 |
| Rapide S | Aston Martin | 2016 | 552 | 465 | United Kingdom | \$205,300 |
| Vanquish | Aston Martin | 2016 | 568 | 465 | United Kingdom | \$287,250 |
| Vantage | Aston Martin | 2016 | 430 | 361 | United Kingdom | \$103,300 |
| Corvette | Chevrolet | 2016 | 650 | 650 | United States | \$88,345 |
| Viper | Dodge | 2017 | 645 | 600 | United States | \$95,895 |
| R8 | Audi | 2015 | 430 | 317 | Germany | \$115,900 |
| RS 7 | Audi | 2016 | 560 | 516 | Germany | \$108,900 |
| S6 | Audi | 2016 | 450 | 406 | Germany | \$70,900 |
| S7 | Audi | 2016 | 450 | 406 | Germany | \$82,900 |
| S8 | Audi | 2016 | 520 | 481 | Germany | \$114,900 |
| Evora | Lotus | 2017 | 400 | 302 | United Kingdom | \$91,900 |
| F-Type | Jaguar | 2016 | 340 | 332 | United Kingdom | \$65,000 |
| AMG GT | Mercedes-Benz | 2016 | 503 | 479 | Germany | \$129,900 |
| SL-Class | Mercedes-Benz | 2016 | 329 | 354 | Germany | \$85,050 |
| Model S | Tesla | 2017 | 259 | 243 | United States | \$74,500 |
| 718 Boxster | Porsche | 2017 | 300 | 280 | Germany | \$56,000 |
| 718 Cayman | Porsche | 2017 | 300 | 280 | Germany | \$53,900 |
| 911 | Porsche | 2016 | 350 | 287 | Germany | \$84,300 |
| Panamera | Porsche | 2016 | 310 | 295 | Germany | \$78,100 |
| 570 | McLaren | 2016 | 570 | 443 | United Kingdom | \$184,900 |
| Dawn | Rolls-Royce | 2016 | 563 | 575 | United Kingdom | \$335,000 |
| Wraith | Rolls-Royce | 2016 | 624 | 590 | United Kingdom | \$304,350 |

The **Base Coupe** (coupe, RWD) makes 647 hp at 6,250 rpm, and 550 lb-ft of torque. It gets 11 mpg in the city, and 18 on the highway. The **Base Coupe** (coupe, RWD) makes 597 hp at 9,000 rpm, and 398 lb-ft of torque. It gets 13 mpg in the city, and 17 on the highway. The **Base** (convertible, RWD) makes 562 hp at 9,000 rpm, and 398 lb-ft of torque. It gets 13 mpg in the city, and 17 on the highway. The **Base Coupe** (coupe, RWD) makes 562 hp at 9,000 rpm, and 398 lb-ft of torque. It gets 13 mpg in the city, and 17 on the highway. The **Base Coupe** (coupe, RWD) makes 661 hp at 8,000 rpm, and 561 lb-ft of torque. It gets 15 mpg in the city, and 22 on the highway. The **Base Convertible** (convertible, RWD) makes 553 hp at 7,500 rpm, and 557 lb-ft of torque. It gets 16 mpg in the city, and 23 on the highway. The **Base Coupe** (coupe, AWD) makes 680 hp at 8,250 rpm, and 514 lb-ft of torque. It gets 12 mpg in the city, and 17 on the highway. The **Base Coupe** (coupe, AWD) makes 652 hp at 8,000 rpm, and 504 lb-ft of torque. It gets 11 mpg in the city, and 16 on the highway. The **Base Coupe** (coupe, RWD) makes 731 hp at 8,250 rpm, and 509 lb-ft of torque. It gets 11 mpg in the city, and 16 on the highway. The **Base Coupe** (coupe, RWD) makes 949 hp at 9,000 rpm, and 664 lb-ft of torque. It gets 12 mpg in the city, and 16 on the highway. The **Base Coupe** (coupe, AWD) makes 573 hp at 6,500 rpm, and 476 lb-ft of torque. It gets 21 mpg in the city, and 22 on the highway. The **Premium Coupe** (coupe, AWD) makes 545 hp at 6,400 rpm, and 436 lb-ft of torque. It gets 16 mpg in the city, and 22 on the highway. The **LP 700-4 Coupe** (coupe, AWD) makes 700 hp at 8,250 rpm, and 507 lb-ft of torque. It gets 11 mpg in the city, and 18 on the highway. The **LP 610-4 Coupe** (coupe, RWD) makes 610 hp at 8,250 rpm, and 413 lb-ft of torque. It gets 16 mpg in the city, and 20 on the highway. The **LP 550-2 Coupe** (coupe, RWD) makes 550 hp at 8,000 rpm, and 398 lb-ft of torque. It gets 12 mpg in the city, and 20 on the highway. The **V8 Coupe** (coupe, AWD) makes 500 hp at 6,000 rpm, and 487 lb-ft of torque. It gets 15 mpg in the city, and 25 on the highway. The **Sport Coupe** (coupe, RWD) makes 454 hp at 7,600 rpm, and 384 lb-ft of torque. It gets 13 mpg in the city, and 21 on the highway. The **S Sedan** (sedan, RWD) makes 404 hp at 5,500 rpm, and 406 lb-ft of torque. It gets 16 mpg in the city, and 23 on the highway. The **Base Sedan** (sedan, RWD) makes 345 hp at 5,250 rpm, and 369 lb-ft of torque. It gets 17 mpg in the city, and 24 on the highway. The **640 I Coupe** (coupe, RWD) makes 315 hp at 5,800 rpm, and 330 lb-ft of torque. It gets 20 mpg in the city, and 30 on the highway. The **Mega World Coupe** (coupe, AWD) makes 357 hp at 5,800 rpm, and 420 lb-ft of torque. It gets 28 mpg in the city, and 29 on the highway. The **Base Coupe** (coupe, RWD) makes 425 hp at 5,500 rpm, and 406 lb-ft of torque. It gets 17 mpg in the city, and 24 on the highway. The **Base Sedan** (sedan, RWD) makes 560 hp at 6,000 rpm, and 500 lb-ft of torque. It gets 15 mpg in the city, and 22 on the highway. The **Base Coupe** (coupe, RWD) makes 560 hp at 6,000 rpm, and 500 lb-ft of torque. It gets 15 mpg in the city, and 22 on the highway. The **Base Coupe** (coupe, RWD) makes 608 hp at 6,500 rpm, and 516 lb-ft of torque. It gets 15 mpg in the city, and 21 on the highway. The **Base Sedan** (sedan, RWD) makes 552 hp at 6,650 rpm, and 465 lb-ft of torque. It gets 14 mpg in the city, and 21 on the highway. The **Base Coupe** (coupe, RWD) makes 568 hp at 6,650 rpm, and 465 lb-ft of torque. It gets 13 mpg in the city, and 21 on the highway. The **V8 GT (Manual) Coupe** (coupe, RWD) makes 430 hp at 7,300 rpm, and 361 lb-ft of torque. It gets 13 mpg in the city, and 19 on the highway. The **Z06 Coupe** (coupe, RWD) makes 650 hp at 6,400 rpm, and 650 lb-ft of torque. It gets 15 mpg in the city, and 22 on the highway. The **GT Coupe** (coupe, RWD) makes 645 hp at 5,000 rpm, and 600 lb-ft of torque. It gets 12 mpg in the city, and 19 on the highway. The **4.2 (Manual) Coupe** (coupe, AWD) makes 430 hp at 7,900 rpm, and 317 lb-ft of torque. It gets 11 mpg in the city, and 20 on the highway. The **Quattro Hatchback** (hatchback, AWD) makes 560 hp at 5,700 rpm, and 516 lb-ft of torque. It gets 15 mpg in the city, and 25 on the highway. The **Premium Plus quattro Sedan** (sedan, AWD) makes 450 hp at 5,800 rpm, and 406 lb-ft of torque. It gets 18 mpg in the city, and 27 on the highway. The **Prestige quattro Hatchback** (hatchback, AWD) makes 450 hp at 5,800 rpm, and 406 lb-ft of torque. It gets 17 mpg in the city, and 27 on the highway. The **Base Sedan** (sedan, AWD) makes 520 hp at 5,800 rpm, and 481 lb-ft of torque. It gets 15 mpg in the city, and 25 on the highway. The **2+2 Coupe** (coupe, RWD) makes 400 hp at 7,000 rpm, and 302 lb-ft of torque. It gets 16 mpg in the city, and 24 on the highway. The **Base (Manual) Coupe** (coupe, RWD) makes 340 hp at 6,500 rpm, and 332 lb-ft of torque. It gets 16 mpg in the city, and 24 on the highway. The **S Coupe** (coupe, RWD) makes 503 hp at 6,250 rpm, and 479 lb-ft of torque. It gets 16 mpg in the city, and 22 on the highway. The **SL400 Convertible** (convertible, RWD) makes 329 hp at 5,250 rpm, and 354 lb-ft of torque. It gets 20 mpg in the city, and 27 on the highway. The **75D** (sedan, AWD) makes 259 hp at 6,100 rpm, and 243 lb-ft of torque. The **Base Convertible** (convertible, RWD) makes 300 hp at 6,500 rpm, and 280 lb-ft of torque. It gets 21 mpg in the city, and 28 on the highway. The **Base Coupe** (coupe, RWD) makes 300 hp at 6,500 rpm, and 280 lb-ft of torque. It gets 20 mpg in the city, and 29 on the highway. The **Carrera Coupe** (coupe, RWD) makes 350 hp at 7,400 rpm, and 287 lb-ft of torque. It gets 20 mpg in the city, and 28 on the highway. The **Base Sedan** (sedan, RWD) makes 310 hp at 6,200 rpm, and 295 lb-ft of torque. It gets 18 mpg in the city, and 28 on the highway. The **Base Coupe** (coupe, RWD) makes 570 hp at 7,500 rpm, and 443 lb-ft of torque. It gets 16 mpg in the city, and 23 on the highway. The **Base Convertible** (convertible, RWD) makes 563 hp at 5,250 rpm, and 575 lb-ft of torque. It gets 12 mpg in the city, and 19 on the highway. The **Base Coupe** (coupe, RWD) makes 624 hp at 5,600 rpm, and 590 lb-ft of torque. It gets 13 mpg in the city, and 21 on the highway.

The details are in the table's HTML, made as it's rendered, but aren't searched, filtered or exported (and each [GT](../reference/GT.md#great_tables.GT) table in them brings its own CSS, so many of them make a larger page). A column can hold them instead, with each row's details: [i_row_details()](../reference/GTI.i_row_details.md#great_tables.GTI.i_row_details) takes its name, and the column is then left out of the table.

## Column profiles

With [i_cols_profile()](../reference/GTI.i_cols_profile.md#great_tables.GTI.i_cols_profile), columns get a small plot under their labels of how their values are spread: a histogram of numbers and dates, and bars for the most common values of the others, each with the share of rows that have a missing value. The plots follow the rows a search or filter keeps, so they show at a glance what's left. Here, choose a few makes in the `Make` filter and watch the horsepower and prices narrow; point at a bar to see its values and its number of rows.

``` python
(
    GTI(gtcars_pl)
    .tab_header(title="GT Cars: with column profiles")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp", decimals=0)
    .i_cols_filter(columns="mfr", type="facet")
    .i_cols_profile(columns=["mfr", "year", "hp", "msrp"])
)
```

| GT Cars: with column profiles |                |      |     |        |             |
|-------------------------------|----------------|------|-----|--------|-------------|
| Make                          | Model          | Year | HP  | Torque | MSRP        |
| Ford                          | GT             | 2017 | 647 | 550    | \$447,000   |
| Ferrari                       | 458 Speciale   | 2015 | 597 | 398    | \$291,744   |
| Ferrari                       | 458 Spider     | 2015 | 562 | 398    | \$263,553   |
| Ferrari                       | 458 Italia     | 2014 | 562 | 398    | \$233,509   |
| Ferrari                       | 488 GTB        | 2016 | 661 | 561    | \$245,400   |
| Ferrari                       | California     | 2015 | 553 | 557    | \$198,973   |
| Ferrari                       | GTC4Lusso      | 2017 | 680 | 514    | \$298,000   |
| Ferrari                       | FF             | 2015 | 652 | 504    | \$295,000   |
| Ferrari                       | F12Berlinetta  | 2015 | 731 | 509    | \$319,995   |
| Ferrari                       | LaFerrari      | 2015 | 949 | 664    | \$1,416,362 |
| Acura                         | NSX            | 2017 | 573 | 476    | \$156,000   |
| Nissan                        | GT-R           | 2016 | 545 | 436    | \$101,770   |
| Lamborghini                   | Aventador      | 2015 | 700 | 507    | \$397,500   |
| Lamborghini                   | Huracan        | 2015 | 610 | 413    | \$237,250   |
| Lamborghini                   | Gallardo       | 2014 | 550 | 398    | \$191,900   |
| Bentley                       | Continental GT | 2016 | 500 | 487    | \$198,500   |
| Maserati                      | Granturismo    | 2016 | 454 | 384    | \$132,825   |
| Maserati                      | Quattroporte   | 2016 | 404 | 406    | \$99,900    |
| Maserati                      | Ghibli         | 2016 | 345 | 369    | \$70,600    |
| BMW                           | 6-Series       | 2016 | 315 | 330    | \$77,300    |
| BMW                           | i8             | 2016 | 357 | 420    | \$140,700   |
| BMW                           | M4             | 2016 | 425 | 406    | \$65,700    |
| BMW                           | M5             | 2016 | 560 | 500    | \$94,100    |
| BMW                           | M6             | 2016 | 560 | 500    | \$113,400   |
| Aston Martin                  | DB11           | 2017 | 608 | 516    | \$211,195   |
| Aston Martin                  | Rapide S       | 2016 | 552 | 465    | \$205,300   |
| Aston Martin                  | Vanquish       | 2016 | 568 | 465    | \$287,250   |
| Aston Martin                  | Vantage        | 2016 | 430 | 361    | \$103,300   |
| Chevrolet                     | Corvette       | 2016 | 650 | 650    | \$88,345    |
| Dodge                         | Viper          | 2017 | 645 | 600    | \$95,895    |
| Audi                          | R8             | 2015 | 430 | 317    | \$115,900   |
| Audi                          | RS 7           | 2016 | 560 | 516    | \$108,900   |
| Audi                          | S6             | 2016 | 450 | 406    | \$70,900    |
| Audi                          | S7             | 2016 | 450 | 406    | \$82,900    |
| Audi                          | S8             | 2016 | 520 | 481    | \$114,900   |
| Lotus                         | Evora          | 2017 | 400 | 302    | \$91,900    |
| Jaguar                        | F-Type         | 2016 | 340 | 332    | \$65,000    |
| Mercedes-Benz                 | AMG GT         | 2016 | 503 | 479    | \$129,900   |
| Mercedes-Benz                 | SL-Class       | 2016 | 329 | 354    | \$85,050    |
| Tesla                         | Model S        | 2017 | 259 | 243    | \$74,500    |
| Porsche                       | 718 Boxster    | 2017 | 300 | 280    | \$56,000    |
| Porsche                       | 718 Cayman     | 2017 | 300 | 280    | \$53,900    |
| Porsche                       | 911            | 2016 | 350 | 287    | \$84,300    |
| Porsche                       | Panamera       | 2016 | 310 | 295    | \$78,100    |
| McLaren                       | 570            | 2016 | 570 | 443    | \$184,900   |
| Rolls-Royce                   | Dawn           | 2016 | 563 | 575    | \$335,000   |
| Rolls-Royce                   | Wraith         | 2016 | 624 | 590    | \$304,350   |

A profile's bars span the whole column, not just the rows that are left, so that they stay put as the reader filters (only their heights change). They aren't shown when the table is stacked as cards in a narrow container.

## Colors from the rows kept

With `data_color="recompute"` in [i_cols_controls()](../reference/GTI.i_cols_controls.md#great_tables.GTI.i_cols_controls), a column's colors from [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) are made again from the rows a search or filter keeps, as [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) would make them from those rows alone, so that the whole palette is spread over them. Here, choose a make or two in the `Make` filter: its most powerful car takes the darkest orange, and its most expensive the darkest blue, however they compare to the rest of the cars. Show every row again and the first colors come back.

``` python
(
    GTI(gtcars_pl)
    .tab_header(title="GT Cars: colors from the rows kept")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp", decimals=0)
    .data_color(columns="hp", palette=["#fff7ec", "#ef6c00"])
    .data_color(columns="msrp", palette="Blues")
    .i_cols_filter(columns="mfr", type="facet")
    .i_cols_controls(columns=["hp", "msrp"], data_color="recompute")
)
```

| GT Cars: colors from the rows kept |                |      |     |        |             |
|------------------------------------|----------------|------|-----|--------|-------------|
| Make                               | Model          | Year | HP  | Torque | MSRP        |
| Ford                               | GT             | 2017 | 647 | 550    | \$447,000   |
| Ferrari                            | 458 Speciale   | 2015 | 597 | 398    | \$291,744   |
| Ferrari                            | 458 Spider     | 2015 | 562 | 398    | \$263,553   |
| Ferrari                            | 458 Italia     | 2014 | 562 | 398    | \$233,509   |
| Ferrari                            | 488 GTB        | 2016 | 661 | 561    | \$245,400   |
| Ferrari                            | California     | 2015 | 553 | 557    | \$198,973   |
| Ferrari                            | GTC4Lusso      | 2017 | 680 | 514    | \$298,000   |
| Ferrari                            | FF             | 2015 | 652 | 504    | \$295,000   |
| Ferrari                            | F12Berlinetta  | 2015 | 731 | 509    | \$319,995   |
| Ferrari                            | LaFerrari      | 2015 | 949 | 664    | \$1,416,362 |
| Acura                              | NSX            | 2017 | 573 | 476    | \$156,000   |
| Nissan                             | GT-R           | 2016 | 545 | 436    | \$101,770   |
| Lamborghini                        | Aventador      | 2015 | 700 | 507    | \$397,500   |
| Lamborghini                        | Huracan        | 2015 | 610 | 413    | \$237,250   |
| Lamborghini                        | Gallardo       | 2014 | 550 | 398    | \$191,900   |
| Bentley                            | Continental GT | 2016 | 500 | 487    | \$198,500   |
| Maserati                           | Granturismo    | 2016 | 454 | 384    | \$132,825   |
| Maserati                           | Quattroporte   | 2016 | 404 | 406    | \$99,900    |
| Maserati                           | Ghibli         | 2016 | 345 | 369    | \$70,600    |
| BMW                                | 6-Series       | 2016 | 315 | 330    | \$77,300    |
| BMW                                | i8             | 2016 | 357 | 420    | \$140,700   |
| BMW                                | M4             | 2016 | 425 | 406    | \$65,700    |
| BMW                                | M5             | 2016 | 560 | 500    | \$94,100    |
| BMW                                | M6             | 2016 | 560 | 500    | \$113,400   |
| Aston Martin                       | DB11           | 2017 | 608 | 516    | \$211,195   |
| Aston Martin                       | Rapide S       | 2016 | 552 | 465    | \$205,300   |
| Aston Martin                       | Vanquish       | 2016 | 568 | 465    | \$287,250   |
| Aston Martin                       | Vantage        | 2016 | 430 | 361    | \$103,300   |
| Chevrolet                          | Corvette       | 2016 | 650 | 650    | \$88,345    |
| Dodge                              | Viper          | 2017 | 645 | 600    | \$95,895    |
| Audi                               | R8             | 2015 | 430 | 317    | \$115,900   |
| Audi                               | RS 7           | 2016 | 560 | 516    | \$108,900   |
| Audi                               | S6             | 2016 | 450 | 406    | \$70,900    |
| Audi                               | S7             | 2016 | 450 | 406    | \$82,900    |
| Audi                               | S8             | 2016 | 520 | 481    | \$114,900   |
| Lotus                              | Evora          | 2017 | 400 | 302    | \$91,900    |
| Jaguar                             | F-Type         | 2016 | 340 | 332    | \$65,000    |
| Mercedes-Benz                      | AMG GT         | 2016 | 503 | 479    | \$129,900   |
| Mercedes-Benz                      | SL-Class       | 2016 | 329 | 354    | \$85,050    |
| Tesla                              | Model S        | 2017 | 259 | 243    | \$74,500    |
| Porsche                            | 718 Boxster    | 2017 | 300 | 280    | \$56,000    |
| Porsche                            | 718 Cayman     | 2017 | 300 | 280    | \$53,900    |
| Porsche                            | 911            | 2016 | 350 | 287    | \$84,300    |
| Porsche                            | Panamera       | 2016 | 310 | 295    | \$78,100    |
| McLaren                            | 570            | 2016 | 570 | 443    | \$184,900   |
| Rolls-Royce                        | Dawn           | 2016 | 563 | 575    | \$335,000   |
| Rolls-Royce                        | Wraith         | 2016 | 624 | 590    | \$304,350   |

Sorting the rows or turning the page doesn't change the colors. Only colors that depend on the rows can be made again: those [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) made down a column from the values it found there (not with `domain=`, nor from an ordered categorical's levels), and without `fn=`. A cell that a later style colors keeps that style's colors.

## Grouping rows

With `groupable=True` in [i_cols_controls()](../reference/GTI.i_cols_controls.md#great_tables.GTI.i_cols_controls), readers can group the rows by any of the chosen columns, from the **Group rows** button in the table's control bar. Each group is under a heading with its value and its number of rows (of those a search or filter keeps), the groups in the order of their values (or the other way around, when the column is sorted descending) with any missing values last. The rows are sorted within their groups, and a group running over pages has its heading on each one. Here, the cars start grouped by their country of origin, the most powerful first in each; group them by make instead, or by none.

``` python
by_country = data.pl.gtcars.select(["mfr", "model", "ctry_origin", "year", "hp", "msrp"])

(
    GTI(by_country)
    .tab_header(title="GT Cars: grouped by country")
    .cols_label(mfr="Make", model="Model", ctry_origin="Country", year="Year", hp="HP", msrp="MSRP")
    .fmt_integer(columns=["year", "hp"], use_seps=False)
    .fmt_currency(columns="msrp", decimals=0)
    .i_cols_controls(columns=["mfr", "ctry_origin"], groupable=True)
    .i_view(sort="-hp", group_by="ctry_origin")
)
```

| GT Cars: grouped by country |  |  |  |  |  |
|----|----|----|----|----|----|
| Make | Model | Country | Year | HP | MSRP |
| Ford | GT | United States | 2017 | 647 | \$447,000 |
| Ferrari | 458 Speciale | Italy | 2015 | 597 | \$291,744 |
| Ferrari | 458 Spider | Italy | 2015 | 562 | \$263,553 |
| Ferrari | 458 Italia | Italy | 2014 | 562 | \$233,509 |
| Ferrari | 488 GTB | Italy | 2016 | 661 | \$245,400 |
| Ferrari | California | Italy | 2015 | 553 | \$198,973 |
| Ferrari | GTC4Lusso | Italy | 2017 | 680 | \$298,000 |
| Ferrari | FF | Italy | 2015 | 652 | \$295,000 |
| Ferrari | F12Berlinetta | Italy | 2015 | 731 | \$319,995 |
| Ferrari | LaFerrari | Italy | 2015 | 949 | \$1,416,362 |
| Acura | NSX | Japan | 2017 | 573 | \$156,000 |
| Nissan | GT-R | Japan | 2016 | 545 | \$101,770 |
| Lamborghini | Aventador | Italy | 2015 | 700 | \$397,500 |
| Lamborghini | Huracan | Italy | 2015 | 610 | \$237,250 |
| Lamborghini | Gallardo | Italy | 2014 | 550 | \$191,900 |
| Bentley | Continental GT | United Kingdom | 2016 | 500 | \$198,500 |
| Maserati | Granturismo | Italy | 2016 | 454 | \$132,825 |
| Maserati | Quattroporte | Italy | 2016 | 404 | \$99,900 |
| Maserati | Ghibli | Italy | 2016 | 345 | \$70,600 |
| BMW | 6-Series | Germany | 2016 | 315 | \$77,300 |
| BMW | i8 | Germany | 2016 | 357 | \$140,700 |
| BMW | M4 | Germany | 2016 | 425 | \$65,700 |
| BMW | M5 | Germany | 2016 | 560 | \$94,100 |
| BMW | M6 | Germany | 2016 | 560 | \$113,400 |
| Aston Martin | DB11 | United Kingdom | 2017 | 608 | \$211,195 |
| Aston Martin | Rapide S | United Kingdom | 2016 | 552 | \$205,300 |
| Aston Martin | Vanquish | United Kingdom | 2016 | 568 | \$287,250 |
| Aston Martin | Vantage | United Kingdom | 2016 | 430 | \$103,300 |
| Chevrolet | Corvette | United States | 2016 | 650 | \$88,345 |
| Dodge | Viper | United States | 2017 | 645 | \$95,895 |
| Audi | R8 | Germany | 2015 | 430 | \$115,900 |
| Audi | RS 7 | Germany | 2016 | 560 | \$108,900 |
| Audi | S6 | Germany | 2016 | 450 | \$70,900 |
| Audi | S7 | Germany | 2016 | 450 | \$82,900 |
| Audi | S8 | Germany | 2016 | 520 | \$114,900 |
| Lotus | Evora | United Kingdom | 2017 | 400 | \$91,900 |
| Jaguar | F-Type | United Kingdom | 2016 | 340 | \$65,000 |
| Mercedes-Benz | AMG GT | Germany | 2016 | 503 | \$129,900 |
| Mercedes-Benz | SL-Class | Germany | 2016 | 329 | \$85,050 |
| Tesla | Model S | United States | 2017 | 259 | \$74,500 |
| Porsche | 718 Boxster | Germany | 2017 | 300 | \$56,000 |
| Porsche | 718 Cayman | Germany | 2017 | 300 | \$53,900 |
| Porsche | 911 | Germany | 2016 | 350 | \$84,300 |
| Porsche | Panamera | Germany | 2016 | 310 | \$78,100 |
| McLaren | 570 | United Kingdom | 2016 | 570 | \$184,900 |
| Rolls-Royce | Dawn | United Kingdom | 2016 | 563 | \$335,000 |
| Rolls-Royce | Wraith | United Kingdom | 2016 | 624 | \$304,350 |

The column the rows are grouped by is part of the table's view, which [i_view()](../reference/GTI.i_view.md#great_tables.GTI.i_view) starts the table with (`group_by=`) and [i_view_state()](../reference/GTI.i_view_state.md#great_tables.GTI.i_view_state) can keep. This grouping is the reader's: a table with row groups of its own (from `groupname_col=`) or with summary rows can't have columns to group by.

## Linked tables

With [i_link()](../reference/GTI.i_link.md#great_tables.GTI.i_link), tables on the same page work together: tables with the same group name are linked by a column they each have, so that the rows a reader selects in one filter the others to the rows with the same values. Here, select a make or two in the first table, and the second shows only their cars; clear the selection to show them all again.

``` python
makes = (
    gtcars_pl.group_by("mfr")
    .agg(pl.len().alias("models"), pl.col("hp").max().alias("top_hp"))
    .sort(pl.col("mfr").str.to_lowercase())
)

(
    GTI(makes, rowname_col="mfr")
    .tab_header(title="Makes")
    .cols_label(mfr="Make", models="Models", top_hp="Top HP")
    .fmt_integer(columns="top_hp", use_seps=False)
    .i_selection("multiple")
    .i_pagination(page_size=5)
    .i_link("gtcars", on="mfr")
)
```

| Makes         |        |        |
|---------------|--------|--------|
|               | Models | Top HP |
| Acura         | 1      | 573    |
| Aston Martin  | 4      | 608    |
| Audi          | 5      | 560    |
| Bentley       | 1      | 500    |
| BMW           | 5      | 560    |
| Chevrolet     | 1      | 650    |
| Dodge         | 1      | 645    |
| Ferrari       | 9      | 949    |
| Ford          | 1      | 647    |
| Jaguar        | 1      | 340    |
| Lamborghini   | 3      | 700    |
| Lotus         | 1      | 400    |
| Maserati      | 3      | 454    |
| McLaren       | 1      | 570    |
| Mercedes-Benz | 2      | 503    |
| Nissan        | 1      | 545    |
| Porsche       | 4      | 350    |
| Rolls-Royce   | 2      | 624    |
| Tesla         | 1      | 259    |

``` python
(
    GTI(gtcars_pl.select(["mfr", "model", "year", "hp", "msrp"]), rowname_col="model")
    .tab_header(title="Cars")
    .cols_label(mfr="Make", year="Year", hp="HP", msrp="MSRP")
    .fmt_integer(columns=["year", "hp"], use_seps=False)
    .fmt_currency(columns="msrp", decimals=0)
    .i_link("gtcars", on="mfr")
)
```

| Cars           |               |      |     |             |
|----------------|---------------|------|-----|-------------|
|                | Make          | Year | HP  | MSRP        |
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

A filtered table says what it's filtered by with a token in its control bar ("Selected in Makes: Ferrari, Lamborghini"), which goes to the selection, and whose ✕ shows every row again (until the selection changes); its info panel says so too. The filter is on top of the table's own search and filters, but isn't part of its view, so it isn't kept by [i_view_state()](../reference/GTI.i_view_state.md#great_tables.GTI.i_view_state). The tables link in the browser, with no server, so this works in a Quarto document or an HTML page, and in a notebook whose cells' outputs share a page (in Jupyter, but not in Colab, which shows each cell's output in a frame of its own).

## An explorer for looking through data

`GTI(df, preset="explorer")` starts a table set up for looking through a DataFrame rather than presenting it:

- every column can be filtered, has a profile, and can be hidden and moved
- the rows are compact, each one line high (their text doesn't wrap), with the column labels and the values in a monospaced font
- the rows can be downloaded as CSV
- with [i_inspect()](../reference/GTI.i_inspect.md#great_tables.GTI.i_inspect), the rows are numbered (by their place in the data, which stays with them as they're sorted and filtered), each column's dtype is under its label (as Polars names it, whatever the DataFrame library), missing values are tinted, and the status line says what the data is (a Polars DataFrame or LazyFrame, a Pandas DataFrame, a PyArrow Table, a DuckDB relation, or an Ibis table) and how many of its rows and columns are left

``` python
cars = data.pl.gtcars.select(["mfr", "model", "year", "hp", "mpg_c", "msrp"])

GTI(cars, preset="explorer")
```

| mfr           | model          | year | hp    | mpg_c | msrp      |
|---------------|----------------|------|-------|-------|-----------|
| Ford          | GT             | 2017 | 647.0 | 11.0  | 447000.0  |
| Ferrari       | 458 Speciale   | 2015 | 597.0 | 13.0  | 291744.0  |
| Ferrari       | 458 Spider     | 2015 | 562.0 | 13.0  | 263553.0  |
| Ferrari       | 458 Italia     | 2014 | 562.0 | 13.0  | 233509.0  |
| Ferrari       | 488 GTB        | 2016 | 661.0 | 15.0  | 245400.0  |
| Ferrari       | California     | 2015 | 553.0 | 16.0  | 198973.0  |
| Ferrari       | GTC4Lusso      | 2017 | 680.0 | 12.0  | 298000.0  |
| Ferrari       | FF             | 2015 | 652.0 | 11.0  | 295000.0  |
| Ferrari       | F12Berlinetta  | 2015 | 731.0 | 11.0  | 319995.0  |
| Ferrari       | LaFerrari      | 2015 | 949.0 | 12.0  | 1416362.0 |
| Acura         | NSX            | 2017 | 573.0 | 21.0  | 156000.0  |
| Nissan        | GT-R           | 2016 | 545.0 | 16.0  | 101770.0  |
| Lamborghini   | Aventador      | 2015 | 700.0 | 11.0  | 397500.0  |
| Lamborghini   | Huracan        | 2015 | 610.0 | 16.0  | 237250.0  |
| Lamborghini   | Gallardo       | 2014 | 550.0 | 12.0  | 191900.0  |
| Bentley       | Continental GT | 2016 | 500.0 | 15.0  | 198500.0  |
| Maserati      | Granturismo    | 2016 | 454.0 | 13.0  | 132825.0  |
| Maserati      | Quattroporte   | 2016 | 404.0 | 16.0  | 99900.0   |
| Maserati      | Ghibli         | 2016 | 345.0 | 17.0  | 70600.0   |
| BMW           | 6-Series       | 2016 | 315.0 | 20.0  | 77300.0   |
| BMW           | i8             | 2016 | 357.0 | 28.0  | 140700.0  |
| BMW           | M4             | 2016 | 425.0 | 17.0  | 65700.0   |
| BMW           | M5             | 2016 | 560.0 | 15.0  | 94100.0   |
| BMW           | M6             | 2016 | 560.0 | 15.0  | 113400.0  |
| Aston Martin  | DB11           | 2017 | 608.0 | 15.0  | 211195.0  |
| Aston Martin  | Rapide S       | 2016 | 552.0 | 14.0  | 205300.0  |
| Aston Martin  | Vanquish       | 2016 | 568.0 | 13.0  | 287250.0  |
| Aston Martin  | Vantage        | 2016 | 430.0 | 13.0  | 103300.0  |
| Chevrolet     | Corvette       | 2016 | 650.0 | 15.0  | 88345.0   |
| Dodge         | Viper          | 2017 | 645.0 | 12.0  | 95895.0   |
| Audi          | R8             | 2015 | 430.0 | 11.0  | 115900.0  |
| Audi          | RS 7           | 2016 | 560.0 | 15.0  | 108900.0  |
| Audi          | S6             | 2016 | 450.0 | 18.0  | 70900.0   |
| Audi          | S7             | 2016 | 450.0 | 17.0  | 82900.0   |
| Audi          | S8             | 2016 | 520.0 | 15.0  | 114900.0  |
| Lotus         | Evora          | 2017 | 400.0 | 16.0  | 91900.0   |
| Jaguar        | F-Type         | 2016 | 340.0 | 16.0  | 65000.0   |
| Mercedes-Benz | AMG GT         | 2016 | 503.0 | 16.0  | 129900.0  |
| Mercedes-Benz | SL-Class       | 2016 | 329.0 | 20.0  | 85050.0   |
| Tesla         | Model S        | 2017 | 259.0 | None  | 74500.0   |
| Porsche       | 718 Boxster    | 2017 | 300.0 | 21.0  | 56000.0   |
| Porsche       | 718 Cayman     | 2017 | 300.0 | 20.0  | 53900.0   |
| Porsche       | 911            | 2016 | 350.0 | 20.0  | 84300.0   |
| Porsche       | Panamera       | 2016 | 310.0 | 18.0  | 78100.0   |
| McLaren       | 570            | 2016 | 570.0 | 16.0  | 184900.0  |
| Rolls-Royce   | Dawn           | 2016 | 563.0 | 12.0  | 335000.0  |
| Rolls-Royce   | Wraith         | 2016 | 624.0 | 13.0  | 304350.0  |

A preset is only where the table starts: the `i_` methods change it as they'd change any table. Each sets all of its feature's settings, so `.i_display(wrap=True)` on an explorer lets its text wrap, but also makes its rows less compact and puts them in the table's own font, unless it's given `compact=True` and `monospace=True` too; and `.i_inspect(missing=False)` leaves the row numbers, dtypes and dimensions on. [i_inspect()](../reference/GTI.i_inspect.md#great_tables.GTI.i_inspect) and [i_display()](../reference/GTI.i_display.md#great_tables.GTI.i_display) work on their own as well, on any [GTI](../reference/GTI.md#great_tables.GTI) table.

## Using the table from Python and in apps

Python can read what readers do with a [GTI](../reference/GTI.md#great_tables.GTI) table and change it: in a notebook, with the table as a widget, in a marimo notebook, and in Shiny, Streamlit, Panel and Solara apps; and a page an app makes itself, with Flask, Django or FastHTML, can show it. See [GTI in Python and Apps](gti-in-python-and-apps.md).
