---
name: great-tables
description: How to create effective display tables with Great Tables
---

# Philosophy of Great Tables

Great Tables is for building display tables and these are tables meant for people (not for computation). So the end goal really is communication. We should strive to convey data with clarity, hierarchy, and visual polish. You could think of it as typesetting for tabular data.

## The DataFrame Comes First in the Process

The input DataFrame should already be in presentation-ready shape. Use Polars or Pandas to do the heavy lifting (e.g., sorting, filtering, aggregations, pivots, etc.) before passing the DataFrame to `GT()`. Great Tables is not a data wrangling tool. Rather, it's the presentation layer. So if your table needs reshaping, do that upstream.

## Structure Communicates Meaning

Use a stub column to give each row a clear identity. This anchors the reader and distinguishes records. Set via `rowname_col=` in `GT()`. For tables with natural categorical divisions among rows, group them into row group. This introduces visual breaks and some semantic hierarchy. Set them with `GT(groupname_col=)`. When columns belong to logical categories, use column spanners to span them with a header label. This reduces cognitive load and signals relationships. Use `.tab_spanner()` for this.

## Having Context is Great for the Reader of the Table

It's best to have a table with a title (and an optional subtitle). So use `.tab_header()` to let readers know what the table is about. And it's good to cite your data or add clarifying notes at the bottom with `.tab_source_note()` (you can add multiple notes with repeated uses of that method).

## Formatting is Essential for Adhering to Standards of Communication

Raw/unformatted numbers are not usually good in a presentation table. We expect to see things like thousands separators, appropriate decimal precision, currency symbols, percentages, dates in readable formats, etc. Here are a few examples of the `.fmt_*()` family of formatting methods:

- `.fmt_number()` for general number formatting
- `.fmt_integer()` when decimal precision is not needed
- `.fmt_currency()` for money
- `.fmt_percent()` for percentage values
- `.fmt_date()`/`.fmt_datetime()` for fine control of dates and times

Basically, one might say that unformatted numbers makes a table look unfinished.

## Handle Missing Values Gracefully

Empty cells or `None` values should always be handled for presentation. Use `.sub_missing()` to replace them with an em-dash (`—`) or text that's appropriate to the context (e.g., `"N/A"`, `"nil"`, `"<dl"`, etc.).

## Styling: Broad and Fine

There are many ways to add styling to the display table, here are the ways to do it:

- `.tab_options()`: for sweeping style changes (e.g., fonts, colors, border styles, padding, etc.) applied to entire locations (e.g., body, header, footer, etc.)
- `.tab_style()`: for more precision, like, highlighting a specific cell, emboldening a row, adding a background color to a column; combine with `loc.*` location helpers for targeting
- `.data_color()`: this is heat-mapping for numeric or categorical columns, turning numbers into visual gradients and making patterns clear (i.e., without requiring the reader to carefully parse the digits)

## Column Widths Matter

Browsers will auto-size columns, and sometimes in ways that aren't visually satisfying. Use `.cols_width()` to assert control and specify your preferred widths. Balanced column widths create visual harmony and prevent awkward text wrapping or excessive whitespace.

## Selecting Columns and Rows Intelligently

- the `columns=` parameter accepts Polars selectors (e.g., `cs.starts_with("pct_")`, `cs.numeric()`, etc.) so use these to apply formatting or styling to groups of columns without enumerating them
- the `rows=` parameter accepts Polars expressions for conditional targeting (e.g., `pl.col("value") > 100`); this lets you style outliers, highlight thresholds, or format specific segments
- remember to use `import polars.selectors as cs` before the code

## Respect the Reader's Viewport

A great table fits its context and shouldn't be overwhelming. So if you have a table where a user has to scroll down a table a great amound, you need to put some consideration on either summarizing the data or leaving some of the data out (data which doesn't serve the main point of the table).

There's also another sizing issue: tables that are too wide. To avoid having to make the user needlessly scroll horizontally, try omitting some columns (perhaps make a second table with them?), abbreviating content (e.g., shortening text, using short-forms for terms, etc.), or transposing/pivoting the table (going from wide to narrow).

## Summary of Important Design Decissions

1. prepare your data before introducing it to Great Tables
2. use structure (stub, groups, spanners) to add hierarchy
3. always add a title/subtitle and add table notes when useful
4. format every number consistent with expectations (3.4532 -> $3.45)
5. style intentionally (broad strokes first, then more precisely)
6. handle missing values explicitly
7. control column widths for visual balance
8. leverage selectors and expressions for formatting/styling efficiently (less method calls)
9. keep tables appropriately sized for their medium

Making a great table in Great Tables requires some thoughtfulness. Though the API has many methods the philosophy is somewhat simple: make data easy to read.
