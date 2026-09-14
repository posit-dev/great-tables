# Glossary

Terms used throughout the Great Tables documentation, listed alphabetically. Where a term has a direct counterpart in the API, the relevant class, method, or module is noted.

Body  
The main data area of the table, consisting of rows and columns of cells that hold the underlying data values (after any formatting or substitution has been applied). The body excludes the **header**, **column header**, **stub**, **footer**, and any **summary rows**. Targetable with [loc.body()](../reference/loc.body.md#great_tables.loc.body).

Cell  
A single value at the intersection of a row and a column within the **body**, **stub**, or **summary rows**. Cells are the fundamental unit that **formatters**, **styles**, and **footnotes** act upon.

Column header  
The region directly above the **body** that contains all **column labels** and any **spanner labels**. It provides the labeling structure that maps data columns to their display names and groupings. Targetable as a whole with [loc.column_header()](../reference/loc.column_header.md#great_tables.loc.column_header).

Column labels  
The individual text labels that identify each column in the table. By default they are the column names from the input DataFrame, but they can be overridden with [cols_label()](../reference/GT.cols_label.md#great_tables.GT.cols_label) or transformed with [cols_label_with()](../reference/GT.cols_label_with.md#great_tables.GT.cols_label_with). Targetable with [loc.column_labels()](../reference/loc.column_labels.md#great_tables.loc.column_labels).

Column selector  
An expression passed to a `columns=` parameter to identify which columns an operation should act on. Accepts a column name (string), a list of names, an integer index, a Polars selector expression (e.g., `cs.numeric()`), or a callable that takes a column name and returns a boolean. Column selectors are used throughout the API in methods like `fmt_number()`, [cols_align()](../reference/GT.cols_align.md#great_tables.GT.cols_align), [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style), and many others.

Data color  
A technique for colorizing **cell** backgrounds based on data values, providing a visual encoding of magnitude or category directly in the table. Applied with [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color), which supports custom palettes, ColorBrewer palettes, domain specification, and automatic contrasting text color.

Footer  
The bottom region of the table, below the **body** and any **summary rows**. It contains **footnotes** and **source notes**. Targetable as a whole with [loc.footer()](../reference/loc.footer.md#great_tables.loc.footer).

Footnote  
An annotation consisting of two linked parts: a **footnote mark** placed at a specific location in the table, and the corresponding footnote text rendered in the **footer**. Added with [tab_footnote()](../reference/GT.tab_footnote.md#great_tables.GT.tab_footnote). When multiple footnotes share the same text, the mark is reused rather than duplicated.

Footnote mark  
A small symbol (number, letter, or typographic symbol) attached to a **cell** or label in the table that links it to its corresponding **footnote** text in the **footer**. Marks are ordered left-to-right, top-to-bottom according to their position in the table. The mark style is configured with [opt_footnote_marks()](../reference/GT.opt_footnote_marks.md#great_tables.GT.opt_footnote_marks), which accepts keywords like `"numbers"` (the default), `"letters"`, `"LETTERS"`, `"standard"` (four traditional symbols), or `"extended"` (six symbols), as well as custom lists of strings.

Formatter  
A method that transforms how raw data values are displayed in **cells** without altering the underlying data. All built-in formatters follow the `fmt_*()` naming convention (e.g., `fmt_number()`, `fmt_currency()`, `fmt_date()`). A general-purpose [fmt()](../reference/GT.fmt.md#great_tables.GT.fmt) method accepts a custom formatting function. The `vals` module provides standalone equivalents for use outside a [GT](../reference/GT.md#great_tables.GT) object, such as in **summary rows** definitions.

Grand summary rows  
Aggregation rows that summarize the entire table's data, regardless of **row groups**. Created with [grand_summary_rows()](../reference/GT.grand_summary_rows.md#great_tables.GT.grand_summary_rows) and placed at the very bottom of the **body** (above the **footer**). Targetable with [loc.grand_summary()](../reference/loc.grand_summary.md#great_tables.loc.grand_summary).

GT object  
The central object in Great Tables, created by passing a Pandas or Polars DataFrame to [GT()](../reference/GT.md#great_tables.GT). All table-building operations are methods on this object and return a modified copy, enabling method chaining. Optional constructor arguments include `rowname_col` (to create a **stub**), `groupname_col` (to create **row groups**), `locale`, and `id`.

Header  
The topmost region of the table, positioned above the **column header**. It contains the **title** and optionally a **subtitle**. Set with [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header). Targetable as a whole with [loc.header()](../reference/loc.header.md#great_tables.loc.header).

Hidden column  
A column that is present in the underlying data but not rendered in the output table. Columns can be hidden with [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide) and restored with [cols_unhide()](../reference/GT.cols_unhide.md#great_tables.GT.cols_unhide). Hidden columns remain accessible for operations like **merged columns** patterns, **data color** mapping, and [from_column()](../reference/from_column.md#great_tables.from_column) references.

Locale  
A language/region identifier (e.g., `"en"`, `"de"`, `"fr-CA"`) that controls how **formatters** render numbers, currencies, dates, and times. Locale determines things like the decimal mark, digit grouping separator, currency symbol, and date/time patterns. Set at the table level with `GT(locale=...)` or [with_locale()](../reference/GT.with_locale.md#great_tables.GT.with_locale), or overridden per formatter call.

Location selector  
An object from the `loc` module that identifies a specific region or set of **cells** in the table. Location selectors are used in [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) to target where styles are applied and in [tab_footnote()](../reference/GT.tab_footnote.md#great_tables.GT.tab_footnote) to place **footnote marks**. Examples include [loc.body()](../reference/loc.body.md#great_tables.loc.body), [loc.column_labels()](../reference/loc.column_labels.md#great_tables.loc.column_labels), [loc.stub()](../reference/loc.stub.md#great_tables.loc.stub), and [loc.header()](../reference/loc.header.md#great_tables.loc.header).

Merged columns  
A display technique that combines content from multiple columns into a single column using a pattern string. Created with [cols_merge()](../reference/GT.cols_merge.md#great_tables.GT.cols_merge), where the pattern uses `{0}`, `{1}`, etc. to reference column values (e.g., `"{0} ({1})"`). Conditional removal of content when values are missing is supported via `<<`/`>>` delimiters in the pattern. Convenience variants include [cols_merge_uncert()](../reference/GT.cols_merge_uncert.md#great_tables.GT.cols_merge_uncert), [cols_merge_range()](../reference/GT.cols_merge_range.md#great_tables.GT.cols_merge_range), and [cols_merge_n_pct()](../reference/GT.cols_merge_n_pct.md#great_tables.GT.cols_merge_n_pct).

Nanoplot  
A tiny inline visualization embedded directly in a table **cell** via [fmt_nanoplot()](../reference/GT.fmt_nanoplot.md#great_tables.GT.fmt_nanoplot). Supports `"line"` and `"bar"` plot types, with optional reference lines, reference areas, and automatic y-axis scaling across rows. Appearance is customized through [nanoplot_options()](../reference/nanoplot_options.md#great_tables.nanoplot_options).

Preheader  
Optional content rendered above the table element itself (before the **header**). Set via `tab_header(preheader=...)`. Accepts raw HTML strings and is useful for adding non-tabular content like badges or links that sit outside the table's visual boundaries.

Row group  
A categorical label that divides the **body** into logical sections of rows. Row groups appear as spanning labels across the full width of the table. Created by passing `groupname_col=` to [GT()](../reference/GT.md#great_tables.GT) and ordered with `row_group_order()`. Targetable with [loc.row_groups()](../reference/loc.row_groups.md#great_tables.loc.row_groups).

Row selector  
An expression passed to a `rows=` parameter to identify which rows an operation should act on. Accepts an integer index, a list of indices, a list of row names (when a **stub** is present), a Polars expression, or a callable. Row selectors are used in methods like `fmt_number()`, [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style), [cols_merge()](../reference/GT.cols_merge.md#great_tables.GT.cols_merge), and others.

Source note  
Citation or attribution text displayed in the **footer**, below any **footnotes**. Added with [tab_source_note()](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note) and supports [md()](../reference/md.md#great_tables.md) and [html()](../reference/html.md#great_tables.html) formatting. Multiple source notes can be added and appear in the order they were defined. Targetable with [loc.source_notes()](../reference/loc.source_notes.md#great_tables.loc.source_notes).

Spanner label  
A label in the **column header** that spans across multiple contiguous **column labels**, providing a higher-level grouping. Created with [tab_spanner()](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) or automatically with [tab_spanner_delim()](../reference/GT.tab_spanner_delim.md#great_tables.GT.tab_spanner_delim) (which splits column names at a delimiter character). Spanners can be nested to any depth. Targetable with [loc.spanner_labels()](../reference/loc.spanner_labels.md#great_tables.loc.spanner_labels).

Stub  
A reserved leftmost column of the table that holds row labels, visually set apart from the **body** by a vertical dividing line. Created by passing `rowname_col=` to [GT()](../reference/GT.md#great_tables.GT). The stub provides a way to name rows and is required for features like **row groups** and row-based selection by name. Targetable with [loc.stub()](../reference/loc.stub.md#great_tables.loc.stub). The [stub](../reference/loc.stub.md#great_tables.loc.stub) sentinel object (importable from `great_tables`) can be used in [cols_width()](../reference/GT.cols_width.md#great_tables.GT.cols_width) to set the stub column's width.

Stubhead  
The cell at the top-left corner of the table, at the intersection of the **stub** and the **column header**. It exists only when a **stub** is present and can be labeled with [tab_stubhead()](../reference/GT.tab_stubhead.md#great_tables.GT.tab_stubhead). Targetable with [loc.stubhead()](../reference/loc.stubhead.md#great_tables.loc.stubhead).

Style  
A visual property applied to table elements via [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style). Styles are defined using objects from the `style` module: [style.text()](../reference/style.text.md#great_tables.style.text) for text properties (color, font, size, weight, alignment), [style.fill()](../reference/style.fill.md#great_tables.style.fill) for background color, [style.borders()](../reference/style.borders.md#great_tables.style.borders) for cell borders, and [style.css()](../reference/style.css.md#great_tables.style.css) for arbitrary CSS. Styles are paired with **location selectors** to target specific parts of the table.

Subtitle  
Secondary descriptive text displayed below the **title** in the **header**. Set via `tab_header(subtitle=...)`. Supports [md()](../reference/md.md#great_tables.md) and [html()](../reference/html.md#great_tables.html) formatting. Targetable with [loc.subtitle()](../reference/loc.subtitle.md#great_tables.loc.subtitle).

Summary rows  
Aggregation rows placed within each **row group** that summarize that group's data. Created with [summary_rows()](../reference/GT.summary_rows.md#great_tables.GT.summary_rows), which accepts aggregation functions (Polars expressions or callables) and an optional formatter. Can be placed at the top or bottom of each group with the `side=` parameter. Targetable with `loc.summary()`.

Table theme  
A coordinated set of visual options that control the overall appearance of the table. Great Tables provides 36 premade themes via [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize), combining 6 visual styles with 6 color palettes. Fine-grained control over every aspect of the table's appearance is available through [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options).

Title  
The main heading text displayed at the top of the **header**. Set via `tab_header(title=...)`. Supports [md()](../reference/md.md#great_tables.md) and [html()](../reference/html.md#great_tables.html) formatting. Targetable with [loc.title()](../reference/loc.title.md#great_tables.loc.title).
