# Footnotes

Footnotes provide a way to annotate specific cells, columns, or other table parts with additional context without cluttering the main display. **Great Tables** manages footnotes as a system: marks are automatically sequenced, placed consistently, and matched to their explanatory text in the table footer.

Footnotes are best suited for cell-specific or column-specific context that would clutter the main display if placed inline. For information that applies to the entire table, a source note in the footer (via [tab_source_note()](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note)) is usually a better fit because it avoids attaching a mark to any one location. And for systematic column descriptions, such as units or definitions, consider relabeling the column itself so the context is always visible without requiring the reader to look down at the footer.

## A Basic Footnote

Adding a footnote requires two things: the footnote text and a location specifier indicating where the footnote mark should appear. The [tab_footnote()](../reference/GT.tab_footnote.md#great_tables.GT.tab_footnote) method handles both, placing the mark at the targeted location and appending the text to the footer.

``` python
from great_tables import GT, md, loc
from great_tables.data import gibraltar

weather_mini = gibraltar.head(5)[["date", "time", "temp", "humidity", "wind_speed", "pressure"]]

(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Air temperature in degrees Celsius.",
        locations=loc.column_labels(columns="temp")
    )
)
```

| Weather at Gibraltar Airport |  |  |  |  |  |
|----|----|----|----|----|----|
| Observations on May 1, 2023 |  |  |  |  |  |
| date | time | temp1 | humidity | wind_speed | pressure |
| 2023-05-01 | 00:20 | 18.9 | 0.68 | 6.7 | 1015.2 |
| 2023-05-01 | 00:50 | 18.9 | 0.73 | 7.2 | 1015.2 |
| 2023-05-01 | 01:20 | 17.8 | 0.77 | 6.7 | 1014.6 |
| 2023-05-01 | 01:50 | 18.9 | 0.73 | 6.7 | 1014.6 |
| 2023-05-01 | 02:20 | 18.9 | 0.68 | 6.7 | 1014.6 |
| 1 Air temperature in degrees Celsius. |  |  |  |  |  |

The footnote mark (a superscript number) appears next to the `"temp"` column label, and the corresponding text appears at the bottom of the table.

## Targeting Different Locations

Footnotes can be attached to many different parts of the table. The `locations=` argument accepts any of the `loc` specifiers that support footnotes. Here are some of the most common targets.

### Column Labels

Attaching a footnote to a column label is useful for clarifying units or methodology.

``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Relative humidity, as a value between 0 and 1.",
        locations=loc.column_labels(columns="humidity")
    )
)
```

| Weather at Gibraltar Airport |  |  |  |  |  |
|----|----|----|----|----|----|
| Observations on May 1, 2023 |  |  |  |  |  |
| date | time | temp | humidity1 | wind_speed | pressure |
| 2023-05-01 | 00:20 | 18.9 | 0.68 | 6.7 | 1015.2 |
| 2023-05-01 | 00:50 | 18.9 | 0.73 | 7.2 | 1015.2 |
| 2023-05-01 | 01:20 | 17.8 | 0.77 | 6.7 | 1014.6 |
| 2023-05-01 | 01:50 | 18.9 | 0.73 | 6.7 | 1014.6 |
| 2023-05-01 | 02:20 | 18.9 | 0.68 | 6.7 | 1014.6 |
| 1 Relative humidity, as a value between 0 and 1. |  |  |  |  |  |

### Body Cells

You can annotate specific data cells by targeting them with [loc.body()](../reference/loc.body.md#great_tables.loc.body).

``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Lowest temperature in this sample.",
        locations=loc.body(columns="temp", rows=[2])
    )
)
```

| Weather at Gibraltar Airport |  |  |  |  |  |
|----|----|----|----|----|----|
| Observations on May 1, 2023 |  |  |  |  |  |
| date | time | temp | humidity | wind_speed | pressure |
| 2023-05-01 | 00:20 | 18.9 | 0.68 | 6.7 | 1015.2 |
| 2023-05-01 | 00:50 | 18.9 | 0.73 | 7.2 | 1015.2 |
| 2023-05-01 | 01:20 | 1 17.8 | 0.77 | 6.7 | 1014.6 |
| 2023-05-01 | 01:50 | 18.9 | 0.73 | 6.7 | 1014.6 |
| 2023-05-01 | 02:20 | 18.9 | 0.68 | 6.7 | 1014.6 |
| 1 Lowest temperature in this sample. |  |  |  |  |  |

### The Title or Subtitle

Footnotes on the table header can provide methodological notes or data source context.

``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Data collected at the airport's weather station, 5 m above mean sea level.",
        locations=loc.title()
    )
)
```

| Weather at Gibraltar Airport1 |  |  |  |  |  |
|----|----|----|----|----|----|
| Observations on May 1, 2023 |  |  |  |  |  |
| date | time | temp | humidity | wind_speed | pressure |
| 2023-05-01 | 00:20 | 18.9 | 0.68 | 6.7 | 1015.2 |
| 2023-05-01 | 00:50 | 18.9 | 0.73 | 7.2 | 1015.2 |
| 2023-05-01 | 01:20 | 17.8 | 0.77 | 6.7 | 1014.6 |
| 2023-05-01 | 01:50 | 18.9 | 0.73 | 6.7 | 1014.6 |
| 2023-05-01 | 02:20 | 18.9 | 0.68 | 6.7 | 1014.6 |
| 1 Data collected at the airport's weather station, 5 m above mean sea level. |  |  |  |  |  |

## Multiple Footnotes

You can add multiple footnotes to a single table. Each call to [tab_footnote()](../reference/GT.tab_footnote.md#great_tables.GT.tab_footnote) creates a new footnote with its own sequenced mark. The marks are numbered in the order they appear in the table (reading left-to-right, top-to-bottom).

``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Air temperature in degrees Celsius.",
        locations=loc.column_labels(columns="temp")
    )
    .tab_footnote(
        footnote="Atmospheric pressure in hectopascals.",
        locations=loc.column_labels(columns="pressure")
    )
    .tab_footnote(
        footnote="Highest wind speed in this sample.",
        locations=loc.body(columns="wind_speed", rows=[1])
    )
)
```

| Weather at Gibraltar Airport |  |  |  |  |  |
|----|----|----|----|----|----|
| Observations on May 1, 2023 |  |  |  |  |  |
| date | time | temp1 | humidity | wind_speed | pressure2 |
| 2023-05-01 | 00:20 | 18.9 | 0.68 | 6.7 | 1015.2 |
| 2023-05-01 | 00:50 | 18.9 | 0.73 | 3 7.2 | 1015.2 |
| 2023-05-01 | 01:20 | 17.8 | 0.77 | 6.7 | 1014.6 |
| 2023-05-01 | 01:50 | 18.9 | 0.73 | 6.7 | 1014.6 |
| 2023-05-01 | 02:20 | 18.9 | 0.68 | 6.7 | 1014.6 |
| 1 Air temperature in degrees Celsius. |  |  |  |  |  |
| 2 Atmospheric pressure in hectopascals. |  |  |  |  |  |
| 3 Highest wind speed in this sample. |  |  |  |  |  |

Three footnote marks are placed in the table, and three corresponding notes appear in the footer, each with its sequential number.

While you can add many footnotes to a single table, use restraint. More than three or four footnotes can overwhelm the reader and make the footer itself difficult to navigate. If you find yourself adding footnotes to most cells, consider whether the information would be better conveyed through more descriptive column labels, a subtitle, or a separate explanatory paragraph outside the table.

## Footnotes Without a Mark

If you want to include explanatory text in the footer without attaching a mark to any cell, omit the `locations=` argument (or set it to `None`).

``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(footnote="All observations are from Gibraltar Airport, May 2023.")
)
```

| Weather at Gibraltar Airport |  |  |  |  |  |
|----|----|----|----|----|----|
| Observations on May 1, 2023 |  |  |  |  |  |
| date | time | temp | humidity | wind_speed | pressure |
| 2023-05-01 | 00:20 | 18.9 | 0.68 | 6.7 | 1015.2 |
| 2023-05-01 | 00:50 | 18.9 | 0.73 | 7.2 | 1015.2 |
| 2023-05-01 | 01:20 | 17.8 | 0.77 | 6.7 | 1014.6 |
| 2023-05-01 | 01:50 | 18.9 | 0.73 | 6.7 | 1014.6 |
| 2023-05-01 | 02:20 | 18.9 | 0.68 | 6.7 | 1014.6 |
| All observations are from Gibraltar Airport, May 2023. |  |  |  |  |  |

This is useful for general notes that apply to the entire table rather than to a specific cell or label. Markless footnotes work well for disclaimers, methodological notes, or data-source attributions that apply broadly rather than to any single cell. Because they carry no superscript mark, they read as supplementary context for the table as a whole.

## Controlling Mark Placement

The `placement=` argument determines where the footnote mark appears relative to the cell content. The options are `"auto"` (the default), `"left"`, and `"right"`.

``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Wind speed in meters per second.",
        locations=loc.column_labels(columns="wind_speed"),
        placement="left"
    )
)
```

| Weather at Gibraltar Airport       |       |      |          |              |          |
|------------------------------------|-------|------|----------|--------------|----------|
| Observations on May 1, 2023        |       |      |          |              |          |
| date                               | time  | temp | humidity | 1 wind_speed | pressure |
| 2023-05-01                         | 00:20 | 18.9 | 0.68     | 6.7          | 1015.2   |
| 2023-05-01                         | 00:50 | 18.9 | 0.73     | 7.2          | 1015.2   |
| 2023-05-01                         | 01:20 | 17.8 | 0.77     | 6.7          | 1014.6   |
| 2023-05-01                         | 01:50 | 18.9 | 0.73     | 6.7          | 1014.6   |
| 2023-05-01                         | 02:20 | 18.9 | 0.68     | 6.7          | 1014.6   |
| 1 Wind speed in meters per second. |       |      |          |              |          |

With `placement="left"`, the footnote mark appears before the cell text rather than after it.

## Using Markdown in Footnotes

Footnote text supports Markdown formatting through the [md()](../reference/md.md#great_tables.md) helper function. This lets you include emphasis, links, or other inline formatting in your footnotes.

``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote=md("Observations from the *Gibraltar Airport Station* (GIB)."),
        locations=loc.title()
    )
)
```

| Weather at Gibraltar Airport1 |  |  |  |  |  |
|----|----|----|----|----|----|
| Observations on May 1, 2023 |  |  |  |  |  |
| date | time | temp | humidity | wind_speed | pressure |
| 2023-05-01 | 00:20 | 18.9 | 0.68 | 6.7 | 1015.2 |
| 2023-05-01 | 00:50 | 18.9 | 0.73 | 7.2 | 1015.2 |
| 2023-05-01 | 01:20 | 17.8 | 0.77 | 6.7 | 1014.6 |
| 2023-05-01 | 01:50 | 18.9 | 0.73 | 6.7 | 1014.6 |
| 2023-05-01 | 02:20 | 18.9 | 0.68 | 6.7 | 1014.6 |
| 1 Observations from the *Gibraltar Airport Station* (GIB). |  |  |  |  |  |

Footnotes are a subtle but important tool for building informative tables. They let you add precision and context where it matters most, keeping the main table body clean while ensuring readers have access to the details they need. The automatic sequencing and placement system means you can focus on content rather than managing mark numbers manually.
