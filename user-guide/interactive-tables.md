# Interactive Tables

**Great Tables** can render a fully interactive table (with sorting, searching, filtering, and pagination) by calling `opt_interactive()`. The result is a self-contained HTML widget powered by [DataTables](https://datatables.net/) that works in Jupyter notebooks, Quarto documents, and any HTML output.


# Enabling interactivity

A single call to `opt_interactive()` switches the table from static to interactive. All of the normal formatting and styling methods continue to work exactly as before.


``` python
from great_tables import GT
from great_tables.data import gtcars
import polars as pl

gtcars_pl = pl.from_pandas(gtcars).select(["mfr", "model", "year", "hp", "trq", "msrp"])

(
    GT(gtcars_pl)
    .tab_header(title="GT Cars", subtitle="The full dataset, interactively")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .opt_interactive()
)
```


GT Cars

The full dataset, interactively


<style>/* tmp/reactable/srcjs/react-table.css */
.Reactable {
  position: relative;
  display: flex;
  flex-direction: column;
}
.Reactable * {
  box-sizing: border-box;
}
.Reactable .rt-table {
  flex: auto 1;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  width: 100%;
  border-collapse: collapse;
  overflow: auto;
}
.Reactable .rt-thead {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-thead .rt-th,
.Reactable .rt-thead .rt-td {
  line-height: normal;
  position: relative;
}
.Reactable .rt-th.rt-th-resizable {
  overflow: visible;
}
.Reactable .rt-th.rt-th-resizable:last-child {
  overflow: hidden;
}
.Reactable .rt-tbody {
  display: flex;
  flex-direction: column;
  overflow: auto;
}
.rt-td-expandable {
  cursor: pointer;
}
.Reactable .rt-tr-group {
  flex: 1 0 auto;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.Reactable .rt-tr {
  flex: 1 0 auto;
  display: flex;
}
.Reactable .rt-th,
.Reactable .rt-td {
  flex: 1 0 0;
  overflow: hidden;
}
.Reactable .rt-resizer {
  display: inline-block;
  position: absolute;
  width: 36px;
  top: 0;
  bottom: 0;
  right: -18px;
  cursor: col-resize;
  z-index: 10;
}
.Reactable .rt-tfoot {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-resizing .rt-th,
.Reactable .rt-resizing .rt-td {
  transition: none !important;
  cursor: col-resize;
  user-select: none;
}

/* tmp/reactable/srcjs/reactable.css */
.Reactable {
  height: 100%;
  background-color: #fff;
}
.rt-inline {
  display: inline-flex;
}
.rt-th {
  font-weight: 600;
}
.rt-th,
.rt-td {
  display: flex;
  overflow-wrap: break-word;
  max-width: 100%;
  word-wrap: break-word;
}
.rt-th-inner,
.rt-td-inner {
  padding: 7px 8px;
  width: 100%;
  overflow: hidden;
}
.rt-compact .rt-th-inner,
.rt-compact .rt-td-inner {
  padding: 4px 6px;
}
.rt-text-content {
  overflow: hidden;
}
.rt-nowrap .rt-th-inner,
.rt-nowrap .rt-td-inner,
.rt-nowrap .rt-text-content {
  white-space: nowrap;
  text-overflow: ellipsis;
}
.rt-select {
  display: flex;
  align-items: center;
  justify-content: center;
}
input[type=checkbox].rt-select-input,
input[type=radio].rt-select-input {
  display: block;
  margin: 0;
}
.rt-align-left {
  text-align: left;
}
.rt-align-right {
  text-align: right;
}
.rt-align-center {
  text-align: center;
}
.rt-valign-center {
  align-items: center;
}
.rt-valign-bottom {
  align-items: flex-end;
}
.rt-tr,
.rt-tr-group,
.rt-tbody {
  background-color: inherit;
}
.rt-sticky {
  background-color: inherit;
  z-index: 1;
}
.rt-table {
  border-width: 1px;
  border-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-table,
.rt-bordered .rt-table {
  border-style: solid;
}
.Reactable:not(.rt-keyboard-active) .rt-table:focus {
  outline-width: 0;
  outline-style: solid;
}
.rt-th {
  border-bottom: 2px solid hsl(0, 0%, 90%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-outlined .rt-th,
.rt-bordered .rt-th {
  border-bottom-width: 1px;
}
.rt-td {
  border-top: 1px solid hsl(0, 0%, 95%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-group:first-child > .rt-tr:first-child .rt-td {
  border-top: none;
}
.rt-borderless .rt-td {
  border-top: none;
}
.rt-bordered .rt-td,
.rt-bordered .rt-th {
  border-left-style: solid;
}
.rt-bordered .rt-td:first-child,
.rt-bordered .rt-th:first-child {
  border-left: none;
}
.rt-th-group,
.rt-th-group-none {
  border-bottom-style: none;
}
.rt-th-group::after {
  content: "";
  position: absolute;
  margin: auto;
  left: 8px;
  right: 8px;
  bottom: 0;
  width: 100%;
  height: 1px;
  background-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-th-group::after,
.rt-bordered .rt-th-group::after {
  left: 0;
  right: 0;
}
.rt-bordered .rt-th-group-none {
  border-bottom-style: solid;
}
.rt-tr-striped {
  background-color: rgba(0, 0, 0, 0.03);
}
.rt-tr-striped-sticky {
  background-color: hsl(0, 0%, 97%);
}
.rt-tr-highlight:hover {
  background-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-highlight-sticky:hover {
  background-color: hsl(0, 0%, 95%);
}
.rt-tr-pad {
  user-select: none;
}
.Reactable .rt-thead,
.Reactable .rt-tfoot,
.Reactable .rt-tbody {
  flex-shrink: 0;
}
@supports (position: sticky) {
  .Reactable .rt-table {
    background: inherit;
  }
  .Reactable .rt-tbody {
    overflow: visible;
  }
  .Reactable .rt-thead {
    position: sticky;
    top: 0;
    background: inherit;
    z-index: 2;
  }
  .Reactable .rt-tfoot {
    position: sticky;
    bottom: 0;
    background: inherit;
    z-index: 2;
  }
}
@media screen and (-ms-high-contrast: active), screen and (-ms-high-contrast: none) {
  .Reactable .rt-tbody {
    overflow: auto;
    -ms-overflow-style: -ms-autohiding-scrollbar;
  }
}
.rt-td-filter {
  border-top: 0;
  border-bottom: 1px solid hsl(0, 0%, 95%);
}
.rt-borderless .rt-td-filter {
  border-bottom: 0;
}
.rt-filter {
  padding: 5px 7px;
  margin: 0;
  width: 100%;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  font-family: inherit;
  font-size: inherit;
  font-weight: normal;
  outline-width: 0;
  outline-style: solid;
}
.rt-filter:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
.rt-sort-header {
  display: flex;
}
.rt-align-center .rt-sort-header {
  justify-content: center;
}
.rt-align-right .rt-sort-header {
  justify-content: flex-end;
}
.rt-th {
  outline-width: 0;
  outline-style: solid;
}
.rt-th[aria-sort] {
  cursor: pointer;
}
.rt-th[aria-sort] .rt-sort-left::after {
  padding-right: 5px;
  line-height: 0;
}
.rt-th[aria-sort] .rt-sort-right::after {
  padding-left: 5px;
  line-height: 0;
}
.rt-th[aria-sort=ascending] .rt-sort-left::after,
.rt-th[aria-sort=ascending] .rt-sort-right::after {
  content: "\2191";
}
.rt-th[aria-sort=descending] .rt-sort-left::after,
.rt-th[aria-sort=descending] .rt-sort-right::after {
  content: "\2193";
}
.rt-th[aria-sort=none] .rt-sort::after {
  content: "\2195";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-right::after {
  content: "\2191";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-right::after {
  content: "\2193";
  opacity: 0.4;
}
.rt-expander-button {
  margin: 0 2px;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}
.rt-expander {
  display: inline-block;
  position: relative;
  padding: 0 8px;
  color: transparent;
  outline-width: 0;
  outline-style: solid;
}
.rt-expander::after {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-90deg);
  border-left: 5.04px solid transparent;
  border-right: 5.04px solid transparent;
  border-top: 7px solid rgba(0, 0, 0, 0.8);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  cursor: pointer;
}
.rt-expander.rt-expander-open::after {
  transform: translate(-50%, -50%) rotate(0);
}
.rt-pagination {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  padding: 6px 4px;
  border-top: 1px solid hsl(0, 0%, 95%);
}
.rt-outlined .rt-pagination,
.rt-bordered .rt-pagination {
  border-top: none;
}
.rt-pagination-info :not(:last-child) {
  margin-right: 16px;
}
.rt-page-info {
  display: inline-block;
  margin: 6px 8px;
  opacity: 0.9;
}
.rt-page-size {
  display: inline-block;
  margin: 0 8px;
}
.rt-page-size-select {
  margin: 0 2px;
}
.rt-page-size-select,
.rt-page-jump,
.rt-page-button {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  line-height: inherit;
}
.rt-page-size-select,
.rt-page-jump {
  background-color: #fff;
  padding: 3px;
  border-radius: 3px;
  border: 1px solid rgba(0, 0, 0, 0.05);
}
@supports (-moz-appearance: none) {
  .rt-page-size-select {
    -moz-appearance: none;
    padding-right: 12px;
    background-image: url('data:image/svg+xml;charset=US-ASCII,<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg"><path fill="%23333" d="M24 1.5l-12 21-12-21h24z"></path></svg>');
    background-repeat: no-repeat;
    background-position: right 6px center;
    background-size: 6px;
  }
}
.rt-page-button {
  padding: 6px 12px;
  background-color: transparent;
  border: none;
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  cursor: pointer;
}
.rt-page-button::-moz-focus-inner {
  padding: 0;
  border-style: none;
}
.rt-page-button:disabled {
  opacity: 0.6;
  cursor: default;
}
.rt-page-button:hover {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:active {
  background-color: rgba(0, 0, 0, 0.08);
}
.rt-keyboard-active .rt-page-button:focus {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:disabled:hover,
.rt-page-button:disabled:focus {
  background-color: transparent;
}
.rt-page-button-current {
  font-weight: 700;
}
.rt-page-ellipsis {
  margin: 0 4px;
  pointer-events: none;
}
.rt-page-numbers {
  display: inline-block;
  margin: 0 8px;
  white-space: nowrap;
}
.rt-page-jump {
  width: 70px;
  text-align: center;
}
.rt-tbody-no-data {
  position: relative;
}
.rt-tbody-no-data .rt-td {
  border-color: transparent;
}
.rt-no-data {
  display: block;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  line-height: 0;
  z-index: 1;
}
.rt-search {
  display: block;
  align-self: flex-end;
  margin: 0 0 8px 0;
  padding: 5px 7px;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  font-family: inherit;
  font-size: inherit;
}
.rt-search:active,
.rt-search:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
</style> <style>#gt-ihtml-mzqlifcmkp-container { display: block; width: 100%; font-size: 16px; margin: 10px 0; }
#gt-ihtml-mzqlifcmkp-container .gt-ihtml-header { display: block; width: 100%; text-align: center; padding: 10px 5px 8px 5px; border-top: 2px solid #A8A8A8; border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-mzqlifcmkp-container .rt-tbody { border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-mzqlifcmkp-container .rt-search { margin-top: 8px; }
#gt-ihtml-mzqlifcmkp-container .gt-ihtml-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.5em; font-weight: initial; margin: 0; }
#gt-ihtml-mzqlifcmkp-container .gt-ihtml-subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.05em; font-weight: initial; margin: 0; }
#gt-ihtml-mzqlifcmkp-container .gt-ihtml-source-note { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 90%; padding: 4px; margin: 0; }</style>


Click on any column header to sort. The table is paginated by default with 10 rows per page.


# Search and per-column filters

Pass `use_search=True` to add a global search box, and `use_filters=True` to add a per-column text filter row beneath the headers.


``` python
from great_tables import GT
from great_tables.data import gtcars
import polars as pl

(
    GT(gtcars_pl)
    .tab_header(title="GT Cars: Search and Filter")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .opt_interactive(use_search=True, use_filters=True)
)
```


GT Cars: Search and Filter


<style>/* tmp/reactable/srcjs/react-table.css */
.Reactable {
  position: relative;
  display: flex;
  flex-direction: column;
}
.Reactable * {
  box-sizing: border-box;
}
.Reactable .rt-table {
  flex: auto 1;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  width: 100%;
  border-collapse: collapse;
  overflow: auto;
}
.Reactable .rt-thead {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-thead .rt-th,
.Reactable .rt-thead .rt-td {
  line-height: normal;
  position: relative;
}
.Reactable .rt-th.rt-th-resizable {
  overflow: visible;
}
.Reactable .rt-th.rt-th-resizable:last-child {
  overflow: hidden;
}
.Reactable .rt-tbody {
  display: flex;
  flex-direction: column;
  overflow: auto;
}
.rt-td-expandable {
  cursor: pointer;
}
.Reactable .rt-tr-group {
  flex: 1 0 auto;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.Reactable .rt-tr {
  flex: 1 0 auto;
  display: flex;
}
.Reactable .rt-th,
.Reactable .rt-td {
  flex: 1 0 0;
  overflow: hidden;
}
.Reactable .rt-resizer {
  display: inline-block;
  position: absolute;
  width: 36px;
  top: 0;
  bottom: 0;
  right: -18px;
  cursor: col-resize;
  z-index: 10;
}
.Reactable .rt-tfoot {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-resizing .rt-th,
.Reactable .rt-resizing .rt-td {
  transition: none !important;
  cursor: col-resize;
  user-select: none;
}

/* tmp/reactable/srcjs/reactable.css */
.Reactable {
  height: 100%;
  background-color: #fff;
}
.rt-inline {
  display: inline-flex;
}
.rt-th {
  font-weight: 600;
}
.rt-th,
.rt-td {
  display: flex;
  overflow-wrap: break-word;
  max-width: 100%;
  word-wrap: break-word;
}
.rt-th-inner,
.rt-td-inner {
  padding: 7px 8px;
  width: 100%;
  overflow: hidden;
}
.rt-compact .rt-th-inner,
.rt-compact .rt-td-inner {
  padding: 4px 6px;
}
.rt-text-content {
  overflow: hidden;
}
.rt-nowrap .rt-th-inner,
.rt-nowrap .rt-td-inner,
.rt-nowrap .rt-text-content {
  white-space: nowrap;
  text-overflow: ellipsis;
}
.rt-select {
  display: flex;
  align-items: center;
  justify-content: center;
}
input[type=checkbox].rt-select-input,
input[type=radio].rt-select-input {
  display: block;
  margin: 0;
}
.rt-align-left {
  text-align: left;
}
.rt-align-right {
  text-align: right;
}
.rt-align-center {
  text-align: center;
}
.rt-valign-center {
  align-items: center;
}
.rt-valign-bottom {
  align-items: flex-end;
}
.rt-tr,
.rt-tr-group,
.rt-tbody {
  background-color: inherit;
}
.rt-sticky {
  background-color: inherit;
  z-index: 1;
}
.rt-table {
  border-width: 1px;
  border-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-table,
.rt-bordered .rt-table {
  border-style: solid;
}
.Reactable:not(.rt-keyboard-active) .rt-table:focus {
  outline-width: 0;
  outline-style: solid;
}
.rt-th {
  border-bottom: 2px solid hsl(0, 0%, 90%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-outlined .rt-th,
.rt-bordered .rt-th {
  border-bottom-width: 1px;
}
.rt-td {
  border-top: 1px solid hsl(0, 0%, 95%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-group:first-child > .rt-tr:first-child .rt-td {
  border-top: none;
}
.rt-borderless .rt-td {
  border-top: none;
}
.rt-bordered .rt-td,
.rt-bordered .rt-th {
  border-left-style: solid;
}
.rt-bordered .rt-td:first-child,
.rt-bordered .rt-th:first-child {
  border-left: none;
}
.rt-th-group,
.rt-th-group-none {
  border-bottom-style: none;
}
.rt-th-group::after {
  content: "";
  position: absolute;
  margin: auto;
  left: 8px;
  right: 8px;
  bottom: 0;
  width: 100%;
  height: 1px;
  background-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-th-group::after,
.rt-bordered .rt-th-group::after {
  left: 0;
  right: 0;
}
.rt-bordered .rt-th-group-none {
  border-bottom-style: solid;
}
.rt-tr-striped {
  background-color: rgba(0, 0, 0, 0.03);
}
.rt-tr-striped-sticky {
  background-color: hsl(0, 0%, 97%);
}
.rt-tr-highlight:hover {
  background-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-highlight-sticky:hover {
  background-color: hsl(0, 0%, 95%);
}
.rt-tr-pad {
  user-select: none;
}
.Reactable .rt-thead,
.Reactable .rt-tfoot,
.Reactable .rt-tbody {
  flex-shrink: 0;
}
@supports (position: sticky) {
  .Reactable .rt-table {
    background: inherit;
  }
  .Reactable .rt-tbody {
    overflow: visible;
  }
  .Reactable .rt-thead {
    position: sticky;
    top: 0;
    background: inherit;
    z-index: 2;
  }
  .Reactable .rt-tfoot {
    position: sticky;
    bottom: 0;
    background: inherit;
    z-index: 2;
  }
}
@media screen and (-ms-high-contrast: active), screen and (-ms-high-contrast: none) {
  .Reactable .rt-tbody {
    overflow: auto;
    -ms-overflow-style: -ms-autohiding-scrollbar;
  }
}
.rt-td-filter {
  border-top: 0;
  border-bottom: 1px solid hsl(0, 0%, 95%);
}
.rt-borderless .rt-td-filter {
  border-bottom: 0;
}
.rt-filter {
  padding: 5px 7px;
  margin: 0;
  width: 100%;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  font-family: inherit;
  font-size: inherit;
  font-weight: normal;
  outline-width: 0;
  outline-style: solid;
}
.rt-filter:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
.rt-sort-header {
  display: flex;
}
.rt-align-center .rt-sort-header {
  justify-content: center;
}
.rt-align-right .rt-sort-header {
  justify-content: flex-end;
}
.rt-th {
  outline-width: 0;
  outline-style: solid;
}
.rt-th[aria-sort] {
  cursor: pointer;
}
.rt-th[aria-sort] .rt-sort-left::after {
  padding-right: 5px;
  line-height: 0;
}
.rt-th[aria-sort] .rt-sort-right::after {
  padding-left: 5px;
  line-height: 0;
}
.rt-th[aria-sort=ascending] .rt-sort-left::after,
.rt-th[aria-sort=ascending] .rt-sort-right::after {
  content: "\2191";
}
.rt-th[aria-sort=descending] .rt-sort-left::after,
.rt-th[aria-sort=descending] .rt-sort-right::after {
  content: "\2193";
}
.rt-th[aria-sort=none] .rt-sort::after {
  content: "\2195";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-right::after {
  content: "\2191";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-right::after {
  content: "\2193";
  opacity: 0.4;
}
.rt-expander-button {
  margin: 0 2px;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}
.rt-expander {
  display: inline-block;
  position: relative;
  padding: 0 8px;
  color: transparent;
  outline-width: 0;
  outline-style: solid;
}
.rt-expander::after {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-90deg);
  border-left: 5.04px solid transparent;
  border-right: 5.04px solid transparent;
  border-top: 7px solid rgba(0, 0, 0, 0.8);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  cursor: pointer;
}
.rt-expander.rt-expander-open::after {
  transform: translate(-50%, -50%) rotate(0);
}
.rt-pagination {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  padding: 6px 4px;
  border-top: 1px solid hsl(0, 0%, 95%);
}
.rt-outlined .rt-pagination,
.rt-bordered .rt-pagination {
  border-top: none;
}
.rt-pagination-info :not(:last-child) {
  margin-right: 16px;
}
.rt-page-info {
  display: inline-block;
  margin: 6px 8px;
  opacity: 0.9;
}
.rt-page-size {
  display: inline-block;
  margin: 0 8px;
}
.rt-page-size-select {
  margin: 0 2px;
}
.rt-page-size-select,
.rt-page-jump,
.rt-page-button {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  line-height: inherit;
}
.rt-page-size-select,
.rt-page-jump {
  background-color: #fff;
  padding: 3px;
  border-radius: 3px;
  border: 1px solid rgba(0, 0, 0, 0.05);
}
@supports (-moz-appearance: none) {
  .rt-page-size-select {
    -moz-appearance: none;
    padding-right: 12px;
    background-image: url('data:image/svg+xml;charset=US-ASCII,<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg"><path fill="%23333" d="M24 1.5l-12 21-12-21h24z"></path></svg>');
    background-repeat: no-repeat;
    background-position: right 6px center;
    background-size: 6px;
  }
}
.rt-page-button {
  padding: 6px 12px;
  background-color: transparent;
  border: none;
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  cursor: pointer;
}
.rt-page-button::-moz-focus-inner {
  padding: 0;
  border-style: none;
}
.rt-page-button:disabled {
  opacity: 0.6;
  cursor: default;
}
.rt-page-button:hover {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:active {
  background-color: rgba(0, 0, 0, 0.08);
}
.rt-keyboard-active .rt-page-button:focus {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:disabled:hover,
.rt-page-button:disabled:focus {
  background-color: transparent;
}
.rt-page-button-current {
  font-weight: 700;
}
.rt-page-ellipsis {
  margin: 0 4px;
  pointer-events: none;
}
.rt-page-numbers {
  display: inline-block;
  margin: 0 8px;
  white-space: nowrap;
}
.rt-page-jump {
  width: 70px;
  text-align: center;
}
.rt-tbody-no-data {
  position: relative;
}
.rt-tbody-no-data .rt-td {
  border-color: transparent;
}
.rt-no-data {
  display: block;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  line-height: 0;
  z-index: 1;
}
.rt-search {
  display: block;
  align-self: flex-end;
  margin: 0 0 8px 0;
  padding: 5px 7px;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  font-family: inherit;
  font-size: inherit;
}
.rt-search:active,
.rt-search:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
</style> <style>#gt-ihtml-eqzjbyfdbo-container { display: block; width: 100%; font-size: 16px; margin: 10px 0; }
#gt-ihtml-eqzjbyfdbo-container .gt-ihtml-header { display: block; width: 100%; text-align: center; padding: 10px 5px 8px 5px; border-top: 2px solid #A8A8A8; border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-eqzjbyfdbo-container .rt-tbody { border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-eqzjbyfdbo-container .rt-search { margin-top: 8px; }
#gt-ihtml-eqzjbyfdbo-container .gt-ihtml-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.5em; font-weight: initial; margin: 0; }
#gt-ihtml-eqzjbyfdbo-container .gt-ihtml-subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.05em; font-weight: initial; margin: 0; }
#gt-ihtml-eqzjbyfdbo-container .gt-ihtml-source-note { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 90%; padding: 4px; margin: 0; }</style>


Try typing `"Audi"` in the `Make` filter or `"2017"` in the `Year` filter to narrow the results.


# Pagination options

Control the number of rows per page and let users choose from a list of sizes with `page_size_default=` and `page_size_values=`. The pagination style can also be changed with `pagination_type=` (`"numbers"`, `"simple"`, or `"full"`).


``` python
from great_tables import GT
from great_tables.data import gtcars
import polars as pl

(
    GT(gtcars_pl)
    .tab_header(title="GT Cars: Pagination options")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .opt_interactive(
        use_page_size_select=True,
        page_size_default=5,
        page_size_values=[5, 10, 25, 50],
        pagination_type="simple",
    )
)
```


GT Cars: Pagination options


<style>/* tmp/reactable/srcjs/react-table.css */
.Reactable {
  position: relative;
  display: flex;
  flex-direction: column;
}
.Reactable * {
  box-sizing: border-box;
}
.Reactable .rt-table {
  flex: auto 1;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  width: 100%;
  border-collapse: collapse;
  overflow: auto;
}
.Reactable .rt-thead {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-thead .rt-th,
.Reactable .rt-thead .rt-td {
  line-height: normal;
  position: relative;
}
.Reactable .rt-th.rt-th-resizable {
  overflow: visible;
}
.Reactable .rt-th.rt-th-resizable:last-child {
  overflow: hidden;
}
.Reactable .rt-tbody {
  display: flex;
  flex-direction: column;
  overflow: auto;
}
.rt-td-expandable {
  cursor: pointer;
}
.Reactable .rt-tr-group {
  flex: 1 0 auto;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.Reactable .rt-tr {
  flex: 1 0 auto;
  display: flex;
}
.Reactable .rt-th,
.Reactable .rt-td {
  flex: 1 0 0;
  overflow: hidden;
}
.Reactable .rt-resizer {
  display: inline-block;
  position: absolute;
  width: 36px;
  top: 0;
  bottom: 0;
  right: -18px;
  cursor: col-resize;
  z-index: 10;
}
.Reactable .rt-tfoot {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-resizing .rt-th,
.Reactable .rt-resizing .rt-td {
  transition: none !important;
  cursor: col-resize;
  user-select: none;
}

/* tmp/reactable/srcjs/reactable.css */
.Reactable {
  height: 100%;
  background-color: #fff;
}
.rt-inline {
  display: inline-flex;
}
.rt-th {
  font-weight: 600;
}
.rt-th,
.rt-td {
  display: flex;
  overflow-wrap: break-word;
  max-width: 100%;
  word-wrap: break-word;
}
.rt-th-inner,
.rt-td-inner {
  padding: 7px 8px;
  width: 100%;
  overflow: hidden;
}
.rt-compact .rt-th-inner,
.rt-compact .rt-td-inner {
  padding: 4px 6px;
}
.rt-text-content {
  overflow: hidden;
}
.rt-nowrap .rt-th-inner,
.rt-nowrap .rt-td-inner,
.rt-nowrap .rt-text-content {
  white-space: nowrap;
  text-overflow: ellipsis;
}
.rt-select {
  display: flex;
  align-items: center;
  justify-content: center;
}
input[type=checkbox].rt-select-input,
input[type=radio].rt-select-input {
  display: block;
  margin: 0;
}
.rt-align-left {
  text-align: left;
}
.rt-align-right {
  text-align: right;
}
.rt-align-center {
  text-align: center;
}
.rt-valign-center {
  align-items: center;
}
.rt-valign-bottom {
  align-items: flex-end;
}
.rt-tr,
.rt-tr-group,
.rt-tbody {
  background-color: inherit;
}
.rt-sticky {
  background-color: inherit;
  z-index: 1;
}
.rt-table {
  border-width: 1px;
  border-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-table,
.rt-bordered .rt-table {
  border-style: solid;
}
.Reactable:not(.rt-keyboard-active) .rt-table:focus {
  outline-width: 0;
  outline-style: solid;
}
.rt-th {
  border-bottom: 2px solid hsl(0, 0%, 90%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-outlined .rt-th,
.rt-bordered .rt-th {
  border-bottom-width: 1px;
}
.rt-td {
  border-top: 1px solid hsl(0, 0%, 95%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-group:first-child > .rt-tr:first-child .rt-td {
  border-top: none;
}
.rt-borderless .rt-td {
  border-top: none;
}
.rt-bordered .rt-td,
.rt-bordered .rt-th {
  border-left-style: solid;
}
.rt-bordered .rt-td:first-child,
.rt-bordered .rt-th:first-child {
  border-left: none;
}
.rt-th-group,
.rt-th-group-none {
  border-bottom-style: none;
}
.rt-th-group::after {
  content: "";
  position: absolute;
  margin: auto;
  left: 8px;
  right: 8px;
  bottom: 0;
  width: 100%;
  height: 1px;
  background-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-th-group::after,
.rt-bordered .rt-th-group::after {
  left: 0;
  right: 0;
}
.rt-bordered .rt-th-group-none {
  border-bottom-style: solid;
}
.rt-tr-striped {
  background-color: rgba(0, 0, 0, 0.03);
}
.rt-tr-striped-sticky {
  background-color: hsl(0, 0%, 97%);
}
.rt-tr-highlight:hover {
  background-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-highlight-sticky:hover {
  background-color: hsl(0, 0%, 95%);
}
.rt-tr-pad {
  user-select: none;
}
.Reactable .rt-thead,
.Reactable .rt-tfoot,
.Reactable .rt-tbody {
  flex-shrink: 0;
}
@supports (position: sticky) {
  .Reactable .rt-table {
    background: inherit;
  }
  .Reactable .rt-tbody {
    overflow: visible;
  }
  .Reactable .rt-thead {
    position: sticky;
    top: 0;
    background: inherit;
    z-index: 2;
  }
  .Reactable .rt-tfoot {
    position: sticky;
    bottom: 0;
    background: inherit;
    z-index: 2;
  }
}
@media screen and (-ms-high-contrast: active), screen and (-ms-high-contrast: none) {
  .Reactable .rt-tbody {
    overflow: auto;
    -ms-overflow-style: -ms-autohiding-scrollbar;
  }
}
.rt-td-filter {
  border-top: 0;
  border-bottom: 1px solid hsl(0, 0%, 95%);
}
.rt-borderless .rt-td-filter {
  border-bottom: 0;
}
.rt-filter {
  padding: 5px 7px;
  margin: 0;
  width: 100%;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  font-family: inherit;
  font-size: inherit;
  font-weight: normal;
  outline-width: 0;
  outline-style: solid;
}
.rt-filter:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
.rt-sort-header {
  display: flex;
}
.rt-align-center .rt-sort-header {
  justify-content: center;
}
.rt-align-right .rt-sort-header {
  justify-content: flex-end;
}
.rt-th {
  outline-width: 0;
  outline-style: solid;
}
.rt-th[aria-sort] {
  cursor: pointer;
}
.rt-th[aria-sort] .rt-sort-left::after {
  padding-right: 5px;
  line-height: 0;
}
.rt-th[aria-sort] .rt-sort-right::after {
  padding-left: 5px;
  line-height: 0;
}
.rt-th[aria-sort=ascending] .rt-sort-left::after,
.rt-th[aria-sort=ascending] .rt-sort-right::after {
  content: "\2191";
}
.rt-th[aria-sort=descending] .rt-sort-left::after,
.rt-th[aria-sort=descending] .rt-sort-right::after {
  content: "\2193";
}
.rt-th[aria-sort=none] .rt-sort::after {
  content: "\2195";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-right::after {
  content: "\2191";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-right::after {
  content: "\2193";
  opacity: 0.4;
}
.rt-expander-button {
  margin: 0 2px;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}
.rt-expander {
  display: inline-block;
  position: relative;
  padding: 0 8px;
  color: transparent;
  outline-width: 0;
  outline-style: solid;
}
.rt-expander::after {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-90deg);
  border-left: 5.04px solid transparent;
  border-right: 5.04px solid transparent;
  border-top: 7px solid rgba(0, 0, 0, 0.8);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  cursor: pointer;
}
.rt-expander.rt-expander-open::after {
  transform: translate(-50%, -50%) rotate(0);
}
.rt-pagination {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  padding: 6px 4px;
  border-top: 1px solid hsl(0, 0%, 95%);
}
.rt-outlined .rt-pagination,
.rt-bordered .rt-pagination {
  border-top: none;
}
.rt-pagination-info :not(:last-child) {
  margin-right: 16px;
}
.rt-page-info {
  display: inline-block;
  margin: 6px 8px;
  opacity: 0.9;
}
.rt-page-size {
  display: inline-block;
  margin: 0 8px;
}
.rt-page-size-select {
  margin: 0 2px;
}
.rt-page-size-select,
.rt-page-jump,
.rt-page-button {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  line-height: inherit;
}
.rt-page-size-select,
.rt-page-jump {
  background-color: #fff;
  padding: 3px;
  border-radius: 3px;
  border: 1px solid rgba(0, 0, 0, 0.05);
}
@supports (-moz-appearance: none) {
  .rt-page-size-select {
    -moz-appearance: none;
    padding-right: 12px;
    background-image: url('data:image/svg+xml;charset=US-ASCII,<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg"><path fill="%23333" d="M24 1.5l-12 21-12-21h24z"></path></svg>');
    background-repeat: no-repeat;
    background-position: right 6px center;
    background-size: 6px;
  }
}
.rt-page-button {
  padding: 6px 12px;
  background-color: transparent;
  border: none;
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  cursor: pointer;
}
.rt-page-button::-moz-focus-inner {
  padding: 0;
  border-style: none;
}
.rt-page-button:disabled {
  opacity: 0.6;
  cursor: default;
}
.rt-page-button:hover {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:active {
  background-color: rgba(0, 0, 0, 0.08);
}
.rt-keyboard-active .rt-page-button:focus {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:disabled:hover,
.rt-page-button:disabled:focus {
  background-color: transparent;
}
.rt-page-button-current {
  font-weight: 700;
}
.rt-page-ellipsis {
  margin: 0 4px;
  pointer-events: none;
}
.rt-page-numbers {
  display: inline-block;
  margin: 0 8px;
  white-space: nowrap;
}
.rt-page-jump {
  width: 70px;
  text-align: center;
}
.rt-tbody-no-data {
  position: relative;
}
.rt-tbody-no-data .rt-td {
  border-color: transparent;
}
.rt-no-data {
  display: block;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  line-height: 0;
  z-index: 1;
}
.rt-search {
  display: block;
  align-self: flex-end;
  margin: 0 0 8px 0;
  padding: 5px 7px;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  font-family: inherit;
  font-size: inherit;
}
.rt-search:active,
.rt-search:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
</style> <style>#gt-ihtml-vevjzudulj-container { display: block; width: 100%; font-size: 16px; margin: 10px 0; }
#gt-ihtml-vevjzudulj-container .gt-ihtml-header { display: block; width: 100%; text-align: center; padding: 10px 5px 8px 5px; border-top: 2px solid #A8A8A8; border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-vevjzudulj-container .rt-tbody { border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-vevjzudulj-container .rt-search { margin-top: 8px; }
#gt-ihtml-vevjzudulj-container .gt-ihtml-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.5em; font-weight: initial; margin: 0; }
#gt-ihtml-vevjzudulj-container .gt-ihtml-subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.05em; font-weight: initial; margin: 0; }
#gt-ihtml-vevjzudulj-container .gt-ihtml-source-note { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 90%; padding: 4px; margin: 0; }</style>


Set `use_pagination=False` to display the full table without paging. This is useful for smaller datasets.


# Styling with [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style)

The [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) methods works in interactive mode for [loc.body()](../reference/loc.body.md#great_tables.loc.body) and [loc.column_labels()](../reference/loc.column_labels.md#great_tables.loc.column_labels). Styles are applied row-by-row as DataTables renders each page, so they follow the data when you sort or filter.


``` python
from great_tables import style, loc

(
    GT(gtcars_pl)
    .tab_header(title="GT Cars: Targeted styles")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .tab_style(
        style=style.fill(color="#fff3cd"),
        locations=loc.body(columns="hp", rows=pl.col("hp") > 500),
    )
    .tab_style(
        style=[style.text(color="#c0392b", weight="bold")],
        locations=loc.body(columns="msrp", rows=pl.col("msrp") > 200_000),
    )
    .tab_style(
        style=[style.fill(color="#ddeeff"), style.text(weight="bold")],
        locations=loc.column_labels(columns=["hp", "trq"]),
    )
    .opt_interactive(use_search=True, use_filters=True, page_size_default=10)
)
```


GT Cars: Targeted styles


<style>/* tmp/reactable/srcjs/react-table.css */
.Reactable {
  position: relative;
  display: flex;
  flex-direction: column;
}
.Reactable * {
  box-sizing: border-box;
}
.Reactable .rt-table {
  flex: auto 1;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  width: 100%;
  border-collapse: collapse;
  overflow: auto;
}
.Reactable .rt-thead {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-thead .rt-th,
.Reactable .rt-thead .rt-td {
  line-height: normal;
  position: relative;
}
.Reactable .rt-th.rt-th-resizable {
  overflow: visible;
}
.Reactable .rt-th.rt-th-resizable:last-child {
  overflow: hidden;
}
.Reactable .rt-tbody {
  display: flex;
  flex-direction: column;
  overflow: auto;
}
.rt-td-expandable {
  cursor: pointer;
}
.Reactable .rt-tr-group {
  flex: 1 0 auto;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.Reactable .rt-tr {
  flex: 1 0 auto;
  display: flex;
}
.Reactable .rt-th,
.Reactable .rt-td {
  flex: 1 0 0;
  overflow: hidden;
}
.Reactable .rt-resizer {
  display: inline-block;
  position: absolute;
  width: 36px;
  top: 0;
  bottom: 0;
  right: -18px;
  cursor: col-resize;
  z-index: 10;
}
.Reactable .rt-tfoot {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-resizing .rt-th,
.Reactable .rt-resizing .rt-td {
  transition: none !important;
  cursor: col-resize;
  user-select: none;
}

/* tmp/reactable/srcjs/reactable.css */
.Reactable {
  height: 100%;
  background-color: #fff;
}
.rt-inline {
  display: inline-flex;
}
.rt-th {
  font-weight: 600;
}
.rt-th,
.rt-td {
  display: flex;
  overflow-wrap: break-word;
  max-width: 100%;
  word-wrap: break-word;
}
.rt-th-inner,
.rt-td-inner {
  padding: 7px 8px;
  width: 100%;
  overflow: hidden;
}
.rt-compact .rt-th-inner,
.rt-compact .rt-td-inner {
  padding: 4px 6px;
}
.rt-text-content {
  overflow: hidden;
}
.rt-nowrap .rt-th-inner,
.rt-nowrap .rt-td-inner,
.rt-nowrap .rt-text-content {
  white-space: nowrap;
  text-overflow: ellipsis;
}
.rt-select {
  display: flex;
  align-items: center;
  justify-content: center;
}
input[type=checkbox].rt-select-input,
input[type=radio].rt-select-input {
  display: block;
  margin: 0;
}
.rt-align-left {
  text-align: left;
}
.rt-align-right {
  text-align: right;
}
.rt-align-center {
  text-align: center;
}
.rt-valign-center {
  align-items: center;
}
.rt-valign-bottom {
  align-items: flex-end;
}
.rt-tr,
.rt-tr-group,
.rt-tbody {
  background-color: inherit;
}
.rt-sticky {
  background-color: inherit;
  z-index: 1;
}
.rt-table {
  border-width: 1px;
  border-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-table,
.rt-bordered .rt-table {
  border-style: solid;
}
.Reactable:not(.rt-keyboard-active) .rt-table:focus {
  outline-width: 0;
  outline-style: solid;
}
.rt-th {
  border-bottom: 2px solid hsl(0, 0%, 90%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-outlined .rt-th,
.rt-bordered .rt-th {
  border-bottom-width: 1px;
}
.rt-td {
  border-top: 1px solid hsl(0, 0%, 95%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-group:first-child > .rt-tr:first-child .rt-td {
  border-top: none;
}
.rt-borderless .rt-td {
  border-top: none;
}
.rt-bordered .rt-td,
.rt-bordered .rt-th {
  border-left-style: solid;
}
.rt-bordered .rt-td:first-child,
.rt-bordered .rt-th:first-child {
  border-left: none;
}
.rt-th-group,
.rt-th-group-none {
  border-bottom-style: none;
}
.rt-th-group::after {
  content: "";
  position: absolute;
  margin: auto;
  left: 8px;
  right: 8px;
  bottom: 0;
  width: 100%;
  height: 1px;
  background-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-th-group::after,
.rt-bordered .rt-th-group::after {
  left: 0;
  right: 0;
}
.rt-bordered .rt-th-group-none {
  border-bottom-style: solid;
}
.rt-tr-striped {
  background-color: rgba(0, 0, 0, 0.03);
}
.rt-tr-striped-sticky {
  background-color: hsl(0, 0%, 97%);
}
.rt-tr-highlight:hover {
  background-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-highlight-sticky:hover {
  background-color: hsl(0, 0%, 95%);
}
.rt-tr-pad {
  user-select: none;
}
.Reactable .rt-thead,
.Reactable .rt-tfoot,
.Reactable .rt-tbody {
  flex-shrink: 0;
}
@supports (position: sticky) {
  .Reactable .rt-table {
    background: inherit;
  }
  .Reactable .rt-tbody {
    overflow: visible;
  }
  .Reactable .rt-thead {
    position: sticky;
    top: 0;
    background: inherit;
    z-index: 2;
  }
  .Reactable .rt-tfoot {
    position: sticky;
    bottom: 0;
    background: inherit;
    z-index: 2;
  }
}
@media screen and (-ms-high-contrast: active), screen and (-ms-high-contrast: none) {
  .Reactable .rt-tbody {
    overflow: auto;
    -ms-overflow-style: -ms-autohiding-scrollbar;
  }
}
.rt-td-filter {
  border-top: 0;
  border-bottom: 1px solid hsl(0, 0%, 95%);
}
.rt-borderless .rt-td-filter {
  border-bottom: 0;
}
.rt-filter {
  padding: 5px 7px;
  margin: 0;
  width: 100%;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  font-family: inherit;
  font-size: inherit;
  font-weight: normal;
  outline-width: 0;
  outline-style: solid;
}
.rt-filter:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
.rt-sort-header {
  display: flex;
}
.rt-align-center .rt-sort-header {
  justify-content: center;
}
.rt-align-right .rt-sort-header {
  justify-content: flex-end;
}
.rt-th {
  outline-width: 0;
  outline-style: solid;
}
.rt-th[aria-sort] {
  cursor: pointer;
}
.rt-th[aria-sort] .rt-sort-left::after {
  padding-right: 5px;
  line-height: 0;
}
.rt-th[aria-sort] .rt-sort-right::after {
  padding-left: 5px;
  line-height: 0;
}
.rt-th[aria-sort=ascending] .rt-sort-left::after,
.rt-th[aria-sort=ascending] .rt-sort-right::after {
  content: "\2191";
}
.rt-th[aria-sort=descending] .rt-sort-left::after,
.rt-th[aria-sort=descending] .rt-sort-right::after {
  content: "\2193";
}
.rt-th[aria-sort=none] .rt-sort::after {
  content: "\2195";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-right::after {
  content: "\2191";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-right::after {
  content: "\2193";
  opacity: 0.4;
}
.rt-expander-button {
  margin: 0 2px;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}
.rt-expander {
  display: inline-block;
  position: relative;
  padding: 0 8px;
  color: transparent;
  outline-width: 0;
  outline-style: solid;
}
.rt-expander::after {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-90deg);
  border-left: 5.04px solid transparent;
  border-right: 5.04px solid transparent;
  border-top: 7px solid rgba(0, 0, 0, 0.8);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  cursor: pointer;
}
.rt-expander.rt-expander-open::after {
  transform: translate(-50%, -50%) rotate(0);
}
.rt-pagination {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  padding: 6px 4px;
  border-top: 1px solid hsl(0, 0%, 95%);
}
.rt-outlined .rt-pagination,
.rt-bordered .rt-pagination {
  border-top: none;
}
.rt-pagination-info :not(:last-child) {
  margin-right: 16px;
}
.rt-page-info {
  display: inline-block;
  margin: 6px 8px;
  opacity: 0.9;
}
.rt-page-size {
  display: inline-block;
  margin: 0 8px;
}
.rt-page-size-select {
  margin: 0 2px;
}
.rt-page-size-select,
.rt-page-jump,
.rt-page-button {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  line-height: inherit;
}
.rt-page-size-select,
.rt-page-jump {
  background-color: #fff;
  padding: 3px;
  border-radius: 3px;
  border: 1px solid rgba(0, 0, 0, 0.05);
}
@supports (-moz-appearance: none) {
  .rt-page-size-select {
    -moz-appearance: none;
    padding-right: 12px;
    background-image: url('data:image/svg+xml;charset=US-ASCII,<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg"><path fill="%23333" d="M24 1.5l-12 21-12-21h24z"></path></svg>');
    background-repeat: no-repeat;
    background-position: right 6px center;
    background-size: 6px;
  }
}
.rt-page-button {
  padding: 6px 12px;
  background-color: transparent;
  border: none;
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  cursor: pointer;
}
.rt-page-button::-moz-focus-inner {
  padding: 0;
  border-style: none;
}
.rt-page-button:disabled {
  opacity: 0.6;
  cursor: default;
}
.rt-page-button:hover {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:active {
  background-color: rgba(0, 0, 0, 0.08);
}
.rt-keyboard-active .rt-page-button:focus {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:disabled:hover,
.rt-page-button:disabled:focus {
  background-color: transparent;
}
.rt-page-button-current {
  font-weight: 700;
}
.rt-page-ellipsis {
  margin: 0 4px;
  pointer-events: none;
}
.rt-page-numbers {
  display: inline-block;
  margin: 0 8px;
  white-space: nowrap;
}
.rt-page-jump {
  width: 70px;
  text-align: center;
}
.rt-tbody-no-data {
  position: relative;
}
.rt-tbody-no-data .rt-td {
  border-color: transparent;
}
.rt-no-data {
  display: block;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  line-height: 0;
  z-index: 1;
}
.rt-search {
  display: block;
  align-self: flex-end;
  margin: 0 0 8px 0;
  padding: 5px 7px;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  font-family: inherit;
  font-size: inherit;
}
.rt-search:active,
.rt-search:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
</style> <style>#gt-ihtml-vuituayddb-container { display: block; width: 100%; font-size: 16px; margin: 10px 0; }
#gt-ihtml-vuituayddb-container .gt-ihtml-header { display: block; width: 100%; text-align: center; padding: 10px 5px 8px 5px; border-top: 2px solid #A8A8A8; border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-vuituayddb-container .rt-tbody { border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-vuituayddb-container .rt-search { margin-top: 8px; }
#gt-ihtml-vuituayddb-container .gt-ihtml-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.5em; font-weight: initial; margin: 0; }
#gt-ihtml-vuituayddb-container .gt-ihtml-subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.05em; font-weight: initial; margin: 0; }
#gt-ihtml-vuituayddb-container .gt-ihtml-source-note { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 90%; padding: 4px; margin: 0; }</style>


From the output you might notice:

- rows where HP exceeds 500 are highlighted in amber
- MSRP values over \$200,000 appear in bold red
- the `HP` and `Torque` column headers have a blue-tinted background

Sort by `HP` or `MSRP` to confirm that the styling moves with the data.


# Colorizing with [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color)

The use of [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) is fully supported in interactive tables. It applies a continuous color scale to each cell based on the underlying value. Because [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) is implemented via [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) internally, it inherits the same interactive behavior automatically.


``` python
(
    GT(gtcars_pl)
    .tab_header(title="GT Cars: data_color()")
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .data_color(columns="hp",  palette=["#fff7ec", "#ef6c00"])
    .data_color(columns="msrp", palette="Blues")
    .opt_interactive(use_search=True, use_filters=True, page_size_default=10)
)
```


GT Cars: data_color()


<style>/* tmp/reactable/srcjs/react-table.css */
.Reactable {
  position: relative;
  display: flex;
  flex-direction: column;
}
.Reactable * {
  box-sizing: border-box;
}
.Reactable .rt-table {
  flex: auto 1;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  width: 100%;
  border-collapse: collapse;
  overflow: auto;
}
.Reactable .rt-thead {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-thead .rt-th,
.Reactable .rt-thead .rt-td {
  line-height: normal;
  position: relative;
}
.Reactable .rt-th.rt-th-resizable {
  overflow: visible;
}
.Reactable .rt-th.rt-th-resizable:last-child {
  overflow: hidden;
}
.Reactable .rt-tbody {
  display: flex;
  flex-direction: column;
  overflow: auto;
}
.rt-td-expandable {
  cursor: pointer;
}
.Reactable .rt-tr-group {
  flex: 1 0 auto;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.Reactable .rt-tr {
  flex: 1 0 auto;
  display: flex;
}
.Reactable .rt-th,
.Reactable .rt-td {
  flex: 1 0 0;
  overflow: hidden;
}
.Reactable .rt-resizer {
  display: inline-block;
  position: absolute;
  width: 36px;
  top: 0;
  bottom: 0;
  right: -18px;
  cursor: col-resize;
  z-index: 10;
}
.Reactable .rt-tfoot {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-resizing .rt-th,
.Reactable .rt-resizing .rt-td {
  transition: none !important;
  cursor: col-resize;
  user-select: none;
}

/* tmp/reactable/srcjs/reactable.css */
.Reactable {
  height: 100%;
  background-color: #fff;
}
.rt-inline {
  display: inline-flex;
}
.rt-th {
  font-weight: 600;
}
.rt-th,
.rt-td {
  display: flex;
  overflow-wrap: break-word;
  max-width: 100%;
  word-wrap: break-word;
}
.rt-th-inner,
.rt-td-inner {
  padding: 7px 8px;
  width: 100%;
  overflow: hidden;
}
.rt-compact .rt-th-inner,
.rt-compact .rt-td-inner {
  padding: 4px 6px;
}
.rt-text-content {
  overflow: hidden;
}
.rt-nowrap .rt-th-inner,
.rt-nowrap .rt-td-inner,
.rt-nowrap .rt-text-content {
  white-space: nowrap;
  text-overflow: ellipsis;
}
.rt-select {
  display: flex;
  align-items: center;
  justify-content: center;
}
input[type=checkbox].rt-select-input,
input[type=radio].rt-select-input {
  display: block;
  margin: 0;
}
.rt-align-left {
  text-align: left;
}
.rt-align-right {
  text-align: right;
}
.rt-align-center {
  text-align: center;
}
.rt-valign-center {
  align-items: center;
}
.rt-valign-bottom {
  align-items: flex-end;
}
.rt-tr,
.rt-tr-group,
.rt-tbody {
  background-color: inherit;
}
.rt-sticky {
  background-color: inherit;
  z-index: 1;
}
.rt-table {
  border-width: 1px;
  border-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-table,
.rt-bordered .rt-table {
  border-style: solid;
}
.Reactable:not(.rt-keyboard-active) .rt-table:focus {
  outline-width: 0;
  outline-style: solid;
}
.rt-th {
  border-bottom: 2px solid hsl(0, 0%, 90%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-outlined .rt-th,
.rt-bordered .rt-th {
  border-bottom-width: 1px;
}
.rt-td {
  border-top: 1px solid hsl(0, 0%, 95%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-group:first-child > .rt-tr:first-child .rt-td {
  border-top: none;
}
.rt-borderless .rt-td {
  border-top: none;
}
.rt-bordered .rt-td,
.rt-bordered .rt-th {
  border-left-style: solid;
}
.rt-bordered .rt-td:first-child,
.rt-bordered .rt-th:first-child {
  border-left: none;
}
.rt-th-group,
.rt-th-group-none {
  border-bottom-style: none;
}
.rt-th-group::after {
  content: "";
  position: absolute;
  margin: auto;
  left: 8px;
  right: 8px;
  bottom: 0;
  width: 100%;
  height: 1px;
  background-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-th-group::after,
.rt-bordered .rt-th-group::after {
  left: 0;
  right: 0;
}
.rt-bordered .rt-th-group-none {
  border-bottom-style: solid;
}
.rt-tr-striped {
  background-color: rgba(0, 0, 0, 0.03);
}
.rt-tr-striped-sticky {
  background-color: hsl(0, 0%, 97%);
}
.rt-tr-highlight:hover {
  background-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-highlight-sticky:hover {
  background-color: hsl(0, 0%, 95%);
}
.rt-tr-pad {
  user-select: none;
}
.Reactable .rt-thead,
.Reactable .rt-tfoot,
.Reactable .rt-tbody {
  flex-shrink: 0;
}
@supports (position: sticky) {
  .Reactable .rt-table {
    background: inherit;
  }
  .Reactable .rt-tbody {
    overflow: visible;
  }
  .Reactable .rt-thead {
    position: sticky;
    top: 0;
    background: inherit;
    z-index: 2;
  }
  .Reactable .rt-tfoot {
    position: sticky;
    bottom: 0;
    background: inherit;
    z-index: 2;
  }
}
@media screen and (-ms-high-contrast: active), screen and (-ms-high-contrast: none) {
  .Reactable .rt-tbody {
    overflow: auto;
    -ms-overflow-style: -ms-autohiding-scrollbar;
  }
}
.rt-td-filter {
  border-top: 0;
  border-bottom: 1px solid hsl(0, 0%, 95%);
}
.rt-borderless .rt-td-filter {
  border-bottom: 0;
}
.rt-filter {
  padding: 5px 7px;
  margin: 0;
  width: 100%;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  font-family: inherit;
  font-size: inherit;
  font-weight: normal;
  outline-width: 0;
  outline-style: solid;
}
.rt-filter:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
.rt-sort-header {
  display: flex;
}
.rt-align-center .rt-sort-header {
  justify-content: center;
}
.rt-align-right .rt-sort-header {
  justify-content: flex-end;
}
.rt-th {
  outline-width: 0;
  outline-style: solid;
}
.rt-th[aria-sort] {
  cursor: pointer;
}
.rt-th[aria-sort] .rt-sort-left::after {
  padding-right: 5px;
  line-height: 0;
}
.rt-th[aria-sort] .rt-sort-right::after {
  padding-left: 5px;
  line-height: 0;
}
.rt-th[aria-sort=ascending] .rt-sort-left::after,
.rt-th[aria-sort=ascending] .rt-sort-right::after {
  content: "\2191";
}
.rt-th[aria-sort=descending] .rt-sort-left::after,
.rt-th[aria-sort=descending] .rt-sort-right::after {
  content: "\2193";
}
.rt-th[aria-sort=none] .rt-sort::after {
  content: "\2195";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-right::after {
  content: "\2191";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-right::after {
  content: "\2193";
  opacity: 0.4;
}
.rt-expander-button {
  margin: 0 2px;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}
.rt-expander {
  display: inline-block;
  position: relative;
  padding: 0 8px;
  color: transparent;
  outline-width: 0;
  outline-style: solid;
}
.rt-expander::after {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-90deg);
  border-left: 5.04px solid transparent;
  border-right: 5.04px solid transparent;
  border-top: 7px solid rgba(0, 0, 0, 0.8);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  cursor: pointer;
}
.rt-expander.rt-expander-open::after {
  transform: translate(-50%, -50%) rotate(0);
}
.rt-pagination {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  padding: 6px 4px;
  border-top: 1px solid hsl(0, 0%, 95%);
}
.rt-outlined .rt-pagination,
.rt-bordered .rt-pagination {
  border-top: none;
}
.rt-pagination-info :not(:last-child) {
  margin-right: 16px;
}
.rt-page-info {
  display: inline-block;
  margin: 6px 8px;
  opacity: 0.9;
}
.rt-page-size {
  display: inline-block;
  margin: 0 8px;
}
.rt-page-size-select {
  margin: 0 2px;
}
.rt-page-size-select,
.rt-page-jump,
.rt-page-button {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  line-height: inherit;
}
.rt-page-size-select,
.rt-page-jump {
  background-color: #fff;
  padding: 3px;
  border-radius: 3px;
  border: 1px solid rgba(0, 0, 0, 0.05);
}
@supports (-moz-appearance: none) {
  .rt-page-size-select {
    -moz-appearance: none;
    padding-right: 12px;
    background-image: url('data:image/svg+xml;charset=US-ASCII,<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg"><path fill="%23333" d="M24 1.5l-12 21-12-21h24z"></path></svg>');
    background-repeat: no-repeat;
    background-position: right 6px center;
    background-size: 6px;
  }
}
.rt-page-button {
  padding: 6px 12px;
  background-color: transparent;
  border: none;
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  cursor: pointer;
}
.rt-page-button::-moz-focus-inner {
  padding: 0;
  border-style: none;
}
.rt-page-button:disabled {
  opacity: 0.6;
  cursor: default;
}
.rt-page-button:hover {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:active {
  background-color: rgba(0, 0, 0, 0.08);
}
.rt-keyboard-active .rt-page-button:focus {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:disabled:hover,
.rt-page-button:disabled:focus {
  background-color: transparent;
}
.rt-page-button-current {
  font-weight: 700;
}
.rt-page-ellipsis {
  margin: 0 4px;
  pointer-events: none;
}
.rt-page-numbers {
  display: inline-block;
  margin: 0 8px;
  white-space: nowrap;
}
.rt-page-jump {
  width: 70px;
  text-align: center;
}
.rt-tbody-no-data {
  position: relative;
}
.rt-tbody-no-data .rt-td {
  border-color: transparent;
}
.rt-no-data {
  display: block;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  line-height: 0;
  z-index: 1;
}
.rt-search {
  display: block;
  align-self: flex-end;
  margin: 0 0 8px 0;
  padding: 5px 7px;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  font-family: inherit;
  font-size: inherit;
}
.rt-search:active,
.rt-search:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
</style> <style>#gt-ihtml-ukdoyktuee-container { display: block; width: 100%; font-size: 16px; margin: 10px 0; }
#gt-ihtml-ukdoyktuee-container .gt-ihtml-header { display: block; width: 100%; text-align: center; padding: 10px 5px 8px 5px; border-top: 2px solid #A8A8A8; border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-ukdoyktuee-container .rt-tbody { border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-ukdoyktuee-container .rt-search { margin-top: 8px; }
#gt-ihtml-ukdoyktuee-container .gt-ihtml-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.5em; font-weight: initial; margin: 0; }
#gt-ihtml-ukdoyktuee-container .gt-ihtml-subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.05em; font-weight: initial; margin: 0; }
#gt-ihtml-ukdoyktuee-container .gt-ihtml-source-note { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 90%; padding: 4px; margin: 0; }</style>


Each column uses its own independent scale: orange for `HP` and blue for `MSRP`. Try filtering by `Make` to see how the scales update in context.


## Multiple columns, shared scale

Pass `domain=` to lock the color range across columns so they share a common scale.


``` python
(
    GT(gtcars_pl)
    .tab_header(
        title="GT Cars: HP and Torque on a shared scale",
        subtitle="Higher values are darker and both columns use the same domain",
    )
    .cols_label(mfr="Make", model="Model", year="Year", hp="HP", trq="Torque", msrp="MSRP")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .data_color(
        columns=["hp", "trq"],
        palette=["#edf8fb", "#006d2c"],
        domain=[200, 700],
    )
    .opt_interactive(use_search=True, page_size_default=10)
)
```


GT Cars: HP and Torque on a shared scale

Higher values are darker and both columns use the same domain


<style>/* tmp/reactable/srcjs/react-table.css */
.Reactable {
  position: relative;
  display: flex;
  flex-direction: column;
}
.Reactable * {
  box-sizing: border-box;
}
.Reactable .rt-table {
  flex: auto 1;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  width: 100%;
  border-collapse: collapse;
  overflow: auto;
}
.Reactable .rt-thead {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-thead .rt-th,
.Reactable .rt-thead .rt-td {
  line-height: normal;
  position: relative;
}
.Reactable .rt-th.rt-th-resizable {
  overflow: visible;
}
.Reactable .rt-th.rt-th-resizable:last-child {
  overflow: hidden;
}
.Reactable .rt-tbody {
  display: flex;
  flex-direction: column;
  overflow: auto;
}
.rt-td-expandable {
  cursor: pointer;
}
.Reactable .rt-tr-group {
  flex: 1 0 auto;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.Reactable .rt-tr {
  flex: 1 0 auto;
  display: flex;
}
.Reactable .rt-th,
.Reactable .rt-td {
  flex: 1 0 0;
  overflow: hidden;
}
.Reactable .rt-resizer {
  display: inline-block;
  position: absolute;
  width: 36px;
  top: 0;
  bottom: 0;
  right: -18px;
  cursor: col-resize;
  z-index: 10;
}
.Reactable .rt-tfoot {
  display: flex;
  flex-direction: column;
}
.Reactable .rt-resizing .rt-th,
.Reactable .rt-resizing .rt-td {
  transition: none !important;
  cursor: col-resize;
  user-select: none;
}

/* tmp/reactable/srcjs/reactable.css */
.Reactable {
  height: 100%;
  background-color: #fff;
}
.rt-inline {
  display: inline-flex;
}
.rt-th {
  font-weight: 600;
}
.rt-th,
.rt-td {
  display: flex;
  overflow-wrap: break-word;
  max-width: 100%;
  word-wrap: break-word;
}
.rt-th-inner,
.rt-td-inner {
  padding: 7px 8px;
  width: 100%;
  overflow: hidden;
}
.rt-compact .rt-th-inner,
.rt-compact .rt-td-inner {
  padding: 4px 6px;
}
.rt-text-content {
  overflow: hidden;
}
.rt-nowrap .rt-th-inner,
.rt-nowrap .rt-td-inner,
.rt-nowrap .rt-text-content {
  white-space: nowrap;
  text-overflow: ellipsis;
}
.rt-select {
  display: flex;
  align-items: center;
  justify-content: center;
}
input[type=checkbox].rt-select-input,
input[type=radio].rt-select-input {
  display: block;
  margin: 0;
}
.rt-align-left {
  text-align: left;
}
.rt-align-right {
  text-align: right;
}
.rt-align-center {
  text-align: center;
}
.rt-valign-center {
  align-items: center;
}
.rt-valign-bottom {
  align-items: flex-end;
}
.rt-tr,
.rt-tr-group,
.rt-tbody {
  background-color: inherit;
}
.rt-sticky {
  background-color: inherit;
  z-index: 1;
}
.rt-table {
  border-width: 1px;
  border-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-table,
.rt-bordered .rt-table {
  border-style: solid;
}
.Reactable:not(.rt-keyboard-active) .rt-table:focus {
  outline-width: 0;
  outline-style: solid;
}
.rt-th {
  border-bottom: 2px solid hsl(0, 0%, 90%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-outlined .rt-th,
.rt-bordered .rt-th {
  border-bottom-width: 1px;
}
.rt-td {
  border-top: 1px solid hsl(0, 0%, 95%);
  border-left-width: 1px;
  border-left-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-group:first-child > .rt-tr:first-child .rt-td {
  border-top: none;
}
.rt-borderless .rt-td {
  border-top: none;
}
.rt-bordered .rt-td,
.rt-bordered .rt-th {
  border-left-style: solid;
}
.rt-bordered .rt-td:first-child,
.rt-bordered .rt-th:first-child {
  border-left: none;
}
.rt-th-group,
.rt-th-group-none {
  border-bottom-style: none;
}
.rt-th-group::after {
  content: "";
  position: absolute;
  margin: auto;
  left: 8px;
  right: 8px;
  bottom: 0;
  width: 100%;
  height: 1px;
  background-color: hsl(0, 0%, 90%);
}
.rt-outlined .rt-th-group::after,
.rt-bordered .rt-th-group::after {
  left: 0;
  right: 0;
}
.rt-bordered .rt-th-group-none {
  border-bottom-style: solid;
}
.rt-tr-striped {
  background-color: rgba(0, 0, 0, 0.03);
}
.rt-tr-striped-sticky {
  background-color: hsl(0, 0%, 97%);
}
.rt-tr-highlight:hover {
  background-color: rgba(0, 0, 0, 0.05);
}
.rt-tr-highlight-sticky:hover {
  background-color: hsl(0, 0%, 95%);
}
.rt-tr-pad {
  user-select: none;
}
.Reactable .rt-thead,
.Reactable .rt-tfoot,
.Reactable .rt-tbody {
  flex-shrink: 0;
}
@supports (position: sticky) {
  .Reactable .rt-table {
    background: inherit;
  }
  .Reactable .rt-tbody {
    overflow: visible;
  }
  .Reactable .rt-thead {
    position: sticky;
    top: 0;
    background: inherit;
    z-index: 2;
  }
  .Reactable .rt-tfoot {
    position: sticky;
    bottom: 0;
    background: inherit;
    z-index: 2;
  }
}
@media screen and (-ms-high-contrast: active), screen and (-ms-high-contrast: none) {
  .Reactable .rt-tbody {
    overflow: auto;
    -ms-overflow-style: -ms-autohiding-scrollbar;
  }
}
.rt-td-filter {
  border-top: 0;
  border-bottom: 1px solid hsl(0, 0%, 95%);
}
.rt-borderless .rt-td-filter {
  border-bottom: 0;
}
.rt-filter {
  padding: 5px 7px;
  margin: 0;
  width: 100%;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  font-family: inherit;
  font-size: inherit;
  font-weight: normal;
  outline-width: 0;
  outline-style: solid;
}
.rt-filter:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
.rt-sort-header {
  display: flex;
}
.rt-align-center .rt-sort-header {
  justify-content: center;
}
.rt-align-right .rt-sort-header {
  justify-content: flex-end;
}
.rt-th {
  outline-width: 0;
  outline-style: solid;
}
.rt-th[aria-sort] {
  cursor: pointer;
}
.rt-th[aria-sort] .rt-sort-left::after {
  padding-right: 5px;
  line-height: 0;
}
.rt-th[aria-sort] .rt-sort-right::after {
  padding-left: 5px;
  line-height: 0;
}
.rt-th[aria-sort=ascending] .rt-sort-left::after,
.rt-th[aria-sort=ascending] .rt-sort-right::after {
  content: "\2191";
}
.rt-th[aria-sort=descending] .rt-sort-left::after,
.rt-th[aria-sort=descending] .rt-sort-right::after {
  content: "\2193";
}
.rt-th[aria-sort=none] .rt-sort::after {
  content: "\2195";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=ascending]:focus .rt-sort-right::after {
  content: "\2191";
  opacity: 0.4;
}
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-left::after,
.rt-keyboard-active .rt-th[data-sort-hint=descending]:focus .rt-sort-right::after {
  content: "\2193";
  opacity: 0.4;
}
.rt-expander-button {
  margin: 0 2px;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}
.rt-expander {
  display: inline-block;
  position: relative;
  padding: 0 8px;
  color: transparent;
  outline-width: 0;
  outline-style: solid;
}
.rt-expander::after {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-90deg);
  border-left: 5.04px solid transparent;
  border-right: 5.04px solid transparent;
  border-top: 7px solid rgba(0, 0, 0, 0.8);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  cursor: pointer;
}
.rt-expander.rt-expander-open::after {
  transform: translate(-50%, -50%) rotate(0);
}
.rt-pagination {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  padding: 6px 4px;
  border-top: 1px solid hsl(0, 0%, 95%);
}
.rt-outlined .rt-pagination,
.rt-bordered .rt-pagination {
  border-top: none;
}
.rt-pagination-info :not(:last-child) {
  margin-right: 16px;
}
.rt-page-info {
  display: inline-block;
  margin: 6px 8px;
  opacity: 0.9;
}
.rt-page-size {
  display: inline-block;
  margin: 0 8px;
}
.rt-page-size-select {
  margin: 0 2px;
}
.rt-page-size-select,
.rt-page-jump,
.rt-page-button {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  line-height: inherit;
}
.rt-page-size-select,
.rt-page-jump {
  background-color: #fff;
  padding: 3px;
  border-radius: 3px;
  border: 1px solid rgba(0, 0, 0, 0.05);
}
@supports (-moz-appearance: none) {
  .rt-page-size-select {
    -moz-appearance: none;
    padding-right: 12px;
    background-image: url('data:image/svg+xml;charset=US-ASCII,<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg"><path fill="%23333" d="M24 1.5l-12 21-12-21h24z"></path></svg>');
    background-repeat: no-repeat;
    background-position: right 6px center;
    background-size: 6px;
  }
}
.rt-page-button {
  padding: 6px 12px;
  background-color: transparent;
  border: none;
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  cursor: pointer;
}
.rt-page-button::-moz-focus-inner {
  padding: 0;
  border-style: none;
}
.rt-page-button:disabled {
  opacity: 0.6;
  cursor: default;
}
.rt-page-button:hover {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:active {
  background-color: rgba(0, 0, 0, 0.08);
}
.rt-keyboard-active .rt-page-button:focus {
  background-color: rgba(0, 0, 0, 0.04);
}
.rt-page-button:disabled:hover,
.rt-page-button:disabled:focus {
  background-color: transparent;
}
.rt-page-button-current {
  font-weight: 700;
}
.rt-page-ellipsis {
  margin: 0 4px;
  pointer-events: none;
}
.rt-page-numbers {
  display: inline-block;
  margin: 0 8px;
  white-space: nowrap;
}
.rt-page-jump {
  width: 70px;
  text-align: center;
}
.rt-tbody-no-data {
  position: relative;
}
.rt-tbody-no-data .rt-td {
  border-color: transparent;
}
.rt-no-data {
  display: block;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  line-height: 0;
  z-index: 1;
}
.rt-search {
  display: block;
  align-self: flex-end;
  margin: 0 0 8px 0;
  padding: 5px 7px;
  color: inherit;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  outline-width: 0;
  outline-style: solid;
  font-family: inherit;
  font-size: inherit;
}
.rt-search:active,
.rt-search:focus {
  border: 1px solid rgba(0, 0, 0, 0.25);
}
</style> <style>#gt-ihtml-tyujqxrgxw-container { display: block; width: 100%; font-size: 16px; margin: 10px 0; }
#gt-ihtml-tyujqxrgxw-container .gt-ihtml-header { display: block; width: 100%; text-align: center; padding: 10px 5px 8px 5px; border-top: 2px solid #A8A8A8; border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-tyujqxrgxw-container .rt-tbody { border-bottom: 2px solid #D3D3D3; }
#gt-ihtml-tyujqxrgxw-container .rt-search { margin-top: 8px; }
#gt-ihtml-tyujqxrgxw-container .gt-ihtml-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.5em; font-weight: initial; margin: 0; }
#gt-ihtml-tyujqxrgxw-container .gt-ihtml-subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 1.05em; font-weight: initial; margin: 0; }
#gt-ihtml-tyujqxrgxw-container .gt-ihtml-source-note { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", "Fira Sans", "Droid Sans", Arial, sans-serif; font-size: 90%; padding: 4px; margin: 0; }</style>
