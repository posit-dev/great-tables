# How We Used Great Tables to Supercharge Reporting in Pointblank

The Great Tables package allows you to make tables, and they're really great when part of a report, a book, or a web page. The API is meant to be easy to work with so DataFrames could be made into publication-quality tables without a lot of hassle. And having nice-looking tables in the mix elevates the quality of the medium you're working in.

We were inspired by this and decided to explore what it could mean to introduce a package where reporting is largely in the form of beautiful tables. To this end, we started work on a new Python package that generates tables (c/o Great Tables) as reporting objects. This package is called [Pointblank](https://github.com/posit-dev/pointblank), its focus is that of data validation, and the reporting tables it can produce informs users on the results of a data validation workflow. In this post we'll go through how Pointblank:

- enables you to validate many types of DataFrames and SQL databases
- provides easy-to-understand validation result tables and thorough drilldowns
- gives you nice previews of data tables across a range of backends

### Validating data with Pointblank

Just like Great Tables, Pointblank's primary input is a table and the goal of that library is to perform checks of the tabular data. Other libraries in this domain include [Great Expectations](https://github.com/great-expectations/great_expectations), [pandera](https://github.com/unionai-oss/pandera), [Soda](https://github.com/sodadata/soda-core?tab=readme-ov-file), and [PyDeequ](https://github.com/awslabs/python-deequ).

Below is the main validation report table that users are likely to see quite often. Each row is a validation step, with columns reporting details about each step and their results.

``` python
import pointblank as pb

validation = (
    pb.Validate(
        data=pb.load_dataset(dataset="small_table", tbl_type="polars"),
        label="An example validation",
        thresholds=(0.1, 0.2, 0.5),
    )
    .col_vals_gt(columns="d", value=1000)
    .col_vals_le(columns="c", value=5)
    .col_exists(columns=["date", "date_time"])
    .interrogate()
)

validation
```

[TABLE]

The first validation step (`cols_val_gt()`) checks the `d` column in the data, to ensure each value is greater than `1000`. Notice that the red bar on the left indicates it failed, and the `FAIL` column says it has 6 failing values out of 13 `UNITS`.

The table is chock full of the information you need when doing data validation tasks. And it's also easy on the eyes. Some cool features include:

1.  a header with information on the type of input table plus important validation options
2.  vertical color strips on the left side to indicate overall status of the rows
3.  icons in several columns (space saving and they let you know what's up)
4.  'CSV' buttons that, when clicked, provide you with a CSV file
5.  a footer with timing information for the analysis

It's a nice table and it scales nicely to the large variety of validation types and options available in the Pointblank library. Viewing this table is a central part of using that library and the great thing about the reporting being a table like this is that it can be shared by placing it in a publication environment of your choosing (for example, it could be put in a Quarto document).

Here is the code that was used to generate the data validation above:

``` python
import pointblank as pb

validation = (
    pb.Validate(
        data=pb.load_dataset(dataset="small_table", tbl_type="polars"),
        label="An example validation",
        thresholds=(0.1, 0.2, 0.5),
    )
    .col_vals_gt(columns="d", value=1000)
    .col_vals_le(columns="c", value=5)
    .col_exists(columns=["date", "date_time"])
    .interrogate()
)

validation
```

Pointblank makes it easy to get started by giving you a simple entry point (`Validate()`), allowing you to define as many validation steps as needed. Each validation step is specified by calling methods like `.cols_vals_gt()`, which is short for checking that "column values are greater than" some specified value.

Pointblank enables you to validate many types of DataFrames and SQL databases. Pointblank supports Pandas and Polars through Narwhals, and numerous backends (like DuckDB and MySQL) are also supported though our Ibis integration.

### Exploring data validation failures

Note that the above validation report table showed 6 failures in the first validation step. You might want to know exactly *what* failed, giving you a chance to fix the underlying data quality issues. To do that, you can use the `get_step_report()` method:

``` python
validation.get_step_report(i=1)
```

| Report for Validation Step 1 ASSERTION `d > 1000` **6** / **13** TEST UNIT FAILURES IN COLUMN **6** EXTRACT OF ALL **6** ROWS (WITH TEST UNIT FAILURES IN RED): |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|
|  | date_time *Datetime* | date *Date* | a *Int64* | b *String* | c *Int64* | d *Float64* | e *Boolean* | f *String* |
| 5 | 2016-01-09 12:36:00 | 2016-01-09 | 8 | 3-ldm-038 | 7 | 283.94 | True | low |
| 7 | 2016-01-15 18:46:00 | 2016-01-15 | 7 | 1-knw-093 | 3 | 843.34 | True | high |
| 9 | 2016-01-20 04:30:00 | 2016-01-20 | 3 | 5-bce-642 | 9 | 837.93 | False | high |
| 10 | 2016-01-20 04:30:00 | 2016-01-20 | 3 | 5-bce-642 | 9 | 837.93 | False | high |
| 11 | 2016-01-26 20:07:00 | 2016-01-26 | 4 | 2-dmx-010 | 7 | 833.98 | True | low |
| 12 | 2016-01-28 02:51:00 | 2016-01-28 | 2 | 7-dmx-010 | 8 | 108.34 | False | low |

The use of a table for reporting is ideal here! The main features of this step report table include:

1.  a header with summarized information
2.  the selected rows that contain the failures
3.  a highlighted column of interest

Different types of validation methods will have step report tables that organize the pertinent information in a way that makes sense for the validation performed.

### Previewing datasets across backends

Because many of the backends Pointblank supports have varying ways to view the underlying data, we provide a unified `preview()` function. It gives you a beautiful and consistent view of any data table. Here is how it looks against a 2,000 row DuckDB table that's included in the package (`game_revenue`):

``` python
pb.preview(pb.load_dataset(dataset="game_revenue", tbl_type="duckdb"))
```

| DuckDBRows2,000Columns11 |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|
|  | player_id *string* | session_id *string* | session_start *timestamp* | time *timestamp* | item_type *string* | item_name *string* | item_revenue *float64* | session_duration *float64* | start_day *date* | acquisition *string* | country *string* |
| 1 | ECPANOIXLZHF896 | ECPANOIXLZHF896-eol2j8bs | 2015-01-01 01:31:03+00:00 | 2015-01-01 01:31:27+00:00 | iap | offer2 | 8.99 | 16.3 | 2015-01-01 | google | Germany |
| 2 | ECPANOIXLZHF896 | ECPANOIXLZHF896-eol2j8bs | 2015-01-01 01:31:03+00:00 | 2015-01-01 01:36:57+00:00 | iap | gems3 | 22.49 | 16.3 | 2015-01-01 | google | Germany |
| 3 | ECPANOIXLZHF896 | ECPANOIXLZHF896-eol2j8bs | 2015-01-01 01:31:03+00:00 | 2015-01-01 01:37:45+00:00 | iap | gold7 | 107.99 | 16.3 | 2015-01-01 | google | Germany |
| 4 | ECPANOIXLZHF896 | ECPANOIXLZHF896-eol2j8bs | 2015-01-01 01:31:03+00:00 | 2015-01-01 01:42:33+00:00 | ad | ad_20sec | 0.76 | 16.3 | 2015-01-01 | google | Germany |
| 5 | ECPANOIXLZHF896 | ECPANOIXLZHF896-hdu9jkls | 2015-01-01 11:50:02+00:00 | 2015-01-01 11:55:20+00:00 | ad | ad_5sec | 0.03 | 35.2 | 2015-01-01 | google | Germany |
| 1996 | NAOJRDMCSEBI281 | NAOJRDMCSEBI281-j2vs9ilp | 2015-01-21 01:57:50+00:00 | 2015-01-21 02:02:50+00:00 | ad | ad_survey | 1.332 | 25.8 | 2015-01-11 | organic | Norway |
| 1997 | NAOJRDMCSEBI281 | NAOJRDMCSEBI281-j2vs9ilp | 2015-01-21 01:57:50+00:00 | 2015-01-21 02:22:14+00:00 | ad | ad_survey | 1.35 | 25.8 | 2015-01-11 | organic | Norway |
| 1998 | RMOSWHJGELCI675 | RMOSWHJGELCI675-vbhcsmtr | 2015-01-21 02:39:48+00:00 | 2015-01-21 02:40:00+00:00 | ad | ad_5sec | 0.03 | 8.4 | 2015-01-10 | other_campaign | France |
| 1999 | RMOSWHJGELCI675 | RMOSWHJGELCI675-vbhcsmtr | 2015-01-21 02:39:48+00:00 | 2015-01-21 02:47:12+00:00 | iap | offer5 | 26.09 | 8.4 | 2015-01-10 | other_campaign | France |
| 2000 | GJCXNTWEBIPQ369 | GJCXNTWEBIPQ369-9elq67md | 2015-01-21 03:59:23+00:00 | 2015-01-21 04:06:29+00:00 | ad | ad_5sec | 0.12 | 18.5 | 2015-01-14 | organic | United States |

Notice that the table displays only 10 rows by default, 5 from the top and 5 from the bottom. The grey text on the left of the table indicates the row number, and a blue line helps demarcate the top and bottom rows.

The `preview()` function had a few design goals in mind:

- get the dimensions of the table and display them prominently in the header
- provide the column names and the column types
- have a consistent line height along with a sensible limit to the column width
- use a monospaced typeface having high legibility
- should work for all sorts of tables!

This is a nice drop-in replacement for looking at DataFrames or Ibis tables (the types of tables that Pointblank can work with). If you were to inspect the DuckDB table materialized by `pb.load_dataset(dataset="game_revenue", tbl_type="duckdb")` without `preview()` you'd get this:

``` python
pb.load_dataset(dataset="game_revenue", tbl_type="duckdb")
```

```
DatabaseTable: game_revenue
  player_id        string
  session_id       string
  session_start    timestamp('UTC', 6)
  time             timestamp('UTC', 6)
  item_type        string
  item_name        string
  item_revenue     float64
  session_duration float64
  start_day        date
  acquisition      string
  country          string
```

Which is not nearly as good.

### In closing

We hope this post is a good introduction to Pointblank and that it provides some insight on how Great Tables makes sense for reporting in a different library. If you'd like to learn more about Pointblank, please visit the [project website](https://posit-dev.github.io/pointblank/) and check out the many [examples](https://posit-dev.github.io/pointblank/demos/).
