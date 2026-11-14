# Interactive Tables

**Great Tables** can make a table that readers work with in the browser: sorting it by its columns, searching and filtering its rows, and paging through them. The table is the one you made, with all its formatting, styles and structure; a small script that comes with its HTML adds the controls. Nothing else is needed to view it (no server, internet connection, or other library), and the table can be read before the script runs, or if it never does. It's interactive wherever its HTML is shown: in Jupyter notebooks, Quarto documents, and HTML files written with [write_raw_html()](../reference/GT.write_raw_html.md#great_tables.GT.write_raw_html).

Interactive tables are ideal for exploratory contexts where the reader needs to find specific values in a larger dataset (e.g., dashboards, internal tools, or notebook-based analysis). Sorting and filtering let readers answer their own questions about the data without you having to anticipate every view. For static outputs like PDF reports, printed documents, or email, stick with static tables since the interactivity features won't be functional in those formats.

## Which one do I want?

There are two ways to make an interactive table, and they render it with the same engine.

- **`opt_interactive()`** makes a published table browsable. It's one method, added at the end of a [GT](../reference/GT.md#great_tables.GT) table's method chain, with options for sorting, searching, filtering, paging, and a few things about how the table looks. These options are the same as those of R gt's `opt_interactive()`.
- **`GTI`** makes the table an interface, one that readers work with. A `GTI` table is made just like a [GT](../reference/GT.md#great_tables.GT) table, and its `i_` methods set what readers can do with it, column by column: which filters they get, which columns they can hide, move, or pin, how they can export the rows, how the table is first shown, and whether their view is kept for the next visit. A control bar below the table brings these together. `GTI.from_gt()` turns a [GT](../reference/GT.md#great_tables.GT) table into a `GTI` one. [GTI Tables](gti-tables.md) is about them.

If you're publishing a table and want readers to be able to sort, search and page through it, `opt_interactive()` is all you need. If the table is a focal point of the page (a lookup tool, a dashboard, a view of the data that readers come back to, etc.), it's probably better to use `GTI`.

## Enabling interactivity

A single call to `opt_interactive()` switches the table from static to interactive. The formatting methods continue to work exactly as before.

``` python
from great_tables import GT
from great_tables.data import gtcars
import polars as pl

gtcars_pl = pl.from_pandas(gtcars).select(["mfr", "model", "year", "hp", "trq", "msrp"])

(
    GT(gtcars_pl)
    .tab_header(title="GT Cars", subtitle="The full dataset, interactively")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .opt_interactive()
)
```

| GT Cars                         |                |      |     |        |                |
|---------------------------------|----------------|------|-----|--------|----------------|
| The full dataset, interactively |                |      |     |        |                |
| Make                            | Model          | Year | HP  | Torque | MSRP           |
| Ford                            | GT             | 2017 | 647 | 550    | \$447,000.00   |
| Ferrari                         | 458 Speciale   | 2015 | 597 | 398    | \$291,744.00   |
| Ferrari                         | 458 Spider     | 2015 | 562 | 398    | \$263,553.00   |
| Ferrari                         | 458 Italia     | 2014 | 562 | 398    | \$233,509.00   |
| Ferrari                         | 488 GTB        | 2016 | 661 | 561    | \$245,400.00   |
| Ferrari                         | California     | 2015 | 553 | 557    | \$198,973.00   |
| Ferrari                         | GTC4Lusso      | 2017 | 680 | 514    | \$298,000.00   |
| Ferrari                         | FF             | 2015 | 652 | 504    | \$295,000.00   |
| Ferrari                         | F12Berlinetta  | 2015 | 731 | 509    | \$319,995.00   |
| Ferrari                         | LaFerrari      | 2015 | 949 | 664    | \$1,416,362.00 |
| Acura                           | NSX            | 2017 | 573 | 476    | \$156,000.00   |
| Nissan                          | GT-R           | 2016 | 545 | 436    | \$101,770.00   |
| Lamborghini                     | Aventador      | 2015 | 700 | 507    | \$397,500.00   |
| Lamborghini                     | Huracan        | 2015 | 610 | 413    | \$237,250.00   |
| Lamborghini                     | Gallardo       | 2014 | 550 | 398    | \$191,900.00   |
| Bentley                         | Continental GT | 2016 | 500 | 487    | \$198,500.00   |
| Maserati                        | Granturismo    | 2016 | 454 | 384    | \$132,825.00   |
| Maserati                        | Quattroporte   | 2016 | 404 | 406    | \$99,900.00    |
| Maserati                        | Ghibli         | 2016 | 345 | 369    | \$70,600.00    |
| BMW                             | 6-Series       | 2016 | 315 | 330    | \$77,300.00    |
| BMW                             | i8             | 2016 | 357 | 420    | \$140,700.00   |
| BMW                             | M4             | 2016 | 425 | 406    | \$65,700.00    |
| BMW                             | M5             | 2016 | 560 | 500    | \$94,100.00    |
| BMW                             | M6             | 2016 | 560 | 500    | \$113,400.00   |
| Aston Martin                    | DB11           | 2017 | 608 | 516    | \$211,195.00   |
| Aston Martin                    | Rapide S       | 2016 | 552 | 465    | \$205,300.00   |
| Aston Martin                    | Vanquish       | 2016 | 568 | 465    | \$287,250.00   |
| Aston Martin                    | Vantage        | 2016 | 430 | 361    | \$103,300.00   |
| Chevrolet                       | Corvette       | 2016 | 650 | 650    | \$88,345.00    |
| Dodge                           | Viper          | 2017 | 645 | 600    | \$95,895.00    |
| Audi                            | R8             | 2015 | 430 | 317    | \$115,900.00   |
| Audi                            | RS 7           | 2016 | 560 | 516    | \$108,900.00   |
| Audi                            | S6             | 2016 | 450 | 406    | \$70,900.00    |
| Audi                            | S7             | 2016 | 450 | 406    | \$82,900.00    |
| Audi                            | S8             | 2016 | 520 | 481    | \$114,900.00   |
| Lotus                           | Evora          | 2017 | 400 | 302    | \$91,900.00    |
| Jaguar                          | F-Type         | 2016 | 340 | 332    | \$65,000.00    |
| Mercedes-Benz                   | AMG GT         | 2016 | 503 | 479    | \$129,900.00   |
| Mercedes-Benz                   | SL-Class       | 2016 | 329 | 354    | \$85,050.00    |
| Tesla                           | Model S        | 2017 | 259 | 243    | \$74,500.00    |
| Porsche                         | 718 Boxster    | 2017 | 300 | 280    | \$56,000.00    |
| Porsche                         | 718 Cayman     | 2017 | 300 | 280    | \$53,900.00    |
| Porsche                         | 911            | 2016 | 350 | 287    | \$84,300.00    |
| Porsche                         | Panamera       | 2016 | 310 | 295    | \$78,100.00    |
| McLaren                         | 570            | 2016 | 570 | 443    | \$184,900.00   |
| Rolls-Royce                     | Dawn           | 2016 | 563 | 575    | \$335,000.00   |
| Rolls-Royce                     | Wraith         | 2016 | 624 | 590    | \$304,350.00   |

Click the arrows under any column label to sort (or the label itself), and again to reverse the order. Columns are sorted by their values, not by how they're formatted, so the `MSRP` column sorts as numbers. The table is paginated by default with 10 rows per page.

You don't need to rebuild your table or learn a separate API. Instead, just append `.opt_interactive()` to the end of your method chain. Every part of the table is kept: the header, the stub and row groups, spanners, footnotes, source notes, and summary rows. When the rows are sorted, they're sorted within their groups.

``` python
from great_tables import GT
from great_tables.data import gtcars
import polars as pl

gtcars_grouped = (
    pl.from_pandas(gtcars)
    .filter(pl.col("ctry_origin").is_in(["Germany", "Italy"]))
    .select(["ctry_origin", "model", "year", "hp", "trq", "msrp"])
)

(
    GT(gtcars_grouped, rowname_col="model", groupname_col="ctry_origin")
    .tab_header(title="German and Italian cars")
    .tab_spanner(label="Performance", columns=["hp", "trq"])
    .cols_label(year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp", decimals=0)
    .opt_interactive(use_pagination=False)
)
```

| German and Italian cars |      |             |        |             |
|-------------------------|------|-------------|--------|-------------|
|                         | Year | Performance |        | MSRP        |
|                         |      | HP          | Torque |             |
| Italy                   |      |             |        |             |
| 458 Speciale            | 2015 | 597         | 398    | \$291,744   |
| 458 Spider              | 2015 | 562         | 398    | \$263,553   |
| 458 Italia              | 2014 | 562         | 398    | \$233,509   |
| 488 GTB                 | 2016 | 661         | 561    | \$245,400   |
| California              | 2015 | 553         | 557    | \$198,973   |
| GTC4Lusso               | 2017 | 680         | 514    | \$298,000   |
| FF                      | 2015 | 652         | 504    | \$295,000   |
| F12Berlinetta           | 2015 | 731         | 509    | \$319,995   |
| LaFerrari               | 2015 | 949         | 664    | \$1,416,362 |
| Aventador               | 2015 | 700         | 507    | \$397,500   |
| Huracan                 | 2015 | 610         | 413    | \$237,250   |
| Gallardo                | 2014 | 550         | 398    | \$191,900   |
| Granturismo             | 2016 | 454         | 384    | \$132,825   |
| Quattroporte            | 2016 | 404         | 406    | \$99,900    |
| Ghibli                  | 2016 | 345         | 369    | \$70,600    |
| Germany                 |      |             |        |             |
| 6-Series                | 2016 | 315         | 330    | \$77,300    |
| i8                      | 2016 | 357         | 420    | \$140,700   |
| M4                      | 2016 | 425         | 406    | \$65,700    |
| M5                      | 2016 | 560         | 500    | \$94,100    |
| M6                      | 2016 | 560         | 500    | \$113,400   |
| R8                      | 2015 | 430         | 317    | \$115,900   |
| RS 7                    | 2016 | 560         | 516    | \$108,900   |
| S6                      | 2016 | 450         | 406    | \$70,900    |
| S7                      | 2016 | 450         | 406    | \$82,900    |
| S8                      | 2016 | 520         | 481    | \$114,900   |
| AMG GT                  | 2016 | 503         | 479    | \$129,900   |
| SL-Class                | 2016 | 329         | 354    | \$85,050    |
| 718 Boxster             | 2017 | 300         | 280    | \$56,000    |
| 718 Cayman              | 2017 | 300         | 280    | \$53,900    |
| 911                     | 2016 | 350         | 287    | \$84,300    |
| Panamera                | 2016 | 310         | 295    | \$78,100    |

## Search and filters

Pass `use_search=True` to add a search box above the table, and `use_filters=True` to give every column a filter. Each column label then has a filter button, which opens a filter suited to the column: a range for numbers (and dates), a list of values for a column with only a few of them, and text to match for the rest.

``` python
(
    GT(gtcars_pl)
    .tab_header(title="GT Cars: Search and Filter")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .opt_interactive(use_search=True, use_filters=True)
)
```

| GT Cars: Search and Filter |                |      |     |        |                |
|----------------------------|----------------|------|-----|--------|----------------|
| Make                       | Model          | Year | HP  | Torque | MSRP           |
| Ford                       | GT             | 2017 | 647 | 550    | \$447,000.00   |
| Ferrari                    | 458 Speciale   | 2015 | 597 | 398    | \$291,744.00   |
| Ferrari                    | 458 Spider     | 2015 | 562 | 398    | \$263,553.00   |
| Ferrari                    | 458 Italia     | 2014 | 562 | 398    | \$233,509.00   |
| Ferrari                    | 488 GTB        | 2016 | 661 | 561    | \$245,400.00   |
| Ferrari                    | California     | 2015 | 553 | 557    | \$198,973.00   |
| Ferrari                    | GTC4Lusso      | 2017 | 680 | 514    | \$298,000.00   |
| Ferrari                    | FF             | 2015 | 652 | 504    | \$295,000.00   |
| Ferrari                    | F12Berlinetta  | 2015 | 731 | 509    | \$319,995.00   |
| Ferrari                    | LaFerrari      | 2015 | 949 | 664    | \$1,416,362.00 |
| Acura                      | NSX            | 2017 | 573 | 476    | \$156,000.00   |
| Nissan                     | GT-R           | 2016 | 545 | 436    | \$101,770.00   |
| Lamborghini                | Aventador      | 2015 | 700 | 507    | \$397,500.00   |
| Lamborghini                | Huracan        | 2015 | 610 | 413    | \$237,250.00   |
| Lamborghini                | Gallardo       | 2014 | 550 | 398    | \$191,900.00   |
| Bentley                    | Continental GT | 2016 | 500 | 487    | \$198,500.00   |
| Maserati                   | Granturismo    | 2016 | 454 | 384    | \$132,825.00   |
| Maserati                   | Quattroporte   | 2016 | 404 | 406    | \$99,900.00    |
| Maserati                   | Ghibli         | 2016 | 345 | 369    | \$70,600.00    |
| BMW                        | 6-Series       | 2016 | 315 | 330    | \$77,300.00    |
| BMW                        | i8             | 2016 | 357 | 420    | \$140,700.00   |
| BMW                        | M4             | 2016 | 425 | 406    | \$65,700.00    |
| BMW                        | M5             | 2016 | 560 | 500    | \$94,100.00    |
| BMW                        | M6             | 2016 | 560 | 500    | \$113,400.00   |
| Aston Martin               | DB11           | 2017 | 608 | 516    | \$211,195.00   |
| Aston Martin               | Rapide S       | 2016 | 552 | 465    | \$205,300.00   |
| Aston Martin               | Vanquish       | 2016 | 568 | 465    | \$287,250.00   |
| Aston Martin               | Vantage        | 2016 | 430 | 361    | \$103,300.00   |
| Chevrolet                  | Corvette       | 2016 | 650 | 650    | \$88,345.00    |
| Dodge                      | Viper          | 2017 | 645 | 600    | \$95,895.00    |
| Audi                       | R8             | 2015 | 430 | 317    | \$115,900.00   |
| Audi                       | RS 7           | 2016 | 560 | 516    | \$108,900.00   |
| Audi                       | S6             | 2016 | 450 | 406    | \$70,900.00    |
| Audi                       | S7             | 2016 | 450 | 406    | \$82,900.00    |
| Audi                       | S8             | 2016 | 520 | 481    | \$114,900.00   |
| Lotus                      | Evora          | 2017 | 400 | 302    | \$91,900.00    |
| Jaguar                     | F-Type         | 2016 | 340 | 332    | \$65,000.00    |
| Mercedes-Benz              | AMG GT         | 2016 | 503 | 479    | \$129,900.00   |
| Mercedes-Benz              | SL-Class       | 2016 | 329 | 354    | \$85,050.00    |
| Tesla                      | Model S        | 2017 | 259 | 243    | \$74,500.00    |
| Porsche                    | 718 Boxster    | 2017 | 300 | 280    | \$56,000.00    |
| Porsche                    | 718 Cayman     | 2017 | 300 | 280    | \$53,900.00    |
| Porsche                    | 911            | 2016 | 350 | 287    | \$84,300.00    |
| Porsche                    | Panamera       | 2016 | 310 | 295    | \$78,100.00    |
| McLaren                    | 570            | 2016 | 570 | 443    | \$184,900.00   |
| Rolls-Royce                | Dawn           | 2016 | 563 | 575    | \$335,000.00   |
| Rolls-Royce                | Wraith         | 2016 | 624 | 590    | \$304,350.00   |

Try typing `"Audi"` in the search box, or setting a range in the `HP` filter, to narrow the results.

## Pagination options

Control the number of rows per page and let users choose from a list of sizes with `page_size_default=` and `page_size_values=` (shown with `use_page_size_select=True`). The page controls can also be changed with `pagination_type=`: `"numbers"` (a button for each page, the default), `"simple"` (previous and next), `"full"` (first, previous, next and last, with the page number), or `"jump"` (previous and next, with a box to type the page number in).

``` python
(
    GT(gtcars_pl)
    .tab_header(title="GT Cars: Pagination options")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .opt_interactive(
        use_page_size_select=True,
        page_size_default=5,
        page_size_values=[5, 10, 25, 50],
        pagination_type="full",
    )
)
```

| GT Cars: Pagination options |                |      |     |        |                |
|-----------------------------|----------------|------|-----|--------|----------------|
| Make                        | Model          | Year | HP  | Torque | MSRP           |
| Ford                        | GT             | 2017 | 647 | 550    | \$447,000.00   |
| Ferrari                     | 458 Speciale   | 2015 | 597 | 398    | \$291,744.00   |
| Ferrari                     | 458 Spider     | 2015 | 562 | 398    | \$263,553.00   |
| Ferrari                     | 458 Italia     | 2014 | 562 | 398    | \$233,509.00   |
| Ferrari                     | 488 GTB        | 2016 | 661 | 561    | \$245,400.00   |
| Ferrari                     | California     | 2015 | 553 | 557    | \$198,973.00   |
| Ferrari                     | GTC4Lusso      | 2017 | 680 | 514    | \$298,000.00   |
| Ferrari                     | FF             | 2015 | 652 | 504    | \$295,000.00   |
| Ferrari                     | F12Berlinetta  | 2015 | 731 | 509    | \$319,995.00   |
| Ferrari                     | LaFerrari      | 2015 | 949 | 664    | \$1,416,362.00 |
| Acura                       | NSX            | 2017 | 573 | 476    | \$156,000.00   |
| Nissan                      | GT-R           | 2016 | 545 | 436    | \$101,770.00   |
| Lamborghini                 | Aventador      | 2015 | 700 | 507    | \$397,500.00   |
| Lamborghini                 | Huracan        | 2015 | 610 | 413    | \$237,250.00   |
| Lamborghini                 | Gallardo       | 2014 | 550 | 398    | \$191,900.00   |
| Bentley                     | Continental GT | 2016 | 500 | 487    | \$198,500.00   |
| Maserati                    | Granturismo    | 2016 | 454 | 384    | \$132,825.00   |
| Maserati                    | Quattroporte   | 2016 | 404 | 406    | \$99,900.00    |
| Maserati                    | Ghibli         | 2016 | 345 | 369    | \$70,600.00    |
| BMW                         | 6-Series       | 2016 | 315 | 330    | \$77,300.00    |
| BMW                         | i8             | 2016 | 357 | 420    | \$140,700.00   |
| BMW                         | M4             | 2016 | 425 | 406    | \$65,700.00    |
| BMW                         | M5             | 2016 | 560 | 500    | \$94,100.00    |
| BMW                         | M6             | 2016 | 560 | 500    | \$113,400.00   |
| Aston Martin                | DB11           | 2017 | 608 | 516    | \$211,195.00   |
| Aston Martin                | Rapide S       | 2016 | 552 | 465    | \$205,300.00   |
| Aston Martin                | Vanquish       | 2016 | 568 | 465    | \$287,250.00   |
| Aston Martin                | Vantage        | 2016 | 430 | 361    | \$103,300.00   |
| Chevrolet                   | Corvette       | 2016 | 650 | 650    | \$88,345.00    |
| Dodge                       | Viper          | 2017 | 645 | 600    | \$95,895.00    |
| Audi                        | R8             | 2015 | 430 | 317    | \$115,900.00   |
| Audi                        | RS 7           | 2016 | 560 | 516    | \$108,900.00   |
| Audi                        | S6             | 2016 | 450 | 406    | \$70,900.00    |
| Audi                        | S7             | 2016 | 450 | 406    | \$82,900.00    |
| Audi                        | S8             | 2016 | 520 | 481    | \$114,900.00   |
| Lotus                       | Evora          | 2017 | 400 | 302    | \$91,900.00    |
| Jaguar                      | F-Type         | 2016 | 340 | 332    | \$65,000.00    |
| Mercedes-Benz               | AMG GT         | 2016 | 503 | 479    | \$129,900.00   |
| Mercedes-Benz               | SL-Class       | 2016 | 329 | 354    | \$85,050.00    |
| Tesla                       | Model S        | 2017 | 259 | 243    | \$74,500.00    |
| Porsche                     | 718 Boxster    | 2017 | 300 | 280    | \$56,000.00    |
| Porsche                     | 718 Cayman     | 2017 | 300 | 280    | \$53,900.00    |
| Porsche                     | 911            | 2016 | 350 | 287    | \$84,300.00    |
| Porsche                     | Panamera       | 2016 | 310 | 295    | \$78,100.00    |
| McLaren                     | 570            | 2016 | 570 | 443    | \$184,900.00   |
| Rolls-Royce                 | Dawn           | 2016 | 563 | 575    | \$335,000.00   |
| Rolls-Royce                 | Wraith         | 2016 | 624 | 590    | \$304,350.00   |

Set `use_pagination=False` to display the full table without paging. This is useful for smaller datasets, and with `height=`, which limits the table's height and has it scroll within it, keeping its header and column labels in view.

``` python
(
    GT(gtcars_pl)
    .tab_header(title="GT Cars: Scrolling")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .opt_interactive(use_pagination=False, height=400, use_compact_mode=True)
)
```

| GT Cars: Scrolling |                |      |     |        |                |
|--------------------|----------------|------|-----|--------|----------------|
| Make               | Model          | Year | HP  | Torque | MSRP           |
| Ford               | GT             | 2017 | 647 | 550    | \$447,000.00   |
| Ferrari            | 458 Speciale   | 2015 | 597 | 398    | \$291,744.00   |
| Ferrari            | 458 Spider     | 2015 | 562 | 398    | \$263,553.00   |
| Ferrari            | 458 Italia     | 2014 | 562 | 398    | \$233,509.00   |
| Ferrari            | 488 GTB        | 2016 | 661 | 561    | \$245,400.00   |
| Ferrari            | California     | 2015 | 553 | 557    | \$198,973.00   |
| Ferrari            | GTC4Lusso      | 2017 | 680 | 514    | \$298,000.00   |
| Ferrari            | FF             | 2015 | 652 | 504    | \$295,000.00   |
| Ferrari            | F12Berlinetta  | 2015 | 731 | 509    | \$319,995.00   |
| Ferrari            | LaFerrari      | 2015 | 949 | 664    | \$1,416,362.00 |
| Acura              | NSX            | 2017 | 573 | 476    | \$156,000.00   |
| Nissan             | GT-R           | 2016 | 545 | 436    | \$101,770.00   |
| Lamborghini        | Aventador      | 2015 | 700 | 507    | \$397,500.00   |
| Lamborghini        | Huracan        | 2015 | 610 | 413    | \$237,250.00   |
| Lamborghini        | Gallardo       | 2014 | 550 | 398    | \$191,900.00   |
| Bentley            | Continental GT | 2016 | 500 | 487    | \$198,500.00   |
| Maserati           | Granturismo    | 2016 | 454 | 384    | \$132,825.00   |
| Maserati           | Quattroporte   | 2016 | 404 | 406    | \$99,900.00    |
| Maserati           | Ghibli         | 2016 | 345 | 369    | \$70,600.00    |
| BMW                | 6-Series       | 2016 | 315 | 330    | \$77,300.00    |
| BMW                | i8             | 2016 | 357 | 420    | \$140,700.00   |
| BMW                | M4             | 2016 | 425 | 406    | \$65,700.00    |
| BMW                | M5             | 2016 | 560 | 500    | \$94,100.00    |
| BMW                | M6             | 2016 | 560 | 500    | \$113,400.00   |
| Aston Martin       | DB11           | 2017 | 608 | 516    | \$211,195.00   |
| Aston Martin       | Rapide S       | 2016 | 552 | 465    | \$205,300.00   |
| Aston Martin       | Vanquish       | 2016 | 568 | 465    | \$287,250.00   |
| Aston Martin       | Vantage        | 2016 | 430 | 361    | \$103,300.00   |
| Chevrolet          | Corvette       | 2016 | 650 | 650    | \$88,345.00    |
| Dodge              | Viper          | 2017 | 645 | 600    | \$95,895.00    |
| Audi               | R8             | 2015 | 430 | 317    | \$115,900.00   |
| Audi               | RS 7           | 2016 | 560 | 516    | \$108,900.00   |
| Audi               | S6             | 2016 | 450 | 406    | \$70,900.00    |
| Audi               | S7             | 2016 | 450 | 406    | \$82,900.00    |
| Audi               | S8             | 2016 | 520 | 481    | \$114,900.00   |
| Lotus              | Evora          | 2017 | 400 | 302    | \$91,900.00    |
| Jaguar             | F-Type         | 2016 | 340 | 332    | \$65,000.00    |
| Mercedes-Benz      | AMG GT         | 2016 | 503 | 479    | \$129,900.00   |
| Mercedes-Benz      | SL-Class       | 2016 | 329 | 354    | \$85,050.00    |
| Tesla              | Model S        | 2017 | 259 | 243    | \$74,500.00    |
| Porsche            | 718 Boxster    | 2017 | 300 | 280    | \$56,000.00    |
| Porsche            | 718 Cayman     | 2017 | 300 | 280    | \$53,900.00    |
| Porsche            | 911            | 2016 | 350 | 287    | \$84,300.00    |
| Porsche            | Panamera       | 2016 | 310 | 295    | \$78,100.00    |
| McLaren            | 570            | 2016 | 570 | 443    | \$184,900.00   |
| Rolls-Royce        | Dawn           | 2016 | 563 | 575    | \$335,000.00   |
| Rolls-Royce        | Wraith         | 2016 | 624 | 590    | \$304,350.00   |

A table with thousands of rows is quicker to sort, search and filter with pagination, as only a page of its rows is shown at a time. In Chrome and Edge, sorting a long table also takes longer if the page it's on has CSS rules of its own that use the `:has()` selector, as these make moving rows slower in those browsers.

An interactive table has all of its rows in its HTML, so a very large one can be slow to load, especially on phones. You'll get a warning when a table has more than 3,000 rows or more than 10 MB of HTML, as it's quicker to load with fewer rows (e.g., by filtering the data first) or fewer columns. You'll also get one when a table shows more than 1,000 rows at once, all on one page or on a page of that size, as every row shown is laid out again when the rows are sorted, searched or filtered. To turn the warning off, use `warnings.filterwarnings("ignore", message="This interactive table may be slow")`.

## Styling with [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style)

Styles set with [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) are part of the table's cells, so they follow the data when you sort or filter.

``` python
from great_tables import style, loc

(
    GT(gtcars_pl)
    .tab_header(title="GT Cars: Targeted styles")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .tab_style(
        style=style.fill(color="#fff3cd"),
        locations=loc.body(columns="hp", rows=pl.col("hp") > 500),
    )
    .tab_style(
        style=[style.text(color="#c0392b", weight="bold")],
        locations=loc.body(columns="msrp", rows=pl.col("msrp") > 200_000),
    )
    .tab_style(
        style=[style.fill(color="#ddeeff"), style.text(weight="bold")],
        locations=loc.column_labels(columns=["hp", "trq"]),
    )
    .opt_interactive(use_search=True, use_filters=True, page_size_default=10)
)
```

| GT Cars: Targeted styles |                |      |     |        |                |
|--------------------------|----------------|------|-----|--------|----------------|
| Make                     | Model          | Year | HP  | Torque | MSRP           |
| Ford                     | GT             | 2017 | 647 | 550    | \$447,000.00   |
| Ferrari                  | 458 Speciale   | 2015 | 597 | 398    | \$291,744.00   |
| Ferrari                  | 458 Spider     | 2015 | 562 | 398    | \$263,553.00   |
| Ferrari                  | 458 Italia     | 2014 | 562 | 398    | \$233,509.00   |
| Ferrari                  | 488 GTB        | 2016 | 661 | 561    | \$245,400.00   |
| Ferrari                  | California     | 2015 | 553 | 557    | \$198,973.00   |
| Ferrari                  | GTC4Lusso      | 2017 | 680 | 514    | \$298,000.00   |
| Ferrari                  | FF             | 2015 | 652 | 504    | \$295,000.00   |
| Ferrari                  | F12Berlinetta  | 2015 | 731 | 509    | \$319,995.00   |
| Ferrari                  | LaFerrari      | 2015 | 949 | 664    | \$1,416,362.00 |
| Acura                    | NSX            | 2017 | 573 | 476    | \$156,000.00   |
| Nissan                   | GT-R           | 2016 | 545 | 436    | \$101,770.00   |
| Lamborghini              | Aventador      | 2015 | 700 | 507    | \$397,500.00   |
| Lamborghini              | Huracan        | 2015 | 610 | 413    | \$237,250.00   |
| Lamborghini              | Gallardo       | 2014 | 550 | 398    | \$191,900.00   |
| Bentley                  | Continental GT | 2016 | 500 | 487    | \$198,500.00   |
| Maserati                 | Granturismo    | 2016 | 454 | 384    | \$132,825.00   |
| Maserati                 | Quattroporte   | 2016 | 404 | 406    | \$99,900.00    |
| Maserati                 | Ghibli         | 2016 | 345 | 369    | \$70,600.00    |
| BMW                      | 6-Series       | 2016 | 315 | 330    | \$77,300.00    |
| BMW                      | i8             | 2016 | 357 | 420    | \$140,700.00   |
| BMW                      | M4             | 2016 | 425 | 406    | \$65,700.00    |
| BMW                      | M5             | 2016 | 560 | 500    | \$94,100.00    |
| BMW                      | M6             | 2016 | 560 | 500    | \$113,400.00   |
| Aston Martin             | DB11           | 2017 | 608 | 516    | \$211,195.00   |
| Aston Martin             | Rapide S       | 2016 | 552 | 465    | \$205,300.00   |
| Aston Martin             | Vanquish       | 2016 | 568 | 465    | \$287,250.00   |
| Aston Martin             | Vantage        | 2016 | 430 | 361    | \$103,300.00   |
| Chevrolet                | Corvette       | 2016 | 650 | 650    | \$88,345.00    |
| Dodge                    | Viper          | 2017 | 645 | 600    | \$95,895.00    |
| Audi                     | R8             | 2015 | 430 | 317    | \$115,900.00   |
| Audi                     | RS 7           | 2016 | 560 | 516    | \$108,900.00   |
| Audi                     | S6             | 2016 | 450 | 406    | \$70,900.00    |
| Audi                     | S7             | 2016 | 450 | 406    | \$82,900.00    |
| Audi                     | S8             | 2016 | 520 | 481    | \$114,900.00   |
| Lotus                    | Evora          | 2017 | 400 | 302    | \$91,900.00    |
| Jaguar                   | F-Type         | 2016 | 340 | 332    | \$65,000.00    |
| Mercedes-Benz            | AMG GT         | 2016 | 503 | 479    | \$129,900.00   |
| Mercedes-Benz            | SL-Class       | 2016 | 329 | 354    | \$85,050.00    |
| Tesla                    | Model S        | 2017 | 259 | 243    | \$74,500.00    |
| Porsche                  | 718 Boxster    | 2017 | 300 | 280    | \$56,000.00    |
| Porsche                  | 718 Cayman     | 2017 | 300 | 280    | \$53,900.00    |
| Porsche                  | 911            | 2016 | 350 | 287    | \$84,300.00    |
| Porsche                  | Panamera       | 2016 | 310 | 295    | \$78,100.00    |
| McLaren                  | 570            | 2016 | 570 | 443    | \$184,900.00   |
| Rolls-Royce              | Dawn           | 2016 | 563 | 575    | \$335,000.00   |
| Rolls-Royce              | Wraith         | 2016 | 624 | 590    | \$304,350.00   |

From the output you might notice:

- HP values over 500 are highlighted in amber
- MSRP values over \$200,000 appear in bold red
- the `HP` and `Torque` column headers have a blue-tinted background

Sort by `HP` or `MSRP` to confirm that the styling moves with the data.

## Colorizing with [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color)

The [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) method also works in interactive tables. It applies a continuous color scale to each cell based on the underlying value, and the colors follow the data when you sort or filter.

``` python
(
    GT(gtcars_pl)
    .tab_header(title="GT Cars: data_color()")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .data_color(columns="hp",  palette=["#fff7ec", "#ef6c00"])
    .data_color(columns="msrp", palette="Blues")
    .opt_interactive(use_search=True, use_filters=True, page_size_default=10)
)
```

| GT Cars: data_color() |                |      |     |        |                |
|-----------------------|----------------|------|-----|--------|----------------|
| Make                  | Model          | Year | HP  | Torque | MSRP           |
| Ford                  | GT             | 2017 | 647 | 550    | \$447,000.00   |
| Ferrari               | 458 Speciale   | 2015 | 597 | 398    | \$291,744.00   |
| Ferrari               | 458 Spider     | 2015 | 562 | 398    | \$263,553.00   |
| Ferrari               | 458 Italia     | 2014 | 562 | 398    | \$233,509.00   |
| Ferrari               | 488 GTB        | 2016 | 661 | 561    | \$245,400.00   |
| Ferrari               | California     | 2015 | 553 | 557    | \$198,973.00   |
| Ferrari               | GTC4Lusso      | 2017 | 680 | 514    | \$298,000.00   |
| Ferrari               | FF             | 2015 | 652 | 504    | \$295,000.00   |
| Ferrari               | F12Berlinetta  | 2015 | 731 | 509    | \$319,995.00   |
| Ferrari               | LaFerrari      | 2015 | 949 | 664    | \$1,416,362.00 |
| Acura                 | NSX            | 2017 | 573 | 476    | \$156,000.00   |
| Nissan                | GT-R           | 2016 | 545 | 436    | \$101,770.00   |
| Lamborghini           | Aventador      | 2015 | 700 | 507    | \$397,500.00   |
| Lamborghini           | Huracan        | 2015 | 610 | 413    | \$237,250.00   |
| Lamborghini           | Gallardo       | 2014 | 550 | 398    | \$191,900.00   |
| Bentley               | Continental GT | 2016 | 500 | 487    | \$198,500.00   |
| Maserati              | Granturismo    | 2016 | 454 | 384    | \$132,825.00   |
| Maserati              | Quattroporte   | 2016 | 404 | 406    | \$99,900.00    |
| Maserati              | Ghibli         | 2016 | 345 | 369    | \$70,600.00    |
| BMW                   | 6-Series       | 2016 | 315 | 330    | \$77,300.00    |
| BMW                   | i8             | 2016 | 357 | 420    | \$140,700.00   |
| BMW                   | M4             | 2016 | 425 | 406    | \$65,700.00    |
| BMW                   | M5             | 2016 | 560 | 500    | \$94,100.00    |
| BMW                   | M6             | 2016 | 560 | 500    | \$113,400.00   |
| Aston Martin          | DB11           | 2017 | 608 | 516    | \$211,195.00   |
| Aston Martin          | Rapide S       | 2016 | 552 | 465    | \$205,300.00   |
| Aston Martin          | Vanquish       | 2016 | 568 | 465    | \$287,250.00   |
| Aston Martin          | Vantage        | 2016 | 430 | 361    | \$103,300.00   |
| Chevrolet             | Corvette       | 2016 | 650 | 650    | \$88,345.00    |
| Dodge                 | Viper          | 2017 | 645 | 600    | \$95,895.00    |
| Audi                  | R8             | 2015 | 430 | 317    | \$115,900.00   |
| Audi                  | RS 7           | 2016 | 560 | 516    | \$108,900.00   |
| Audi                  | S6             | 2016 | 450 | 406    | \$70,900.00    |
| Audi                  | S7             | 2016 | 450 | 406    | \$82,900.00    |
| Audi                  | S8             | 2016 | 520 | 481    | \$114,900.00   |
| Lotus                 | Evora          | 2017 | 400 | 302    | \$91,900.00    |
| Jaguar                | F-Type         | 2016 | 340 | 332    | \$65,000.00    |
| Mercedes-Benz         | AMG GT         | 2016 | 503 | 479    | \$129,900.00   |
| Mercedes-Benz         | SL-Class       | 2016 | 329 | 354    | \$85,050.00    |
| Tesla                 | Model S        | 2017 | 259 | 243    | \$74,500.00    |
| Porsche               | 718 Boxster    | 2017 | 300 | 280    | \$56,000.00    |
| Porsche               | 718 Cayman     | 2017 | 300 | 280    | \$53,900.00    |
| Porsche               | 911            | 2016 | 350 | 287    | \$84,300.00    |
| Porsche               | Panamera       | 2016 | 310 | 295    | \$78,100.00    |
| McLaren               | 570            | 2016 | 570 | 443    | \$184,900.00   |
| Rolls-Royce           | Dawn           | 2016 | 563 | 575    | \$335,000.00   |
| Rolls-Royce           | Wraith         | 2016 | 624 | 590    | \$304,350.00   |

Each column uses its own independent scale: orange for `HP` and blue for `MSRP`. The scales are computed from the full dataset, so a cell keeps its color when you filter by `Make`. (A `GTI` table can color them again from the rows a filter keeps instead: see [Colors from the rows kept](22-gti-tables.md#colors-from-the-rows-kept).)

### Multiple columns, shared scale

Pass `domain=` to lock the color range across columns so they share a common scale.

``` python
(
    GT(gtcars_pl)
    .tab_header(
        title="GT Cars: HP and Torque on a shared scale",
        subtitle="Higher values are darker and both columns use the same domain",
    )
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .data_color(
        columns=["hp", "trq"],
        palette=["#edf8fb", "#006d2c"],
        domain=[200, 700],
    )
    .opt_interactive(use_search=True, page_size_default=10)
)
```

| GT Cars: HP and Torque on a shared scale |  |  |  |  |  |
|----|----|----|----|----|----|
| Higher values are darker and both columns use the same domain |  |  |  |  |  |
| Make | Model | Year | HP | Torque | MSRP |
| Ford | GT | 2017 | 647 | 550 | \$447,000.00 |
| Ferrari | 458 Speciale | 2015 | 597 | 398 | \$291,744.00 |
| Ferrari | 458 Spider | 2015 | 562 | 398 | \$263,553.00 |
| Ferrari | 458 Italia | 2014 | 562 | 398 | \$233,509.00 |
| Ferrari | 488 GTB | 2016 | 661 | 561 | \$245,400.00 |
| Ferrari | California | 2015 | 553 | 557 | \$198,973.00 |
| Ferrari | GTC4Lusso | 2017 | 680 | 514 | \$298,000.00 |
| Ferrari | FF | 2015 | 652 | 504 | \$295,000.00 |
| Ferrari | F12Berlinetta | 2015 | 731 | 509 | \$319,995.00 |
| Ferrari | LaFerrari | 2015 | 949 | 664 | \$1,416,362.00 |
| Acura | NSX | 2017 | 573 | 476 | \$156,000.00 |
| Nissan | GT-R | 2016 | 545 | 436 | \$101,770.00 |
| Lamborghini | Aventador | 2015 | 700 | 507 | \$397,500.00 |
| Lamborghini | Huracan | 2015 | 610 | 413 | \$237,250.00 |
| Lamborghini | Gallardo | 2014 | 550 | 398 | \$191,900.00 |
| Bentley | Continental GT | 2016 | 500 | 487 | \$198,500.00 |
| Maserati | Granturismo | 2016 | 454 | 384 | \$132,825.00 |
| Maserati | Quattroporte | 2016 | 404 | 406 | \$99,900.00 |
| Maserati | Ghibli | 2016 | 345 | 369 | \$70,600.00 |
| BMW | 6-Series | 2016 | 315 | 330 | \$77,300.00 |
| BMW | i8 | 2016 | 357 | 420 | \$140,700.00 |
| BMW | M4 | 2016 | 425 | 406 | \$65,700.00 |
| BMW | M5 | 2016 | 560 | 500 | \$94,100.00 |
| BMW | M6 | 2016 | 560 | 500 | \$113,400.00 |
| Aston Martin | DB11 | 2017 | 608 | 516 | \$211,195.00 |
| Aston Martin | Rapide S | 2016 | 552 | 465 | \$205,300.00 |
| Aston Martin | Vanquish | 2016 | 568 | 465 | \$287,250.00 |
| Aston Martin | Vantage | 2016 | 430 | 361 | \$103,300.00 |
| Chevrolet | Corvette | 2016 | 650 | 650 | \$88,345.00 |
| Dodge | Viper | 2017 | 645 | 600 | \$95,895.00 |
| Audi | R8 | 2015 | 430 | 317 | \$115,900.00 |
| Audi | RS 7 | 2016 | 560 | 516 | \$108,900.00 |
| Audi | S6 | 2016 | 450 | 406 | \$70,900.00 |
| Audi | S7 | 2016 | 450 | 406 | \$82,900.00 |
| Audi | S8 | 2016 | 520 | 481 | \$114,900.00 |
| Lotus | Evora | 2017 | 400 | 302 | \$91,900.00 |
| Jaguar | F-Type | 2016 | 340 | 332 | \$65,000.00 |
| Mercedes-Benz | AMG GT | 2016 | 503 | 479 | \$129,900.00 |
| Mercedes-Benz | SL-Class | 2016 | 329 | 354 | \$85,050.00 |
| Tesla | Model S | 2017 | 259 | 243 | \$74,500.00 |
| Porsche | 718 Boxster | 2017 | 300 | 280 | \$56,000.00 |
| Porsche | 718 Cayman | 2017 | 300 | 280 | \$53,900.00 |
| Porsche | 911 | 2016 | 350 | 287 | \$84,300.00 |
| Porsche | Panamera | 2016 | 310 | 295 | \$78,100.00 |
| McLaren | 570 | 2016 | 570 | 443 | \$184,900.00 |
| Rolls-Royce | Dawn | 2016 | 563 | 575 | \$335,000.00 |
| Rolls-Royce | Wraith | 2016 | 624 | 590 | \$304,350.00 |

## Going further with `GTI`

When readers need more than `opt_interactive()` gives them, make the table a `GTI` table: its filters, column profiles, grouping, linked tables and the explorer preset are in [GTI Tables](gti-tables.md). Reading and setting an interactive table's view from Python (in a notebook, or in a Shiny, Streamlit, Panel or Solara app, which take `opt_interactive()` tables too) is in [GTI in Python and Apps](gti-in-python-and-apps.md).
