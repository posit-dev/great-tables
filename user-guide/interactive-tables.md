# Interactive Tables

**Great Tables** can make a table that readers work with in the browser: sorting it by its columns, searching and filtering its rows, and paging through them. The table is the one you made, with all its formatting, styles and structure; a small script that comes with its HTML adds the controls. Nothing else is needed to view it (no server, internet connection, or other library), and the table can be read before the script runs, or if it never does. It's interactive wherever its HTML is shown: in Jupyter notebooks, Quarto documents, and HTML files written with [write_raw_html()](../reference/GT.write_raw_html.md#great_tables.GT.write_raw_html).

Interactive tables are ideal for exploratory contexts where the reader needs to find specific values in a larger dataset (e.g., dashboards, internal tools, or notebook-based analysis). Sorting and filtering let readers answer their own questions about the data without you having to anticipate every view. For static outputs like PDF reports, printed documents, or email, stick with static tables since the interactivity features won't be functional in those formats.

## Which one do I want?

There are two ways to make an interactive table, and they render it with the same engine.

- **`opt_interactive()`** makes a published table browsable. It's one method, added at the end of a [GT](../reference/GT.md#great_tables.GT) table's method chain, with options for sorting, searching, filtering, paging, and a few things about how the table looks. These options are the same as those of R gt's `opt_interactive()`.
- **`GTI`** makes the table an interface, one that readers work with. A `GTI` table is made just like a [GT](../reference/GT.md#great_tables.GT) table, and its `i_` methods set what readers can do with it, column by column: which filters they get, which columns they can hide, move, or pin, how they can export the rows, how the table is first shown, and whether their view is kept for the next visit. A control bar below the table brings these together. `GTI.from_gt()` turns a [GT](../reference/GT.md#great_tables.GT) table into a `GTI` one.

If you're publishing a table and want readers to be able to sort, search and page through it, `opt_interactive()` is all you need. If the table is a focal point the page (a lookup tool, a dashboard, a view of the data that readers come back to, etc.), it's probably better to use `GTI`.

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

Each column uses its own independent scale: orange for `HP` and blue for `MSRP`. The scales are computed from the full dataset, so a cell keeps its color when you filter by `Make`. (A `GTI` table can color them again from the rows a filter keeps instead: see [Colors from the rows kept](#colors-from-the-rows-kept).)

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

When readers need more than `opt_interactive()` gives them, make the table a `GTI` table. Here, the `Make` column gets a list of its values to choose from and `HP` a range, the table is first shown with the most powerful cars at the top, and readers can download the rows they've filtered as CSV.

``` python
from great_tables import GTI

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

A table you've already made with [GT()](../reference/GT.md#great_tables.GT), including one with `opt_interactive()`, becomes a `GTI` table with `GTI.from_gt()`, keeping what `opt_interactive()` set. Each of the `i_` methods has examples in its docstring (e.g., `help(GTI.i_cols_filter)`).

### The parts of a `GTI` table

A `GTI` table is the table GT made, with a few parts added around it. From the top:

- The **status line**, just above the table, says what the data is and how much of it is shown ("Polars DataFrame · 12 of 47 rows × 6 columns"). It's there with `i_inspect()` (and in an explorer). In a table made with `opt_interactive(use_search=True)`, the search box is here too.
- The **column controls**, under each column label: the column's dtype (with `i_inspect()`), its sort arrows, and its filter button.
- The **column profiles**, under the labels of the columns `i_cols_profile()` chose: a small plot of how their values are spread.
- The **row numbers**, at the start of each row (with `i_inspect()`), which stay with the rows as they're sorted and filtered. A DataFrame's rows are numbered from 0, as its index is, and a DuckDB relation's or an Ibis table's from 1, as a database numbers them; `row_start=` in `i_inspect()` sets either one.
- The **control bar**, just below the table, which brings together what readers can do with the table as a whole: searching it, its **page controls** (the arrows, and the **page counter**, "2/5", which can be clicked to type a page to go to), undo and redo, resetting the view, and the buttons that open its **panels** (the table's info, its columns, grouping its rows, exporting it, and its keyboard shortcuts). Over its controls, the **filter tokens** say what the rows are filtered by, one token for each filter, whose ✕ removes it. In a body that scrolls (with `i_scroll()`), the foot of the body is a **height handle**, dragged for a taller or shorter body.

A table made with `opt_interactive()` has a **pager** below it instead of the control bar: its page buttons, and the number of rows shown.

The status line and the control bar are close to the table, and the space that GT (or the page) leaves around the table is kept past them, so that they read as part of it rather than of the text around it.

### Row details

With `i_row_details()`, each row can have more to show under it, when the reader asks for it. A function makes a row's details from its values (including those of columns the table hides): as text, with [md()](../reference/md.md#great_tables.md) or [html()](../reference/html.md#great_tables.md), or as a [GT](../reference/GT.md#great_tables.GT) table of their own. Here, each car has a few lines about its engine. Click the arrow by a car's name to show them, or use **Expand all** in the table's info panel to show every car's.

``` python
from great_tables import md


def engine(row):
    economy = (
        "" if row["mpg_c"] is None else f" It gets {row['mpg_c']:.0f} mpg in the city, "
        f"and {row['mpg_h']:.0f} on the highway."
    )
    return md(
        f"The **{row['trim']}** ({row['bdy_style']}) makes {row['hp']:.0f} hp at "
        f"{row['hp_rpm']:,.0f} rpm, and {row['trq']:.0f} lb-ft of torque.{economy}"
    )


(
    GTI(pl.from_pandas(gtcars), rowname_col="model")
    .tab_header(title="GT Cars: with row details")
    .cols_hide(columns=["trim", "bdy_style", "hp_rpm", "trq_rpm", "mpg_c", "mpg_h", "trsmn"])
    .cols_label(mfr="Make", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp", decimals=0)
    .i_row_details(engine)
)
```

| GT Cars: with row details |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
|  | Make | Year | HP | Torque | drivetrain | ctry_origin | MSRP |
| GT | Ford | 2017 | 647 | 550 | rwd | United States | \$447,000 |
| 458 Speciale | Ferrari | 2015 | 597 | 398 | rwd | Italy | \$291,744 |
| 458 Spider | Ferrari | 2015 | 562 | 398 | rwd | Italy | \$263,553 |
| 458 Italia | Ferrari | 2014 | 562 | 398 | rwd | Italy | \$233,509 |
| 488 GTB | Ferrari | 2016 | 661 | 561 | rwd | Italy | \$245,400 |
| California | Ferrari | 2015 | 553 | 557 | rwd | Italy | \$198,973 |
| GTC4Lusso | Ferrari | 2017 | 680 | 514 | awd | Italy | \$298,000 |
| FF | Ferrari | 2015 | 652 | 504 | awd | Italy | \$295,000 |
| F12Berlinetta | Ferrari | 2015 | 731 | 509 | rwd | Italy | \$319,995 |
| LaFerrari | Ferrari | 2015 | 949 | 664 | rwd | Italy | \$1,416,362 |
| NSX | Acura | 2017 | 573 | 476 | awd | Japan | \$156,000 |
| GT-R | Nissan | 2016 | 545 | 436 | awd | Japan | \$101,770 |
| Aventador | Lamborghini | 2015 | 700 | 507 | awd | Italy | \$397,500 |
| Huracan | Lamborghini | 2015 | 610 | 413 | rwd | Italy | \$237,250 |
| Gallardo | Lamborghini | 2014 | 550 | 398 | rwd | Italy | \$191,900 |
| Continental GT | Bentley | 2016 | 500 | 487 | awd | United Kingdom | \$198,500 |
| Granturismo | Maserati | 2016 | 454 | 384 | rwd | Italy | \$132,825 |
| Quattroporte | Maserati | 2016 | 404 | 406 | rwd | Italy | \$99,900 |
| Ghibli | Maserati | 2016 | 345 | 369 | rwd | Italy | \$70,600 |
| 6-Series | BMW | 2016 | 315 | 330 | rwd | Germany | \$77,300 |
| i8 | BMW | 2016 | 357 | 420 | awd | Germany | \$140,700 |
| M4 | BMW | 2016 | 425 | 406 | rwd | Germany | \$65,700 |
| M5 | BMW | 2016 | 560 | 500 | rwd | Germany | \$94,100 |
| M6 | BMW | 2016 | 560 | 500 | rwd | Germany | \$113,400 |
| DB11 | Aston Martin | 2017 | 608 | 516 | rwd | United Kingdom | \$211,195 |
| Rapide S | Aston Martin | 2016 | 552 | 465 | rwd | United Kingdom | \$205,300 |
| Vanquish | Aston Martin | 2016 | 568 | 465 | rwd | United Kingdom | \$287,250 |
| Vantage | Aston Martin | 2016 | 430 | 361 | rwd | United Kingdom | \$103,300 |
| Corvette | Chevrolet | 2016 | 650 | 650 | rwd | United States | \$88,345 |
| Viper | Dodge | 2017 | 645 | 600 | rwd | United States | \$95,895 |
| R8 | Audi | 2015 | 430 | 317 | awd | Germany | \$115,900 |
| RS 7 | Audi | 2016 | 560 | 516 | awd | Germany | \$108,900 |
| S6 | Audi | 2016 | 450 | 406 | awd | Germany | \$70,900 |
| S7 | Audi | 2016 | 450 | 406 | awd | Germany | \$82,900 |
| S8 | Audi | 2016 | 520 | 481 | awd | Germany | \$114,900 |
| Evora | Lotus | 2017 | 400 | 302 | rwd | United Kingdom | \$91,900 |
| F-Type | Jaguar | 2016 | 340 | 332 | rwd | United Kingdom | \$65,000 |
| AMG GT | Mercedes-Benz | 2016 | 503 | 479 | rwd | Germany | \$129,900 |
| SL-Class | Mercedes-Benz | 2016 | 329 | 354 | rwd | Germany | \$85,050 |
| Model S | Tesla | 2017 | 259 | 243 | awd | United States | \$74,500 |
| 718 Boxster | Porsche | 2017 | 300 | 280 | rwd | Germany | \$56,000 |
| 718 Cayman | Porsche | 2017 | 300 | 280 | rwd | Germany | \$53,900 |
| 911 | Porsche | 2016 | 350 | 287 | rwd | Germany | \$84,300 |
| Panamera | Porsche | 2016 | 310 | 295 | rwd | Germany | \$78,100 |
| 570 | McLaren | 2016 | 570 | 443 | rwd | United Kingdom | \$184,900 |
| Dawn | Rolls-Royce | 2016 | 563 | 575 | rwd | United Kingdom | \$335,000 |
| Wraith | Rolls-Royce | 2016 | 624 | 590 | rwd | United Kingdom | \$304,350 |

The **Base Coupe** (coupe) makes 647 hp at 6,250 rpm, and 550 lb-ft of torque. It gets 11 mpg in the city, and 18 on the highway. The **Base Coupe** (coupe) makes 597 hp at 9,000 rpm, and 398 lb-ft of torque. It gets 13 mpg in the city, and 17 on the highway. The **Base** (convertible) makes 562 hp at 9,000 rpm, and 398 lb-ft of torque. It gets 13 mpg in the city, and 17 on the highway. The **Base Coupe** (coupe) makes 562 hp at 9,000 rpm, and 398 lb-ft of torque. It gets 13 mpg in the city, and 17 on the highway. The **Base Coupe** (coupe) makes 661 hp at 8,000 rpm, and 561 lb-ft of torque. It gets 15 mpg in the city, and 22 on the highway. The **Base Convertible** (convertible) makes 553 hp at 7,500 rpm, and 557 lb-ft of torque. It gets 16 mpg in the city, and 23 on the highway. The **Base Coupe** (coupe) makes 680 hp at 8,250 rpm, and 514 lb-ft of torque. It gets 12 mpg in the city, and 17 on the highway. The **Base Coupe** (coupe) makes 652 hp at 8,000 rpm, and 504 lb-ft of torque. It gets 11 mpg in the city, and 16 on the highway. The **Base Coupe** (coupe) makes 731 hp at 8,250 rpm, and 509 lb-ft of torque. It gets 11 mpg in the city, and 16 on the highway. The **Base Coupe** (coupe) makes 949 hp at 9,000 rpm, and 664 lb-ft of torque. It gets 12 mpg in the city, and 16 on the highway. The **Base Coupe** (coupe) makes 573 hp at 6,500 rpm, and 476 lb-ft of torque. It gets 21 mpg in the city, and 22 on the highway. The **Premium Coupe** (coupe) makes 545 hp at 6,400 rpm, and 436 lb-ft of torque. It gets 16 mpg in the city, and 22 on the highway. The **LP 700-4 Coupe** (coupe) makes 700 hp at 8,250 rpm, and 507 lb-ft of torque. It gets 11 mpg in the city, and 18 on the highway. The **LP 610-4 Coupe** (coupe) makes 610 hp at 8,250 rpm, and 413 lb-ft of torque. It gets 16 mpg in the city, and 20 on the highway. The **LP 550-2 Coupe** (coupe) makes 550 hp at 8,000 rpm, and 398 lb-ft of torque. It gets 12 mpg in the city, and 20 on the highway. The **V8 Coupe** (coupe) makes 500 hp at 6,000 rpm, and 487 lb-ft of torque. It gets 15 mpg in the city, and 25 on the highway. The **Sport Coupe** (coupe) makes 454 hp at 7,600 rpm, and 384 lb-ft of torque. It gets 13 mpg in the city, and 21 on the highway. The **S Sedan** (sedan) makes 404 hp at 5,500 rpm, and 406 lb-ft of torque. It gets 16 mpg in the city, and 23 on the highway. The **Base Sedan** (sedan) makes 345 hp at 5,250 rpm, and 369 lb-ft of torque. It gets 17 mpg in the city, and 24 on the highway. The **640 I Coupe** (coupe) makes 315 hp at 5,800 rpm, and 330 lb-ft of torque. It gets 20 mpg in the city, and 30 on the highway. The **Mega World Coupe** (coupe) makes 357 hp at 5,800 rpm, and 420 lb-ft of torque. It gets 28 mpg in the city, and 29 on the highway. The **Base Coupe** (coupe) makes 425 hp at 5,500 rpm, and 406 lb-ft of torque. It gets 17 mpg in the city, and 24 on the highway. The **Base Sedan** (sedan) makes 560 hp at 6,000 rpm, and 500 lb-ft of torque. It gets 15 mpg in the city, and 22 on the highway. The **Base Coupe** (coupe) makes 560 hp at 6,000 rpm, and 500 lb-ft of torque. It gets 15 mpg in the city, and 22 on the highway. The **Base Coupe** (coupe) makes 608 hp at 6,500 rpm, and 516 lb-ft of torque. It gets 15 mpg in the city, and 21 on the highway. The **Base Sedan** (sedan) makes 552 hp at 6,650 rpm, and 465 lb-ft of torque. It gets 14 mpg in the city, and 21 on the highway. The **Base Coupe** (coupe) makes 568 hp at 6,650 rpm, and 465 lb-ft of torque. It gets 13 mpg in the city, and 21 on the highway. The **V8 GT (Manual) Coupe** (coupe) makes 430 hp at 7,300 rpm, and 361 lb-ft of torque. It gets 13 mpg in the city, and 19 on the highway. The **Z06 Coupe** (coupe) makes 650 hp at 6,400 rpm, and 650 lb-ft of torque. It gets 15 mpg in the city, and 22 on the highway. The **GT Coupe** (coupe) makes 645 hp at 5,000 rpm, and 600 lb-ft of torque. It gets 12 mpg in the city, and 19 on the highway. The **4.2 (Manual) Coupe** (coupe) makes 430 hp at 7,900 rpm, and 317 lb-ft of torque. It gets 11 mpg in the city, and 20 on the highway. The **Quattro Hatchback** (hatchback) makes 560 hp at 5,700 rpm, and 516 lb-ft of torque. It gets 15 mpg in the city, and 25 on the highway. The **Premium Plus quattro Sedan** (sedan) makes 450 hp at 5,800 rpm, and 406 lb-ft of torque. It gets 18 mpg in the city, and 27 on the highway. The **Prestige quattro Hatchback** (hatchback) makes 450 hp at 5,800 rpm, and 406 lb-ft of torque. It gets 17 mpg in the city, and 27 on the highway. The **Base Sedan** (sedan) makes 520 hp at 5,800 rpm, and 481 lb-ft of torque. It gets 15 mpg in the city, and 25 on the highway. The **2+2 Coupe** (coupe) makes 400 hp at 7,000 rpm, and 302 lb-ft of torque. It gets 16 mpg in the city, and 24 on the highway. The **Base (Manual) Coupe** (coupe) makes 340 hp at 6,500 rpm, and 332 lb-ft of torque. It gets 16 mpg in the city, and 24 on the highway. The **S Coupe** (coupe) makes 503 hp at 6,250 rpm, and 479 lb-ft of torque. It gets 16 mpg in the city, and 22 on the highway. The **SL400 Convertible** (convertible) makes 329 hp at 5,250 rpm, and 354 lb-ft of torque. It gets 20 mpg in the city, and 27 on the highway. The **75D** (sedan) makes 259 hp at 6,100 rpm, and 243 lb-ft of torque. The **Base Convertible** (convertible) makes 300 hp at 6,500 rpm, and 280 lb-ft of torque. It gets 21 mpg in the city, and 28 on the highway. The **Base Coupe** (coupe) makes 300 hp at 6,500 rpm, and 280 lb-ft of torque. It gets 20 mpg in the city, and 29 on the highway. The **Carrera Coupe** (coupe) makes 350 hp at 7,400 rpm, and 287 lb-ft of torque. It gets 20 mpg in the city, and 28 on the highway. The **Base Sedan** (sedan) makes 310 hp at 6,200 rpm, and 295 lb-ft of torque. It gets 18 mpg in the city, and 28 on the highway. The **Base Coupe** (coupe) makes 570 hp at 7,500 rpm, and 443 lb-ft of torque. It gets 16 mpg in the city, and 23 on the highway. The **Base Convertible** (convertible) makes 563 hp at 5,250 rpm, and 575 lb-ft of torque. It gets 12 mpg in the city, and 19 on the highway. The **Base Coupe** (coupe) makes 624 hp at 5,600 rpm, and 590 lb-ft of torque. It gets 13 mpg in the city, and 21 on the highway.

The details are in the table's HTML, made as it's rendered, but aren't searched, filtered or exported (and each [GT](../reference/GT.md#great_tables.GT) table in them brings its own CSS, so many of them make a larger page). A column can hold them instead, with each row's details: `i_row_details()` takes its name, and the column is then left out of the table.

### Column profiles

With `i_cols_profile()`, columns get a small plot under their labels of how their values are spread: a histogram of numbers and dates, and bars for the most common values of the others, each with the share of rows that have a missing value. The plots follow the rows a search or filter keeps, so they show at a glance what's left. Here, choose a few makes in the `Make` filter and watch the horsepower and prices narrow; point at a bar to see its values and its number of rows.

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

### Colors from the rows kept

With `data_color="recompute"` in `i_cols_controls()`, a column's colors from [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) are made again from the rows a search or filter keeps, as [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) would make them from those rows alone, so that the whole palette is spread over them. Here, choose a make or two in the `Make` filter: its most powerful car takes the darkest orange, and its most expensive the darkest blue, however they compare to the rest of the cars. Show every row again and the first colors come back.

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

### Grouping rows

With `groupable=True` in `i_cols_controls()`, readers can group the rows by any of the chosen columns, from the **Group rows** button in the table's control bar. Each group is under a heading with its value and its number of rows (of those a search or filter keeps), the groups in the order of their values (or the other way around, when the column is sorted descending) with any missing values last. The rows are sorted within their groups, and a group running over pages has its heading on each one. Here, the cars start grouped by their country of origin, the most powerful first in each; group them by make instead, or by none.

``` python
by_country = pl.from_pandas(gtcars).select(["mfr", "model", "ctry_origin", "year", "hp", "msrp"])

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

The column the rows are grouped by is part of the table's view, which `i_view()` starts the table with (`group_by=`) and `i_view_state()` can keep. This grouping is the reader's: a table with row groups of its own (from `groupname_col=`) or with summary rows can't have columns to group by.

### Linked tables

With `i_link()`, tables on the same page work together: tables with the same group name are linked by a column they each have, so that the rows a reader selects in one filter the others to the rows with the same values. Here, select a make or two in the first table, and the second shows only their cars; clear the selection to show them all again.

``` python
makes = (
    gtcars_pl.group_by("mfr")
    .agg(pl.len().alias("models"), pl.col("hp").max().alias("top_hp"))
    .sort("mfr")
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
| BMW           | 5      | 560    |
| Bentley       | 1      | 500    |
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

A filtered table says what it's filtered by with a token in its control bar ("Selected in Makes: Ferrari, Lamborghini"), which goes to the selection, and whose ✕ shows every row again (until the selection changes); its info panel says so too. The filter is on top of the table's own search and filters, but isn't part of its view, so it isn't kept by `i_view_state()`. The tables link in the browser, with no server, so this works in a Quarto document or an HTML page, and in a notebook whose cells' outputs share a page (in Jupyter, but not in Colab, which shows each cell's output in a frame of its own).

### An explorer for looking through data

`GTI(data, preset="explorer")` starts a table set up for looking through a DataFrame rather than presenting it: every column can be filtered, has a profile, and can be hidden and moved; the rows are compact, each one line high (their text doesn't wrap), with the column labels and the values in a monospaced font, and can be downloaded as CSV; and with `i_inspect()`, the rows are numbered (by their place in the data, from 0 for a DataFrame, which stays with them as they're sorted and filtered), each column's dtype is under its label (as Polars names it, whatever the DataFrame library), the status line above the table says what the data is (a Polars DataFrame or LazyFrame, a Pandas DataFrame, a PyArrow Table, a DuckDB relation, or an Ibis table) and how many of its rows and columns are left, and missing values are tinted.

``` python
cars = pl.from_pandas(gtcars).select(["mfr", "model", "year", "hp", "mpg_c", "msrp"])

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

A preset is only where the table starts: the `i_` methods change it as they'd change any table. Each sets all of its feature's settings, so `.i_display(wrap=True)` on an explorer lets its text wrap, but also makes its rows less compact and puts them in the table's own font, unless it's given `compact=True` and `monospace=True` too; and `.i_inspect(missing=False)` leaves the row numbers, dtypes and dimensions on. `i_inspect()` and `i_display()` work on their own as well, on any `GTI` table.

### Using the table from Python

In a notebook, `i_as_widget()` shows the table as a widget (with [anywidget](https://anywidget.dev), installed with `pip install great_tables[widget]`), whose view and selection Python can read and set: what the reader searched for, filtered and sorted by, the rows that leaves, and the rows they selected. The table still works in the browser; the widget tells Python what it shows.

``` python
widget = (
    GTI(cars)
    .i_cols_filter(columns="mfr", type="facet")
    .i_selection("multiple")
    .i_as_widget()
)
widget
```

Then, in another cell (as the browser gives Python the table's state once the cell is done):

``` python
widget.query            # the filters, as a query in text: 'mfr in ("Ferrari")'
widget.search           # the search
widget.sort             # the sort, e.g., ["-hp"]
widget.rows             # the data rows kept, in the order shown (numbered from 0)
widget.view()           # those rows, as a DataFrame of the data's library
widget.view(selected=True)  # the rows selected

widget.query = 'mfr in ("Ferrari", "Lamborghini")'
widget.sort = "-hp"
widget.selection = [0, 3]
```

Setting `query`, `search`, `sort` or `selection` changes the table as shown, and `widget.on_change(callback)` calls `callback(widget)` after each change the reader makes. A change made from Python is applied by the browser after the cell runs, so ask for the rows it leaves in another cell.

### Using the table in a Shiny app

In a [Shiny](https://shiny.posit.co/py/) app, an interactive table (a `GTI` table, or a [GT](../reference/GT.md#great_tables.GT) table with `opt_interactive()`) rendered with `render_gt()`, from `great_tables.shiny`, gives the server its state as inputs, named after the output: `input.<id>_view()` (a dict with the `"query"`, `"search"`, `"sort"`, `"page"`, `"page_size"`, `"hidden"` columns and `"group_by"` column), `input.<id>_rows()` (the data rows kept, in the order shown) and `input.<id>_selection()` (the rows selected). `update_gti()` sets its query, search, sort and selection from the server.

``` python
from shiny import App, reactive, render, ui
from great_tables import GTI
from great_tables.data import gtcars
from great_tables.shiny import output_gt, render_gt, update_gti

app_ui = ui.page_fluid(
    ui.input_action_button("fastest", "Fastest first"),
    output_gt("cars"),
    ui.output_text("chosen"),
)


def server(input, output, session):
    @render_gt
    def cars():
        return (
            GTI(gtcars[["mfr", "model", "year", "hp", "msrp"]])
            .i_cols_filter(columns="mfr", type="facet")
            .i_selection("multiple")
        )

    @render.text
    def chosen():
        rows = input.cars_selection()
        return f"{len(rows)} of {len(input.cars_rows())} cars selected"

    @reactive.effect
    @reactive.event(input.fastest)
    def _():
        update_gti("cars", sort="-hp", selection=[])


app = App(app_ui, server)
```

The table works in the browser as it does anywhere else, so the server isn't asked for each page, sort or search; a table rendered again starts with the view it's given.

### Using the table in a Streamlit app

In a [Streamlit](https://streamlit.io) app, `st_gti()`, from `great_tables.streamlit` (installed with `pip install great_tables[streamlit]`), shows an interactive table (a `GTI` table, or a [GT](../reference/GT.md#great_tables.GT) table with `opt_interactive()`) and gives its state: its `query`, `search` and `sort`, the data `rows` kept (in the order shown) and the rows in its `selection`. Each change the reader makes runs the app again, with the table's new state. `update_gti()`, called in a widget's callback, sets its query, search, sort and selection from the app.

``` python
import streamlit as st
from great_tables import GTI
from great_tables.data import gtcars
from great_tables.streamlit import st_gti, update_gti

st.button("Fastest first", on_click=update_gti, args=("cars",), kwargs={"sort": "-hp"})
table = (
    GTI(gtcars[["mfr", "model", "year", "hp", "msrp"]])
    .i_cols_filter(columns="mfr", type="facet")
    .i_selection("multiple")
)
state = st_gti(table, key="cars")
st.write(f"{len(state.selection)} of {len(state.rows or [])} cars selected")
```

The table keeps its view and selection by its `key` as the app runs again, as long as it's rendered the same. A table whose rows are kept in Python (with `i_scale()`) asks the app for each page, which runs it again; make it once, with `st.cache_resource`, so that it isn't rendered again each time.

### Using the table in a Panel app

In a [Panel](https://panel.holoviz.org) app or notebook, `GTIPane`, from `great_tables.panel` (installed with `pip install great_tables[panel]`), shows an interactive table (a `GTI` table, or a [GT](../reference/GT.md#great_tables.GT) table with `opt_interactive()`) as a Panel component, whose state is in its parameters: `query`, `search` and `sort` (a list, e.g., `["-hp"]`), the data `rows` kept (in the order shown) and the rows in its `selection`. Each change the reader makes sets them, so that they can be used with `pn.bind()` or watched like any other parameter; and setting `query`, `search`, `sort` or `selection` changes the table.

``` python
import panel as pn
from great_tables import GTI
from great_tables.data import gtcars
from great_tables.panel import GTIPane

pn.extension()

cars = gtcars[["mfr", "model", "year", "hp", "msrp"]]
table = GTIPane(
    GTI(cars).i_cols_filter(columns="mfr", type="facet").i_selection("multiple")
)


def chosen(rows, selection):
    return f"{len(selection)} of {len(rows or [])} cars selected"


fastest = pn.widgets.Button(name="Fastest first")
fastest.on_click(lambda _: table.param.update(sort=["-hp"], selection=[]))
pn.Column(fastest, table, pn.bind(chosen, table.param.rows, table.param.selection)).servable()
```

`table.data()` gives the rows kept as a DataFrame of the data's library (and `table.data(selected=True)` the rows selected). The table works in the browser, which finds its `rows`, so they can be `None` until it has (as before the table's shown with a search). A table whose rows are kept in Python (with `i_scale()`) asks the app for each page instead, and its `rows` are found in Python.
