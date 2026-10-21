# Introducing Great Tables

We are really excited about developing the **Great Tables** package because we believe it'll make great-looking display tables possible in Python. Though it's still early days for the project/package, you can do good things with it today! The most recent version of **Great Tables** is in [`PyPI`](https://pypi.org/project/great-tables/). You can install it by using:

``` bash
pip install great_tables
```

In this short post, we'll take a look at a few examples that focus on the more common table-making use cases. We'll show you how to:

- configure the structure of the table
- format table-cell values
- integrate source notes
- add styling to targeted table cells
- use features from **Polars** to make it all better/nicer

Alright! Let's get right into it.

## A Basic Table

Let's get right to making a display table with **Great Tables**. The package has quite a few datasets and so we'll start by making use of the very small, but useful, [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset. After importing the [GT](../reference/GT.md#great_tables.GT) class and that dataset, we'll introduce that Pandas table to [GT()](../reference/GT.md#great_tables.GT).

``` python
from great_tables import GT, exibble

# Create a display table with the `exibble` dataset
gt_tbl = GT(exibble)

# Now, show the gt table
gt_tbl
```

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 |  | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
|  | fig | six | 2015-06-15 |  | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven |  | 19:10 | 2018-07-07 05:22 |  | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 |  | 0.44 | row_8 | grp_b |

That looks pretty good! Indeed, it is a basic table but we really didn't really ask for much either. What we did get was an HTML table containing column labels and all of the body cells. You'll probably be wanting a bit more, so, let's look at how we can incorporate more table components and perform cell data formatting in the upcoming examples.

## More Complex Tables

Let's take things a bit further and create a table with the included [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset. **Great Tables** provides a large selection of methods and they let you refine the table display. They were designed so that you can easily create a really presentable and *beautiful* table visualization.

For this next table, we'll incorporate a *Stub* component and this provides a place for the row labels. Groupings of rows will be generated through categorical values in a particular column (we just have to cite the column name for that to work). We'll add a table title and subtitle with [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header). The numerical values will be formatted with the `fmt_integer()` and `fmt_currency()` methods. Column labels will be enhanced via [cols_label()](../reference/GT.cols_label.md#great_tables.GT.cols_label) and a source note will be included through use of the [tab_source_note()](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note) method. Here is the table code, followed by the table itself.

``` python
from great_tables import GT, md, html
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "year", "hp", "trq", "msrp"]].tail(10)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .tab_spanner(label=md("*Performance*"), columns=["hp", "trq"])
    .tab_header(
        title=html("Data listing from <strong>gtcars</strong>"),
        subtitle=html("A <span style='font-size:12px;'>small selection</span> of great cars."),
    )
    .cols_label(year="Year Produced", hp="HP", trq="Torque", msrp="Price (USD)")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .tab_source_note(source_note="Source: the gtcars dataset within the Great Tables package.")
)
```

| Data listing from **gtcars** |  |  |  |  |
|----|----|----|----|----|
| A small selection of great cars. |  |  |  |  |
|  | Year Produced | *Performance* |  | Price (USD) |
|  |  | HP | Torque |  |
| Mercedes-Benz |  |  |  |  |
| AMG GT | 2016 | 503 | 479 | \$129,900.00 |
| SL-Class | 2016 | 329 | 354 | \$85,050.00 |
| Tesla |  |  |  |  |
| Model S | 2017 | 259 | 243 | \$74,500.00 |
| Porsche |  |  |  |  |
| 718 Boxster | 2017 | 300 | 280 | \$56,000.00 |
| 718 Cayman | 2017 | 300 | 280 | \$53,900.00 |
| 911 | 2016 | 350 | 287 | \$84,300.00 |
| Panamera | 2016 | 310 | 295 | \$78,100.00 |
| McLaren |  |  |  |  |
| 570 | 2016 | 570 | 443 | \$184,900.00 |
| Rolls-Royce |  |  |  |  |
| Dawn | 2016 | 563 | 575 | \$335,000.00 |
| Wraith | 2016 | 624 | 590 | \$304,350.00 |
| Source: the gtcars dataset within the Great Tables package. |  |  |  |  |

With the six different methods applied, the table looks highly presentable! The rendering you're seeing here has been done through [**Quarto**](https://quarto.org) (this entire site has been generated with [**quartodoc**](https://machow.github.io/quartodoc/get-started/overview.html)). If you haven't yet tried out **Quarto**, we highly recommend it!

For this next example we'll use the `airquality` dataset (also included in the package; it's inside the `data` submodule). With this table, two spanners will be added with the [tab_spanner()](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) method. This method is meant to be easy to use, you only need to provide the text for the spanner label and the columns associated with the spanner. We also make it easy to move columns around. You can use [cols_move_to_start()](../reference/GT.cols_move_to_start.md#great_tables.GT.cols_move_to_start) (example of that below) and there are also the [cols_move_to_end()](../reference/GT.cols_move_to_end.md#great_tables.GT.cols_move_to_end) and [cols_move()](../reference/GT.cols_move.md#great_tables.GT.cols_move) methods.

``` python
from great_tables.data import airquality

airquality_mini = airquality.head(10).assign(Year=1973)

(
    GT(airquality_mini)
    .tab_header(
        title="New York Air Quality Measurements",
        subtitle="Daily measurements in New York City (May 1-10, 1973)",
    )
    .cols_label(
        Ozone=html("Ozone,<br>ppbV"),
        Solar_R=html("Solar R.,<br>cal/m<sup>2</sup>"),
        Wind=html("Wind,<br>mph"),
        Temp=html("Temp,<br>&deg;F"),
    )
    .tab_spanner(label="Date", columns=["Year", "Month", "Day"])
    .tab_spanner(label="Measurement", columns=["Ozone", "Solar.R", "Wind", "Temp"])
    .cols_move_to_start(columns=["Year", "Month", "Day"])
)
```

[TABLE]

That table looks really good, and the nice thing about all these methods is that they can be used in virtually any order.

## Formatting Table Cells

We didn't want to skimp on formatting methods for table cells with this early release. There are 12 `fmt_*()` methods available right now:

- `fmt_number()`: format numeric values
- `fmt_integer()`: format values as integers
- `fmt_percent()`: format values as percentages
- `fmt_scientific()`: format values to scientific notation
- `fmt_currency()`: format values as currencies
- `fmt_bytes()`: format values as bytes
- `fmt_roman()`: format values as Roman numerals
- `fmt_date()`: format values as dates
- `fmt_time()`: format values as times
- `fmt_datetime()`: format values as datetimes
- `fmt_markdown()`: format Markdown text
- [fmt()](../reference/GT.fmt.md#great_tables.GT.fmt): set a column format with a formatting function

We strive to make formatting a simple task but we also want to provide the user a lot of power through advanced options and we ensure that varied combinations of options works well. For example, most of the formatting methods have a `locale=` argument. We want as many users as possible to be able to format numbers, dates, and times in ways that are familiar to them and are adapted to their own regional specifications. Now let's take a look at an example of this with a smaller version of the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset:

``` python
exibble_smaller = exibble[["date", "time"]].head(4)

(
    GT(exibble_smaller)
    .fmt_date(columns="date", date_style="wday_month_day_year")
    .fmt_date(columns="date", rows=[2, 3], date_style="day_month_year", locale="de-CH")
    .fmt_time(columns="time", time_style="h_m_s_p")
)
```

| date                       | time       |
|----------------------------|------------|
| Thursday, January 15, 2015 | 1:35:00 PM |
| Sunday, February 15, 2015  | 2:40:00 PM |
| 15 März 2015               | 3:45:00 PM |
| 15 April 2015              | 4:50:00 PM |

We support hundreds of locales, from `af` to `zu`! While there are more formatting methods yet to be added, the ones that are available all work exceedingly well.

## Using Styles within a Table

We can use the [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) method in combination with [loc.body()](../reference/loc.body.md#great_tables.loc.body) and various `style.*()` functions to set styles on cells of data within the table body. For example, the table-making code below applies a yellow background color to the targeted cells.

``` python
from great_tables import GT, style, loc
from great_tables.data import airquality

airquality_mini = airquality.head()

(
    GT(airquality_mini)
    .tab_style(
        style=style.fill(color="yellow"),
        locations=loc.body(columns="Temp", rows=[1, 2])
    )
)
```

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
|       |         | 14.3 | 56   | 5     | 5   |

Aside from [style.fill()](../reference/style.fill.md#great_tables.style.fill) we can also use [style.text()](../reference/style.text.md#great_tables.style.text) and [style.borders()](../reference/style.borders.md#great_tables.style.borders) to focus the styling on cell text and borders. Here's an example where we perform several types of styling on targeted cells (the key is to put the `style.*()` calls in a list).

``` python
from great_tables import GT, style, exibble

(
    GT(exibble[["num", "currency"]])
    .fmt_number(columns = "num", decimals=1)
    .fmt_currency(columns = "currency")
    .tab_style(
        style=[
            style.fill(color="lightcyan"),
            style.text(weight="bold")
        ],
        locations=loc.body(columns="num")
    )
    .tab_style(
        style=[
            style.fill(color = "#F9E3D6"),
            style.text(style = "italic")
        ],
        locations=loc.body(columns="currency")
    )
)
```

| num         | currency    |
|-------------|-------------|
| 0.1         | \$49.95     |
| 2.2         | \$17.95     |
| 33.3        | \$1.39      |
| 444.4       | \$65,100.00 |
| 5,550.0     | \$1,325.81  |
|             | \$13.26     |
| 777,000.0   |             |
| 8,880,000.0 | \$0.44      |

## Column Selection with Polars (and How It Helps with Styling)

Styles can also be specified using **Polars** expressions. For example, the code below uses the `Temp` column to set color to `"lightyellow"` or `"lightblue"`.

``` python
import polars as pl

from great_tables import GT, from_column, style, loc
from great_tables.data import airquality

airquality_mini = pl.from_pandas(airquality.head())

# A Polars expression defines color based on values in `Temp`
fill_color_temp = (
    pl.when(pl.col("Temp") > 70)
    .then(pl.lit("lightyellow"))
    .otherwise(pl.lit("lightblue"))
)

# Pass `fill_color_temp` to the `color=` arg of `style.fill()`
(
    GT(airquality_mini)
    .tab_style(
        style=style.fill(color=fill_color_temp),
        locations=loc.body("Temp")
    )
)
```

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |

We can deftly mix and match **Polars** column selectors and expressions. This gives us great flexibility in selecting specific columns and rows. Here's an example of doing that again with [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style):

``` python
import polars.selectors as cs

(
    GT(airquality_mini)
    .tab_style(
        style=style.fill(color="yellow"),
        locations=loc.body(
            columns=cs.starts_with("Te"),
            rows=pl.col("Temp") > 70
        )
    )
)
```

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |

It feels great to use the conveniences offered by **Polars** and we're excited about how far we can take this!

## Where We're Going with **Great Tables**

We're obviously pretty encouraged about how **Great Tables** is turning out and so we'll continue to get useful table-making niceties into the package. We welcome any and all feedback, so get in touch with us:

- you can file a GitHub [issue](https://github.com/posit-dev/great-tables/issues) or get a discussion going in [GitHub Discussions](https://github.com/posit-dev/great-tables/discussions)
- there's an [X/Twitter account at @gt_package](https://twitter.com/gt_package), so check it out for package news and announcements
- there's a fun [Discord server](https://discord.gg/Ux7nrcXHVV) that lets you more casually ask questions and generally just talk about table things

Stay tuned for more on **Great Tables** in this blog or elsewhere in the Internet!
