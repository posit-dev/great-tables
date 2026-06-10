# Formatting Values

The values within the table body, specifically those within the body cells, can be formatted with a large selection of `fmt_*()` methods like [fmt_number()](../reference/GT.fmt_number.md#great_tables.GT.fmt_number), [fmt_integer()](../reference/GT.fmt_integer.md#great_tables.GT.fmt_integer), [fmt_scientific()](../reference/GT.fmt_scientific.md#great_tables.GT.fmt_scientific), and more. Let's use a portion of the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset and introduce some formatting to the cell values. First, we'll generate the basic GT object and take a look at the table without any cell formatting applied.


``` python
from great_tables import GT
from great_tables.data import exibble
from great_tables import vals

gt_ex = GT(exibble[["num", "date", "time", "currency"]].head(5))

gt_ex
```


| num    | date       | time  | currency |
|--------|------------|-------|----------|
| 0.1111 | 2015-01-15 | 13:35 | 49.95    |
| 2.222  | 2015-02-15 | 14:40 | 17.95    |
| 33.33  | 2015-03-15 | 15:45 | 1.39     |
| 444.4  | 2015-04-15 | 16:50 | 65100.0  |
| 5550.0 | 2015-05-15 | 17:55 | 1325.81  |


The `num` column contains both small and much larger numbers. We can use the [fmt_number()](../reference/GT.fmt_number.md#great_tables.GT.fmt_number) method to obtain formatted values have a fixed level of decimal precision and grouping separators. At the same time, we'll format the numeric values in `currency` column to get monetary values.


``` python
gt_ex = gt_ex.fmt_number(columns="num", decimals=2).fmt_currency(columns="currency")

gt_ex
```


| num      | date       | time  | currency    |
|----------|------------|-------|-------------|
| 0.11     | 2015-01-15 | 13:35 | \$49.95     |
| 2.22     | 2015-02-15 | 14:40 | \$17.95     |
| 33.33    | 2015-03-15 | 15:45 | \$1.39      |
| 444.40   | 2015-04-15 | 16:50 | \$65,100.00 |
| 5,550.00 | 2015-05-15 | 17:55 | \$1,325.81  |


Dates and times can be formatted as well. As long as they are in ISO 8601 form, the [fmt_date()](../reference/GT.fmt_date.md#great_tables.GT.fmt_date) and [fmt_time()](../reference/GT.fmt_time.md#great_tables.GT.fmt_time) methods can be used to format such values. These methods have corresponding `date_style=` and `time_style=` arguments that accept a number of keywords that act as preset formatting styles.


``` python
gt_ex = (
    gt_ex.fmt_date(columns="date", date_style="m_day_year")
    .fmt_time(columns="time", time_style="h_m_p")
)

gt_ex
```


| num      | date         | time    | currency    |
|----------|--------------|---------|-------------|
| 0.11     | Jan 15, 2015 | 1:35 PM | \$49.95     |
| 2.22     | Feb 15, 2015 | 2:40 PM | \$17.95     |
| 33.33    | Mar 15, 2015 | 3:45 PM | \$1.39      |
| 444.40   | Apr 15, 2015 | 4:50 PM | \$65,100.00 |
| 5,550.00 | May 15, 2015 | 5:55 PM | \$1,325.81  |


It's possible to format cells that have already been formatted. Using a formatting method again on previously formatted cells will always work within the 'last-formatted-wins' rule.


``` python
gt_ex = gt_ex.fmt_date(columns="date", date_style="wday_day_month_year")

gt_ex
```


| num      | date                     | time    | currency    |
|----------|--------------------------|---------|-------------|
| 0.11     | Thursday 15 January 2015 | 1:35 PM | \$49.95     |
| 2.22     | Sunday 15 February 2015  | 2:40 PM | \$17.95     |
| 33.33    | Sunday 15 March 2015     | 3:45 PM | \$1.39      |
| 444.40   | Wednesday 15 April 2015  | 4:50 PM | \$65,100.00 |
| 5,550.00 | Friday 15 May 2015       | 5:55 PM | \$1,325.81  |


Within the selected `columns=` we can choose to target specific cells with the `rows=` argument. The latter argument allows us to pass in a list of row indices.


``` python
gt_ex = gt_ex.fmt_currency(columns="currency", rows=[2, 3, 4], currency="GBP")

gt_ex
```


| num      | date                     | time    | currency   |
|----------|--------------------------|---------|------------|
| 0.11     | Thursday 15 January 2015 | 1:35 PM | \$49.95    |
| 2.22     | Sunday 15 February 2015  | 2:40 PM | \$17.95    |
| 33.33    | Sunday 15 March 2015     | 3:45 PM | £1.39      |
| 444.40   | Wednesday 15 April 2015  | 4:50 PM | £65,100.00 |
| 5,550.00 | Friday 15 May 2015       | 5:55 PM | £1,325.81  |


# Arguments Common to Several Formatting Methods/Functions

While we can use the `fmt_*()` methods on a table, we can also use the functional versions of these methods on scalar values or lists of values. These variants exist within the `vals` module. While arguments across these functions and their corresponding method aren't exactly the same, there are nonetheless many arguments that are shared amongst them. Here are a few examples:

- `decimals=`: set a fixed precision of decimal places
- `sep_mark=`, `dec_mark=`: set digit separators and the decimal symbol (defaults are `","` and `"."`)
- `scale_by=`: we can choose to scale targeted values by a multiplier value
- `compact=`: larger figures (thousands, millions, etc.) can be autoscaled and decorated with the appropriate suffixes (e.g., `"10000"` becomes `"10K"`)
- `pattern=`: option to use a text pattern for decoration of the formatted values
- `locale=`: providing a locale ID (e.g., `"en"`, `"fr"`, `"de-AT"`, etc.) will result in numeric formatting specific to the chosen locale

Here are a number of examples that use [vals.fmt_number()](../reference/vals.fmt_number.md#great_tables.vals.fmt_number).


``` python
fmt_number_1 = vals.fmt_number([1.64, 3.26, 3000.63, 236742.37])
fmt_number_2 = vals.fmt_number([1.64, 3.26, 3000.63, 236742.37], compact=True)
fmt_number_3 = vals.fmt_number([1.64, 3.26, 3000.63, 236742.37], decimals=3)
fmt_number_4 = vals.fmt_number([1.64, 3.26, 3000.63, 236742.37], pattern="[{x}]")
fmt_number_5 = vals.fmt_number([1.64, 3.26, 3000.63, 236742.37], locale="es")

print(fmt_number_1, fmt_number_2, fmt_number_3, fmt_number_4, fmt_number_5, sep="\n")
```


    ['1.64', '3.26', '3,000.63', '236,742.37']
    ['1.64', '3.26', '3.00K', '236.74K']
    ['1.640', '3.260', '3,000.630', '236,742.370']
    ['[1.64]', '[3.26]', '[3,000.63]', '[236,742.37]']
    ['1,64', '3,26', '3.000,63', '236.742,37']


Scientific notation can be done with [vals.fmt_scientific()](../reference/vals.fmt_scientific.md#great_tables.vals.fmt_scientific).


``` python
fmt_sci_1 = vals.fmt_scientific([0.00064, 7.353, 863454.63])
fmt_sci_2 = vals.fmt_scientific([1.64, 3.26, 3000.63], decimals=3)
fmt_sci_3 = vals.fmt_scientific([1.64, 3.26, 3000.63], exp_style="E")
fmt_sci_4 = vals.fmt_scientific([1.64, 3.26, 3000.63], locale="de")

print(fmt_sci_1, fmt_sci_2, fmt_sci_3, fmt_sci_4, sep="\n")
```


    ["6.40 × 10<sup style='font-size: 65%;'>−4</sup>", '7.35', "8.63 × 10<sup style='font-size: 65%;'>5</sup>"]
    ['1.640', '3.260', "3.001 × 10<sup style='font-size: 65%;'>3</sup>"]
    ['1.64E00', '3.26E00', '3.00E03']
    ['1,64', '3,26', "3,00 × 10<sup style='font-size: 65%;'>3</sup>"]


Dates and times are handled with [vals.fmt_date()](../reference/vals.fmt_date.md#great_tables.vals.fmt_date) and [vals.fmt_time()](../reference/vals.fmt_time.md#great_tables.vals.fmt_time).


``` python
fmt_date_1 = vals.fmt_date(
    ["2015-03-15", "2017-08-18", "2020-04-12"], date_style="wday_month_day_year"
)
fmt_date_2 = vals.fmt_date(["2015-03-15", "2017-08-18", "2020-04-12"], date_style="month_day_year")
fmt_time_1 = vals.fmt_time(["23:03", "00:55", "08:23"], time_style="h_m_p")
fmt_time_2 = vals.fmt_time(["23:03", "00:55", "08:23"], time_style="h_p")

print(fmt_date_1, fmt_date_2, fmt_time_1, fmt_time_2, sep="\n")
```


    ['Sunday, March 15, 2015', 'Friday, August 18, 2017', 'Sunday, April 12, 2020']
    ['March 15, 2015', 'August 18, 2017', 'April 12, 2020']
    ['11:03 PM', '12:55 AM', '8:23 AM']
    ['11 PM', '12 AM', '8 AM']


Sometimes it's easier and more convenient to experiment with formatting using the formatting functions in the `vals` module. There are many options to explore with each type of formatting and so visiting the [API Reference](../reference/) is certainly worthwhile.
