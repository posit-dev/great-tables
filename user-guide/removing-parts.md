# Removing Table Parts

Just as the `tab_*()` family of methods lets you *add* components to a table, the `rm_*()` family lets you *remove* them. This is useful when you're handed a [GT](../reference/GT.md#great_tables.GT) object that already carries a header, footnotes, or spanners (perhaps from a shared helper function or a template) and you'd like to strip a component out rather than rebuild the table from scratch. Every `rm_*()` method returns the [GT](../reference/GT.md#great_tables.GT) object, so these calls chain like any other.

A common workflow where removal shines is when you start with a template or shared helper function that builds a fully-decorated table and then strip away the parts that aren't relevant for a particular audience or context. For example, a detailed report might include footnotes and source notes that provide full attribution and methodology details, while a dashboard version of the same table might strip those away for a cleaner, more compact look. Rather than maintaining two separate table-building functions, you maintain one and selectively remove what you don't need.

To have something to remove, let's build up a table that uses several components at once. We'll take a small slice of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset and give it a header, a stubhead label, a spanner, a footnote, and two source notes.

``` python
from great_tables import GT, md, loc
from great_tables.data import gtcars

gtcars_mini = gtcars[["model", "mfr", "hp", "trq", "msrp"]].head(5)

gt_tbl = (
    GT(gtcars_mini, rowname_col="model")
    .tab_header(title="Five Cars", subtitle="From the gtcars dataset")
    .tab_stubhead(label="car")
    .tab_spanner(label="performance", columns=["hp", "trq"], id="performance")
    .tab_footnote(footnote="Horsepower.", locations=loc.body(columns="hp", rows=[0]))
    .tab_source_note(source_note="Source: the gtcars dataset.")
    .tab_source_note(source_note=md("Prices in *USD*."))
)

gt_tbl
```

| Five Cars                   |         |             |       |          |
|-----------------------------|---------|-------------|-------|----------|
| From the gtcars dataset     |         |             |       |          |
| car                         | mfr     | performance |       | msrp     |
|                             |         | hp          | trq   |          |
| GT                          | Ford    | 1 647.0     | 550.0 | 447000.0 |
| 458 Speciale                | Ferrari | 597.0       | 398.0 | 291744.0 |
| 458 Spider                  | Ferrari | 562.0       | 398.0 | 263553.0 |
| 458 Italia                  | Ferrari | 562.0       | 398.0 | 233509.0 |
| 488 GTB                     | Ferrari | 661.0       | 561.0 | 245400.0 |
| Source: the gtcars dataset. |         |             |       |          |
| Prices in *USD*.            |         |             |       |          |
| 1 Horsepower.               |         |             |       |          |

## Removing the Header

The **Table Header** (the title and optional subtitle) is removed with the [rm_header()](../reference/GT.rm_header.md#great_tables.GT.rm_header) method. It takes no arguments and clears the entire header at once.

``` python
gt_tbl.rm_header()
```

| car                         | mfr     | performance |       | msrp     |
|-----------------------------|---------|-------------|-------|----------|
|                             |         | hp          | trq   |          |
| GT                          | Ford    | 1 647.0     | 550.0 | 447000.0 |
| 458 Speciale                | Ferrari | 597.0       | 398.0 | 291744.0 |
| 458 Spider                  | Ferrari | 562.0       | 398.0 | 263553.0 |
| 458 Italia                  | Ferrari | 562.0       | 398.0 | 233509.0 |
| 488 GTB                     | Ferrari | 661.0       | 561.0 | 245400.0 |
| Source: the gtcars dataset. |         |             |       |          |
| Prices in *USD*.            |         |             |       |          |
| 1 Horsepower.               |         |             |       |          |

## Removing the Stubhead Label

The *stubhead label* is the label that sits above the table stub. It's removed with [rm_stubhead()](../reference/GT.rm_stubhead.md#great_tables.GT.rm_stubhead), which leaves the stub itself in place and takes away only the label.

``` python
gt_tbl.rm_stubhead()
```

| Five Cars                   |         |             |       |          |
|-----------------------------|---------|-------------|-------|----------|
| From the gtcars dataset     |         |             |       |          |
|                             | mfr     | performance |       | msrp     |
|                             |         | hp          | trq   |          |
| GT                          | Ford    | 1 647.0     | 550.0 | 447000.0 |
| 458 Speciale                | Ferrari | 597.0       | 398.0 | 291744.0 |
| 458 Spider                  | Ferrari | 562.0       | 398.0 | 263553.0 |
| 458 Italia                  | Ferrari | 562.0       | 398.0 | 233509.0 |
| 488 GTB                     | Ferrari | 661.0       | 561.0 | 245400.0 |
| Source: the gtcars dataset. |         |             |       |          |
| Prices in *USD*.            |         |             |       |          |
| 1 Horsepower.               |         |             |       |          |

## Removing Source Notes

Source notes live in the **Table Footer**. Calling [rm_source_notes()](../reference/GT.rm_source_notes.md#great_tables.GT.rm_source_notes) with no arguments removes all of them.

``` python
gt_tbl.rm_source_notes()
```

| Five Cars               |         |             |       |          |
|-------------------------|---------|-------------|-------|----------|
| From the gtcars dataset |         |             |       |          |
| car                     | mfr     | performance |       | msrp     |
|                         |         | hp          | trq   |          |
| GT                      | Ford    | 1 647.0     | 550.0 | 447000.0 |
| 458 Speciale            | Ferrari | 597.0       | 398.0 | 291744.0 |
| 458 Spider              | Ferrari | 562.0       | 398.0 | 263553.0 |
| 458 Italia              | Ferrari | 562.0       | 398.0 | 233509.0 |
| 488 GTB                 | Ferrari | 661.0       | 561.0 | 245400.0 |
| 1 Horsepower.           |         |             |       |          |

To remove only *some* of the source notes, supply the `source_notes=` argument with a `0`-based index (or a list of indices) reflecting the order in which the notes were added. Here we drop just the first source note and keep the second.

``` python
gt_tbl.rm_source_notes(source_notes=0)
```

| Five Cars               |         |             |       |          |
|-------------------------|---------|-------------|-------|----------|
| From the gtcars dataset |         |             |       |          |
| car                     | mfr     | performance |       | msrp     |
|                         |         | hp          | trq   |          |
| GT                      | Ford    | 1 647.0     | 550.0 | 447000.0 |
| 458 Speciale            | Ferrari | 597.0       | 398.0 | 291744.0 |
| 458 Spider              | Ferrari | 562.0       | 398.0 | 263553.0 |
| 458 Italia              | Ferrari | 562.0       | 398.0 | 233509.0 |
| 488 GTB                 | Ferrari | 661.0       | 561.0 | 245400.0 |
| Prices in *USD*.        |         |             |       |          |
| 1 Horsepower.           |         |             |       |          |

## Removing Footnotes

Footnotes are removed the same way through the [rm_footnotes()](../reference/GT.rm_footnotes.md#great_tables.GT.rm_footnotes) method. Called without arguments, all footnotes are removed. The `footnotes=` argument accepts a `0`-based index or a list of indices when you want to remove specific ones while keeping the rest.

``` python
gt_tbl.rm_footnotes()
```

| Five Cars                   |         |             |       |          |
|-----------------------------|---------|-------------|-------|----------|
| From the gtcars dataset     |         |             |       |          |
| car                         | mfr     | performance |       | msrp     |
|                             |         | hp          | trq   |          |
| GT                          | Ford    | 647.0       | 550.0 | 447000.0 |
| 458 Speciale                | Ferrari | 597.0       | 398.0 | 291744.0 |
| 458 Spider                  | Ferrari | 562.0       | 398.0 | 263553.0 |
| 458 Italia                  | Ferrari | 562.0       | 398.0 | 233509.0 |
| 488 GTB                     | Ferrari | 661.0       | 561.0 | 245400.0 |
| Source: the gtcars dataset. |         |             |       |          |
| Prices in *USD*.            |         |             |       |          |

## Removing Spanners

Spanners are removed with [rm_spanners()](../reference/GT.rm_spanners.md#great_tables.GT.rm_spanners), which takes away the spanner labels while leaving the underlying columns untouched. With no arguments, all spanners are removed. To target specific ones, pass their ID values to the `spanners=` argument.

``` python
gt_tbl.rm_spanners(spanners="performance")
```

| Five Cars                   |         |         |       |          |
|-----------------------------|---------|---------|-------|----------|
| From the gtcars dataset     |         |         |       |          |
| car                         | mfr     | hp      | trq   | msrp     |
| GT                          | Ford    | 1 647.0 | 550.0 | 447000.0 |
| 458 Speciale                | Ferrari | 597.0   | 398.0 | 291744.0 |
| 458 Spider                  | Ferrari | 562.0   | 398.0 | 263553.0 |
| 458 Italia                  | Ferrari | 562.0   | 398.0 | 233509.0 |
| 488 GTB                     | Ferrari | 661.0   | 561.0 | 245400.0 |
| Source: the gtcars dataset. |         |         |       |          |
| Prices in *USD*.            |         |         |       |          |
| 1 Horsepower.               |         |         |       |          |

Spanners can also be removed by *level* using the `levels=` argument. Levels are numbered starting at `0` for the row of spanners closest to the column labels, increasing as you move upward. This is handy when a table has stacked (nested) spanners and you want to clear an entire tier at once. When both `spanners=` and `levels=` are supplied, only the spanners that match *both* conditions are removed.

The ability to remove by level is especially useful when working with deeply nested spanners (spanners that span other spanners). Rather than tracking individual spanner IDs (which can become unwieldy as the number of spanners grows) you can clear an entire tier at once. For instance, if you have a three-level spanner hierarchy and want to simplify the table down to a single level, two [rm_spanners()](../reference/GT.rm_spanners.md#great_tables.GT.rm_spanners) calls with the appropriate `levels=` values will do the job cleanly.

The `rm_*()` methods round out the table-building workflow: the `tab_*()` methods put components in place, and their `rm_*()` counterparts take them back out. Because each returns a [GT](../reference/GT.md#great_tables.GT) object, you can freely mix additions and removals within a single chain, which makes it easy to adapt a table that was created elsewhere to suit your needs.
