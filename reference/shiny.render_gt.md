# shiny.render_gt()

Render a great_tables table.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/shiny.py#L175-L201)

``` python
shiny.render_gt() -> GtTransformer.OutputRendererDecorator
shiny.render_gt(_fn: GtTransformer.ValueFn) -> GtTransformer.OutputRenderer
```

An interactive table (a [GTI](../reference/GTI.md#great_tables.GTI) table, or a [GT](../reference/GT.md#great_tables.GT) table with [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive)) gives the app its state as inputs, for an output with id `id`:

- `input.<id>_view()`: the table's view, a dict with its filters as a query in text (`"query"`), its `"search"`, its `"sort"` (columns, with a `-` before those in descending order), its `"page"` and `"page_size"`, its `"hidden"` columns and the column its rows are grouped by (`"group_by"`);
- `input.<id>_rows()`: the data rows its search and filters keep (and linked tables' selections), in the order shown, on every page, numbered by position in the data (from 0);
- `input.<id>_selection()`: the data rows selected, in data order.

They're set once the table is shown, then after each change to them, whether the reader makes it or the server does, with [`update_gti()`](../reference/shiny.update_gti.md#great_tables.shiny.update_gti). A table rendered again starts again with the view it's given.

A [GTI](../reference/GTI.md#great_tables.GTI) table with more rows than the browser is quick with keeps them on the server instead (see [`i_scale()`](../reference/GTI.i_scale.md#great_tables.GTI.i_scale)), which sends the browser a page at a time: then `input.<id>_rows()` is found on the server, from the table's view (without linked tables' selections).
