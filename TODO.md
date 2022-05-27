Main TODOs:

- create generic interface to wrap source data
  - will be used internally to perform simple table-like operations (filtering, getting), and, also used for conversions of ingested data
- create implementation for formatting of cell contents (function factories, execution of functions at build time on table data)
- build data step implementation: transforming internal data structure to a more convenient data structure for the rendering step
  - reordering rows/columns, hiding columns, formatting cells, resolving spanners and row groups, resolving footnote ordering and attach footnote marks to cell text, styling cells (inline styling for the most part)
  - sometimes specific to each context type
- htmltools implementation
- print methods (e.g., Jupyter, other notebooks, **html**, **repr**, **str**)
- tests and feature parity with gt-r (process to ensure this target can be reached)
