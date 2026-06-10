# Great Tables `v0.18.0`: Easy Column Spanners and More!

The development of Great Tables continues! We're excited to announce the release of `v0.18.0`, which brings several powerful new features. These features make it even easier to create beautiful, informative tables. The key additions in this release include new methods (and a tweak to an existing one):

- [.tab_spanner_delim()](../../reference/GT.tab_spanner_delim.md#great_tables.GT.tab_spanner_delim): quick spanner creation
- [.fmt_tf()](../../reference/GT.fmt_tf.md#great_tables.GT.fmt_tf): easy boolean value formatting
- [.cols_label_rotate()](../../reference/GT.cols_label_rotate.md#great_tables.GT.cols_label_rotate): enables column label rotation
- [.fmt_datetime()](../../reference/GT.fmt_datetime.md#great_tables.GT.fmt_datetime): added `format_str=` parameter for extra customization

Let's explore each of these interesting new features!


## Quick spanner creation with [tab_spanner_delim()](../../reference/GT.tab_spanner_delim.md#great_tables.GT.tab_spanner_delim)

Working with data that has hierarchical column names can be tedious when manually creating spanners. The new [.tab_spanner_delim()](../../reference/GT.tab_spanner_delim.md#great_tables.GT.tab_spanner_delim) method automates this process by intelligently splitting column names based on a delimiter and creating the appropriate spanner structure.

Here's a practical example using the [towny](../../reference/data.towny.md#great_tables.data.towny) dataset, which contains population data for a collection of municipalities across multiple census years. Let's start by looking at the most populated cities and examining their column structure:


``` python
from great_tables import GT
from great_tables.data import towny
import polars as pl
import polars.selectors as cs

# Create a smaller version of the `towny` dataset
towny_mini = (
    pl.from_pandas(towny)
    .filter(pl.col("csd_type") == "city")
    .sort("population_2021", descending=True)
    .select(
        "name",
        cs.starts_with("population_"),
        cs.starts_with("density_")
    )
    .head(5)
)

# Let's look at the column names
print(towny_mini.columns)
```


    ['name', 'population_1996', 'population_2001', 'population_2006', 'population_2011', 'population_2016', 'population_2021', 'density_1996', 'density_2001', 'density_2006', 'density_2011', 'density_2016', 'density_2021']


Notice how the column names have a clear hierarchical structure with underscores as delimiters. Let's now create a table that takes advantage of this structure:


``` python
(
    GT(towny_mini, rowname_col="name")
    .tab_spanner_delim(delim="_")
    .fmt_integer(columns=cs.contains("population"))
    .fmt_number(columns=cs.contains("density"), decimals=1)
    .tab_header(title="Population and Density Trends from Census Data")
    .opt_align_table_header(align="left")
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="13" class="gt_heading gt_title gt_font_normal">Population and Density Trends from Census Data</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th colspan="6" id="population" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">population</th>
<th colspan="6" id="density" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">density</th>
</tr>
<tr class="gt_col_headings">
<th id="population_1996" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1996</th>
<th id="population_2001" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2001</th>
<th id="population_2006" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2006</th>
<th id="population_2011" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2011</th>
<th id="population_2016" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2016</th>
<th id="population_2021" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2021</th>
<th id="density_1996" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1996</th>
<th id="density_2001" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2001</th>
<th id="density_2006" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2006</th>
<th id="density_2011" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2011</th>
<th id="density_2016" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2016</th>
<th id="density_2021" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2021</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">Toronto</th>
<td class="gt_row gt_right">2,385,421</td>
<td class="gt_row gt_right">2,481,494</td>
<td class="gt_row gt_right">2,503,281</td>
<td class="gt_row gt_right">2,615,060</td>
<td class="gt_row gt_right">2,731,571</td>
<td class="gt_row gt_right">2,794,356</td>
<td class="gt_row gt_right">3,779.8</td>
<td class="gt_row gt_right">3,932.0</td>
<td class="gt_row gt_right">3,966.5</td>
<td class="gt_row gt_right">4,143.6</td>
<td class="gt_row gt_right">4,328.3</td>
<td class="gt_row gt_right">4,427.8</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Ottawa</th>
<td class="gt_row gt_right">721,136</td>
<td class="gt_row gt_right">774,072</td>
<td class="gt_row gt_right">812,129</td>
<td class="gt_row gt_right">883,391</td>
<td class="gt_row gt_right">934,243</td>
<td class="gt_row gt_right">1,017,449</td>
<td class="gt_row gt_right">258.6</td>
<td class="gt_row gt_right">277.6</td>
<td class="gt_row gt_right">291.3</td>
<td class="gt_row gt_right">316.8</td>
<td class="gt_row gt_right">335.1</td>
<td class="gt_row gt_right">364.9</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Mississauga</th>
<td class="gt_row gt_right">544,382</td>
<td class="gt_row gt_right">612,925</td>
<td class="gt_row gt_right">668,599</td>
<td class="gt_row gt_right">713,443</td>
<td class="gt_row gt_right">721,599</td>
<td class="gt_row gt_right">717,961</td>
<td class="gt_row gt_right">1,859.6</td>
<td class="gt_row gt_right">2,093.8</td>
<td class="gt_row gt_right">2,283.9</td>
<td class="gt_row gt_right">2,437.1</td>
<td class="gt_row gt_right">2,465.0</td>
<td class="gt_row gt_right">2,452.6</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Brampton</th>
<td class="gt_row gt_right">268,251</td>
<td class="gt_row gt_right">325,428</td>
<td class="gt_row gt_right">433,806</td>
<td class="gt_row gt_right">523,906</td>
<td class="gt_row gt_right">593,638</td>
<td class="gt_row gt_right">656,480</td>
<td class="gt_row gt_right">1,008.9</td>
<td class="gt_row gt_right">1,223.9</td>
<td class="gt_row gt_right">1,631.5</td>
<td class="gt_row gt_right">1,970.4</td>
<td class="gt_row gt_right">2,232.7</td>
<td class="gt_row gt_right">2,469.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Hamilton</th>
<td class="gt_row gt_right">467,799</td>
<td class="gt_row gt_right">490,268</td>
<td class="gt_row gt_right">504,559</td>
<td class="gt_row gt_right">519,949</td>
<td class="gt_row gt_right">536,917</td>
<td class="gt_row gt_right">569,353</td>
<td class="gt_row gt_right">418.3</td>
<td class="gt_row gt_right">438.4</td>
<td class="gt_row gt_right">451.2</td>
<td class="gt_row gt_right">464.9</td>
<td class="gt_row gt_right">480.1</td>
<td class="gt_row gt_right">509.1</td>
</tr>
</tbody>
</table>


The [.tab_spanner_delim()](../../reference/GT.tab_spanner_delim.md#great_tables.GT.tab_spanner_delim) method recognizes the underscore delimiter and creates a hierarchical structure: `"population"` and `"density"` become top-level spanners, with the years (`1996`, `2001`, `2021`) as the final column labels. This creates a clean, organized appearance that clearly groups related metrics together. And, this one method can be used instead of a combination of [.cols_label()](../../reference/GT.cols_label.md#great_tables.GT.cols_label) and [.tab_spanner()](../../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) (which requires a separate invocation per spanner added).


## Beautiful boolean formatting with [fmt_tf()](../../reference/GT.fmt_tf.md#great_tables.GT.fmt_tf)

Boolean data is common in analytical tables, but raw `True`/`False` values can look unprofessional. The new [.fmt_tf()](../../reference/GT.fmt_tf.md#great_tables.GT.fmt_tf) method provides elegant ways to display boolean data using symbols, words, or custom formatting.

Here's a simple example showing different `tf_style=` options:


``` python
from great_tables import GT
import polars as pl

# Create a simple DF with boolean data
bool_df = pl.DataFrame({
    "feature": ["Premium Sound", "Leather Seats", "Sunroof", "Navigation"],
    "model_a": [True, False, True, True],
    "model_b": [True, True, False, True],
    "model_c": [False, True, True, False]
})

(
    GT(bool_df, rowname_col="feature")
    .fmt_tf(tf_style="check-mark", colors=["green", "red"])
    .tab_header(title="Car Features Comparison", subtitle="Using check-mark style")
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Car Features Comparison</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Using check-mark style</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="model_a" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">model_a</th>
<th id="model_b" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">model_b</th>
<th id="model_c" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">model_c</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">Premium Sound</th>
<td class="gt_row gt_center"><span style="color:green">✔</span></td>
<td class="gt_row gt_center"><span style="color:green">✔</span></td>
<td class="gt_row gt_center"><span style="color:red">✘</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Leather Seats</th>
<td class="gt_row gt_center"><span style="color:red">✘</span></td>
<td class="gt_row gt_center"><span style="color:green">✔</span></td>
<td class="gt_row gt_center"><span style="color:green">✔</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Sunroof</th>
<td class="gt_row gt_center"><span style="color:green">✔</span></td>
<td class="gt_row gt_center"><span style="color:red">✘</span></td>
<td class="gt_row gt_center"><span style="color:green">✔</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Navigation</th>
<td class="gt_row gt_center"><span style="color:green">✔</span></td>
<td class="gt_row gt_center"><span style="color:green">✔</span></td>
<td class="gt_row gt_center"><span style="color:red">✘</span></td>
</tr>
</tbody>
</table>


You can also use different symbols and colors for a more distinctive look:


``` python
(
    GT(bool_df, rowname_col="feature")
    .fmt_tf(tf_style="circles", colors=["#4CAF50", "#F44336"])
    .tab_header(title="Car Features Comparison", subtitle="Using circles style")
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Car Features Comparison</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Using circles style</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="model_a" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">model_a</th>
<th id="model_b" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">model_b</th>
<th id="model_c" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">model_c</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">Premium Sound</th>
<td class="gt_row gt_center"><span style="color:#4CAF50">●</span></td>
<td class="gt_row gt_center"><span style="color:#4CAF50">●</span></td>
<td class="gt_row gt_center"><span style="color:#F44336">⭘</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Leather Seats</th>
<td class="gt_row gt_center"><span style="color:#F44336">⭘</span></td>
<td class="gt_row gt_center"><span style="color:#4CAF50">●</span></td>
<td class="gt_row gt_center"><span style="color:#4CAF50">●</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Sunroof</th>
<td class="gt_row gt_center"><span style="color:#4CAF50">●</span></td>
<td class="gt_row gt_center"><span style="color:#F44336">⭘</span></td>
<td class="gt_row gt_center"><span style="color:#4CAF50">●</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Navigation</th>
<td class="gt_row gt_center"><span style="color:#4CAF50">●</span></td>
<td class="gt_row gt_center"><span style="color:#4CAF50">●</span></td>
<td class="gt_row gt_center"><span style="color:#F44336">⭘</span></td>
</tr>
</tbody>
</table>


The [.fmt_tf()](../../reference/GT.fmt_tf.md#great_tables.GT.fmt_tf) method transforms boolean values into visually appealing symbols that make it easy to quickly scan and compare data across rows and columns.


## Rotating column labels with [cols_label_rotate()](../../reference/GT.cols_label_rotate.md#great_tables.GT.cols_label_rotate)

When dealing with many columns or long column names, horizontal space becomes precious. The [.cols_label_rotate()](../../reference/GT.cols_label_rotate.md#great_tables.GT.cols_label_rotate) method solves this by rotating column labels vertically, allowing for more compact table layouts.

Here's an example where we use the [gtcars](../../reference/data.gtcars.md#great_tables.data.gtcars) dataset to create a table which communicates a feature matrix:


``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars
import polars as pl
import polars.selectors as cs

# Manipulate dataset to create a feature comparison table
gtcars_mini = (
    pl.from_pandas(gtcars)
    .filter(pl.col("year") == 2017)
    .filter(pl.col("ctry_origin").is_in(["Germany", "Italy", "United Kingdom"]))
    .with_columns([
        (pl.col("hp") > 500).alias("High Power"),
        (pl.col("mpg_h") > 25).alias("Fuel Efficient"),
        (pl.col("drivetrain") == "awd").alias("All Wheel Drive"),
        (pl.col("msrp") > 100000).alias("Premium Price"),
        (pl.col("trsmn").str.contains("manual")).alias("Manual Transmission")
    ])
    .select([
        "mfr", "model", "trim",
        "High Power",
        "Fuel Efficient",
        "All Wheel Drive",
        "Premium Price",
        "Manual Transmission"
    ])
    .head(10)
)

(
    GT(gtcars_mini)
    .fmt_tf(
        columns=cs.by_dtype(pl.Boolean),
        tf_style="check-mark",
        colors=["#2E8B57", "#DC143C"]
    )
    .cols_label_rotate(
        columns=cs.by_dtype(pl.Boolean),
        dir="sideways-lr"
    )
    .tab_header(
        title="European Luxury Cars Feature Matrix",
        subtitle="2017 Models with Performance & Luxury Features"
    )
    .opt_stylize(style=1)
    .tab_style(
        style=style.text(size="11px"),
        locations=loc.body()
    )
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">European Luxury Cars Feature Matrix</th>
</tr>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">2017 Models with Performance & Luxury Features</th>
</tr>
<tr class="gt_col_headings">
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th id="trim" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">trim</th>
<th id="High-Power" class="gt_col_heading gt_columns_bottom_border gt_center" style="text-align: left; writing-mode: sideways-lr; vertical-align: middle; padding: 8px 0px;" scope="col">High Power</th>
<th id="Fuel-Efficient" class="gt_col_heading gt_columns_bottom_border gt_center" style="text-align: left; writing-mode: sideways-lr; vertical-align: middle; padding: 8px 0px;" scope="col">Fuel Efficient</th>
<th id="All-Wheel-Drive" class="gt_col_heading gt_columns_bottom_border gt_center" style="text-align: left; writing-mode: sideways-lr; vertical-align: middle; padding: 8px 0px;" scope="col">All Wheel Drive</th>
<th id="Premium-Price" class="gt_col_heading gt_columns_bottom_border gt_center" style="text-align: left; writing-mode: sideways-lr; vertical-align: middle; padding: 8px 0px;" scope="col">Premium Price</th>
<th id="Manual-Transmission" class="gt_col_heading gt_columns_bottom_border gt_center" style="text-align: left; writing-mode: sideways-lr; vertical-align: middle; padding: 8px 0px;" scope="col">Manual Transmission</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left" style="font-size: 11px">Ferrari</td>
<td class="gt_row gt_left" style="font-size: 11px">GTC4Lusso</td>
<td class="gt_row gt_left" style="font-size: 11px">Base Coupe</td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#2E8B57">✔</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#2E8B57">✔</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#2E8B57">✔</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped" style="font-size: 11px">Aston Martin</td>
<td class="gt_row gt_left gt_striped" style="font-size: 11px">DB11</td>
<td class="gt_row gt_left gt_striped" style="font-size: 11px">Base Coupe</td>
<td class="gt_row gt_center gt_striped" style="font-size: 11px"><span style="color:#2E8B57">✔</span></td>
<td class="gt_row gt_center gt_striped" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center gt_striped" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center gt_striped" style="font-size: 11px"><span style="color:#2E8B57">✔</span></td>
<td class="gt_row gt_center gt_striped" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
</tr>
<tr>
<td class="gt_row gt_left" style="font-size: 11px">Lotus</td>
<td class="gt_row gt_left" style="font-size: 11px">Evora</td>
<td class="gt_row gt_left" style="font-size: 11px">2+2 Coupe</td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped" style="font-size: 11px">Porsche</td>
<td class="gt_row gt_left gt_striped" style="font-size: 11px">718 Boxster</td>
<td class="gt_row gt_left gt_striped" style="font-size: 11px">Base Convertible</td>
<td class="gt_row gt_center gt_striped" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center gt_striped" style="font-size: 11px"><span style="color:#2E8B57">✔</span></td>
<td class="gt_row gt_center gt_striped" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center gt_striped" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center gt_striped" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
</tr>
<tr>
<td class="gt_row gt_left" style="font-size: 11px">Porsche</td>
<td class="gt_row gt_left" style="font-size: 11px">718 Cayman</td>
<td class="gt_row gt_left" style="font-size: 11px">Base Coupe</td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#2E8B57">✔</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
<td class="gt_row gt_center" style="font-size: 11px"><span style="color:#DC143C">✘</span></td>
</tr>
</tbody>
</table>


This example demonstrates how both the [.fmt_tf()](../../reference/GT.fmt_tf.md#great_tables.GT.fmt_tf) and [.cols_label_rotate()](../../reference/GT.cols_label_rotate.md#great_tables.GT.cols_label_rotate) methods can work well together. The boolean columns use checkmarks (✓/✗) with custom `colors=`, while the rotated labels save horizontal space in this dense feature matrix. The combination allows you to put more information into a compact and still readable format.


## Enhanced datetime formatting with [fmt_datetime()](../../reference/GT.fmt_datetime.md#great_tables.GT.fmt_datetime)

The [.fmt_datetime()](../../reference/GT.fmt_datetime.md#great_tables.GT.fmt_datetime) method now supports custom format strings through the new `format_str=` parameter, giving you complete control over how datetime values appear in your tables.

Here's an example using the included [gibraltar](../../reference/data.gibraltar.md#great_tables.data.gibraltar) weather dataset:


``` python
from great_tables import GT
from great_tables.data import gibraltar
import polars as pl

# Prepare the meteorological data
gibraltar_mini = (
    pl.from_pandas(gibraltar)
    .with_columns(
        [
            pl.concat_str([pl.col("date"), pl.lit(" "), pl.col("time")])
            .str.strptime(pl.Datetime, format="%Y-%m-%d %H:%M")
            .alias("datetime")
        ]
    )
    .filter(pl.col("datetime").dt.hour().is_in([6, 12, 18]))
    .select(["datetime", "temp", "humidity", "condition"])
    .sort("datetime")
    .head(10)
)

(
    GT(gibraltar_mini)
    .fmt_datetime(
        columns="datetime",
        format_str="%b %d %Y (%a) - %I:%M %p",
    )
    .fmt_number(columns="temp", decimals=1, pattern="{x}°C")
    .fmt_percent(columns="humidity", scale_values=False, decimals=0)
    .cols_label(
        datetime="Time",
        temp="Temperature",
        humidity="Humidity",
        condition="Conditions",
    )
    .tab_header(
        title="Gibraltar Temperature and Humidity Conditions",
        subtitle="Morning, Noon, and Evening Readings"
    )
    .opt_stylize(style=1, color="cyan")
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Gibraltar Temperature and Humidity Conditions</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Morning, Noon, and Evening Readings</th>
</tr>
<tr class="gt_col_headings">
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temperature</th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Humidity</th>
<th id="condition" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Conditions</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">May 01 2023 (Mon) - 06:50 AM</td>
<td class="gt_row gt_right">17.2°C</td>
<td class="gt_row gt_right">1%</td>
<td class="gt_row gt_left">Fair</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped">May 01 2023 (Mon) - 12:20 PM</td>
<td class="gt_row gt_right gt_striped">22.2°C</td>
<td class="gt_row gt_right gt_striped">1%</td>
<td class="gt_row gt_left gt_striped">Fair</td>
</tr>
<tr>
<td class="gt_row gt_right">May 01 2023 (Mon) - 12:50 PM</td>
<td class="gt_row gt_right">22.2°C</td>
<td class="gt_row gt_right">1%</td>
<td class="gt_row gt_left">Fair</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped">May 01 2023 (Mon) - 06:20 PM</td>
<td class="gt_row gt_right gt_striped">20.0°C</td>
<td class="gt_row gt_right gt_striped">1%</td>
<td class="gt_row gt_left gt_striped">Fair</td>
</tr>
<tr>
<td class="gt_row gt_right">May 01 2023 (Mon) - 06:50 PM</td>
<td class="gt_row gt_right">20.0°C</td>
<td class="gt_row gt_right">1%</td>
<td class="gt_row gt_left">Fair</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped">May 02 2023 (Tue) - 06:50 AM</td>
<td class="gt_row gt_right gt_striped">17.8°C</td>
<td class="gt_row gt_right gt_striped">1%</td>
<td class="gt_row gt_left gt_striped">Mostly Cloudy</td>
</tr>
<tr>
<td class="gt_row gt_right">May 02 2023 (Tue) - 12:20 PM</td>
<td class="gt_row gt_right">18.9°C</td>
<td class="gt_row gt_right">1%</td>
<td class="gt_row gt_left">Mostly Cloudy</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped">May 02 2023 (Tue) - 12:50 PM</td>
<td class="gt_row gt_right gt_striped">20.0°C</td>
<td class="gt_row gt_right gt_striped">1%</td>
<td class="gt_row gt_left gt_striped">Mostly Cloudy</td>
</tr>
<tr>
<td class="gt_row gt_right">May 02 2023 (Tue) - 06:20 PM</td>
<td class="gt_row gt_right">22.2°C</td>
<td class="gt_row gt_right">1%</td>
<td class="gt_row gt_left">Fair</td>
</tr>
<tr>
<td class="gt_row gt_right gt_striped">May 02 2023 (Tue) - 06:50 PM</td>
<td class="gt_row gt_right gt_striped">22.2°C</td>
<td class="gt_row gt_right gt_striped">1%</td>
<td class="gt_row gt_left gt_striped">Fair</td>
</tr>
</tbody>
</table>


The custom datetime formatting string in `format_str="%b %d %Y (%a) - %I:%M %p"` creates a readable datetime format that's perfect for weather reporting, showing the day of week, month, day, year, and the time in 12-hour format.


## Acknowledgements and what's next

We're grateful to all the contributors who made this release possible. These new features represent significant improvements for creating space-efficient tables while also maximizing visual appeal.

The combination of these features lets you now create complex, professional tables with hierarchical column structures, boolean indicators, space-saving labels, and nicely formatted datetime displays.

We're always happy to get feedback and hear about how you're using Great Tables:

1.  [GitHub Issues](https://github.com/posit-dev/great-tables/issues)
2.  [GitHub Discussions](https://github.com/posit-dev/great-tables/discussions)
3.  [Discord](https://discord.com/invite/Ux7nrcXHVV)

Keep building those beautiful tables!
