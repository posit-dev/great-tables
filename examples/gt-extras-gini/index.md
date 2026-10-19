``` python
import polars as pl
from great_tables import GT, html
import gt_extras as gte

pre_tax_col = "gini_market__age_total"
post_tax_col = "gini_disposable__age_total"

# Read the data
df = pl.read_csv(
    "income_inequality_raw.csv",
    schema={
        "Entity": pl.String,
        "Code": pl.String,
        "Year": pl.Int64,
        post_tax_col: pl.Float64,
        pre_tax_col: pl.Float64,
        "population_historical": pl.Int64,
        "owid_region": pl.String,
    },
    null_values=["NA", ""],
)

# Propagate the region field to all rows of that country
df = (
    df.sort("Entity")
    .group_by("Entity", maintain_order=True)
    .agg(
        [
            pl.col("Code"),
            pl.col("Year"),
            pl.col(post_tax_col),
            pl.col(pre_tax_col),
            pl.col("population_historical"),
            pl.col("owid_region").fill_null(strategy="backward"),
        ]
    )
    .explode(
        [
            "Code",
            "Year",
            post_tax_col,
            pre_tax_col,
            "population_historical",
            "owid_region",
        ]
    )
)

# Drop rows where there is a null in either pre-tax or post-tax cols
df = df.drop_nulls(
    subset=(
        pl.col(post_tax_col),
        pl.col(pre_tax_col),
    )
)

# Compute the percent reduction in gini coefficient.
df = df.with_columns(
    ((pl.col(pre_tax_col) - pl.col(post_tax_col)) / pl.col(pre_tax_col) * 100)
    .round(2)
    .alias("gini_pct_change")
)

# Calculate 5-year benchmark (mean) of percent change for each country
df = df.with_columns(
    pl.col("gini_pct_change")
    .rolling_mean(window_size=5)
    .over(pl.col("Entity"))
    .alias("gini_pct_benchmark_5yr")
)

# Select rows with large population in the year 2020, sorted by coefficient post-tax
df = (
    df.filter(pl.col("population_historical").gt(40000000))
    .filter(pl.col("Year").eq(2020))
    .sort(by=pl.col(post_tax_col))
)


# Scale population
df = df.with_columns((pl.col("population_historical").log10()).alias("pop_log"))
pop_min = df["pop_log"].min() / 1
pop_max = df["pop_log"].max()

# Set up gt-extras icons, scaling population to 1-10 range
df = df.with_columns(
    ((pl.col("pop_log") - pop_min) / (pop_max - pop_min) * 10 + 1)
    .round(0)
    .cast(pl.Int64)
    .alias("pop_icons")
)

# Format original population value with commas
df = df.with_columns(
    pl.col("population_historical").map_elements(
        lambda x: f"{int(x):,}" if x is not None else None, return_dtype=pl.String
    )
)

# Apply gte.fa_icon_repeat to each entry in the pop_icons column
df_with_icons = df.with_columns(
    pl.col("pop_icons").map_elements(
        lambda x: gte.fa_icon_repeat(name="person", repeats=int(x)),
        return_dtype=pl.String,
    )
)
```


``` python
# Generate the table, before gt-extras add-ons
gt = (
    GT(df_with_icons, rowname_col="Entity", groupname_col="owid_region")
    .tab_header(
        "Income Inequality Before and After Taxes in 2020",
        "As measured by the Gini coefficient, where 0 is best and 1 is worst",
    )
    .cols_move("pop_icons", after=pre_tax_col)
    .cols_align("left")
    .cols_hide(["Year", "pop_log", "population_historical"])
    .fmt_flag("Code")
    .cols_label(
        {
            "Code": "",
            "gini_pct_change": "Improvement Post Taxes",
            "pop_icons": "Population",
        }
    )
    .tab_source_note(
        html(
            """
            <div>
            <strong>Source:</strong> Data from [#TidyTuesday](https://github.com/rfordatascience/tidytuesday) (2025-08-05).<br>
                <div>
                <strong>Dumbbell plot:</strong>
                <span style="color:#106ea0;">Blue:</span> post-tax Gini coefficient
                <span style="color:#e0b165;">Gold:</span> pre-tax Gini coefficient
                <br>
                </div>
            <strong>Bullet plot:</strong> Percent reduction in Gini after taxes for each country, compared to its 5-year average benchmark.
            </div>
            """
        )
    )
)

# Apply the gt-extras functions via pipe
(
    gt.pipe(
        gte.gt_plt_dumbbell,
        col1=pre_tax_col,
        col2=post_tax_col,
        col1_color="#e0b165",
        col2_color="#106ea0",
        dot_border_color="transparent",
        num_decimals=2,
        width=240,
        label="Pre-tax to Post-tax Coefficient",
    )
    .pipe(
        gte.gt_plt_bullet,
        "gini_pct_change",
        "gini_pct_benchmark_5yr",
        fill="#963d4c",
        target_color="#3D3D3D",
        bar_height=15,
        width=200,
    )
    .pipe(
        gte.gt_merge_stack,
        col1="pop_icons",
        col2="population_historical",
    )
    .pipe(gte.gt_theme_guardian)
)
```


<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap');
#tuuwinrmyr table {
          font-family: 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tuuwinrmyr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tuuwinrmyr p { margin: 0; padding: 0; }
 #tuuwinrmyr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #f6f6f6; width: auto; border-top-style: solid; border-top-width: 1px; border-top-color: #40c5ff; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: white; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tuuwinrmyr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tuuwinrmyr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #f6f6f6; border-bottom-width: 0; }
 #tuuwinrmyr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #f6f6f6; border-top-width: 0; }
 #tuuwinrmyr .gt_heading { background-color: #f6f6f6; text-align: left; border-bottom-color: #f6f6f6; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tuuwinrmyr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #D3D3D3; }
 #tuuwinrmyr .gt_col_headings { border-top-style: solid; border-top-width: 1px; border-top-color: #ececec; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #ececec; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tuuwinrmyr .gt_col_heading { color: #333333; background-color: #f6f6f6; font-size: 100%; font-weight: bold; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tuuwinrmyr .gt_column_spanner_outer { color: #333333; background-color: #f6f6f6; font-size: 100%; font-weight: bold; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tuuwinrmyr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tuuwinrmyr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tuuwinrmyr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #ececec; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tuuwinrmyr .gt_spanner_row { border-bottom-style: hidden; }
 #tuuwinrmyr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #f6f6f6; font-size: 100%; font-weight: bold; text-transform: inherit; border-top-style: solid; border-top-width: 1px; border-top-color: grey; border-bottom-style: solid; border-bottom-width: 1px; border-bottom-color: grey; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tuuwinrmyr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #f6f6f6; font-size: 100%; font-weight: bold; border-top-style: solid; border-top-width: 1px; border-top-color: grey; border-bottom-style: solid; border-bottom-width: 1px; border-bottom-color: grey; vertical-align: middle; }
 #tuuwinrmyr .gt_from_md> :first-child { margin-top: 0; }
 #tuuwinrmyr .gt_from_md> :last-child { margin-bottom: 0; }
 #tuuwinrmyr .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 0px; border-top-color: white; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tuuwinrmyr .gt_stub { color: #333333; background-color: #f6f6f6; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tuuwinrmyr .gt_indent_1 { text-indent: 5px; }
 #tuuwinrmyr .gt_indent_2 { text-indent: calc(5px * 2); }
 #tuuwinrmyr .gt_indent_3 { text-indent: calc(5px * 3); }
 #tuuwinrmyr .gt_indent_4 { text-indent: calc(5px * 4); }
 #tuuwinrmyr .gt_indent_5 { text-indent: calc(5px * 5); }
 #tuuwinrmyr .gt_stub_row_group { color: #333333; background-color: #f6f6f6; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tuuwinrmyr .gt_row_group_first td { border-top-width: 1px; }
 #tuuwinrmyr .gt_row_group_first th { border-top-width: 1px; }
 #tuuwinrmyr .gt_striped { color: #333333; background-color: #ececec; }
 #tuuwinrmyr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: white; }
 #tuuwinrmyr .gt_summary_row { color: #333333; background-color: #f6f6f6; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tuuwinrmyr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tuuwinrmyr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tuuwinrmyr .gt_grand_summary_row { color: #333333; background-color: #f6f6f6; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tuuwinrmyr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tuuwinrmyr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tuuwinrmyr .gt_sourcenotes { color: #333333; background-color: #f6f6f6; border-bottom-style: none; border-bottom-width: 0px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tuuwinrmyr .gt_sourcenote { font-size: 12px; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tuuwinrmyr .gt_left { text-align: left; }
 #tuuwinrmyr .gt_center { text-align: center; }
 #tuuwinrmyr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tuuwinrmyr .gt_font_normal { font-weight: normal; }
 #tuuwinrmyr .gt_font_bold { font-weight: bold; }
 #tuuwinrmyr .gt_font_italic { font-style: italic; }
 #tuuwinrmyr .gt_super { font-size: 65%; }
 #tuuwinrmyr .gt_footnotes { color: font-color(#f6f6f6); background-color: #f6f6f6; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tuuwinrmyr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tuuwinrmyr .gt_sourcenotes { color: #333333; background-color: #f6f6f6; border-bottom-style: none; border-bottom-width: 0px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tuuwinrmyr .gt_sourcenote { font-size: 12px; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tuuwinrmyr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tuuwinrmyr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="5" id="title" class="gt_heading gt_title gt_font_normal" style="color: #005689; font-size: 22px; font-weight: bold">Income Inequality Before and After Taxes in 2020</th>
</tr>
<tr class="gt_heading">
<th colspan="5" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="color: #005689; font-size: 16px; font-weight: bold">As measured by the Gini coefficient, where 0 is best and 1 is worst</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="Code" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="gini_market__age_total" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Pre-tax to Post-tax Coefficient</th>
<th id="pop_icons" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Population</th>
<th id="gini_pct_change" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Improvement Post Taxes</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="5" id="Europe" class="gt_group_heading" scope="colgroup">Europe</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">France</td>
<td class="gt_row gt_left" headers="Europe stub-1 Code"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iRnJhbmNlIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld2JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5O2hlaWdodDoxZW07d2lkdGg6MWVtOyI+PHRpdGxlPkZyYW5jZTwvdGl0bGU+PG1hc2sgaWQ9IkNvZGUtMC1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjQ29kZS0wLWEpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTY3IDBoMTc4bDI1LjkgMjUyLjNMMzQ1IDUxMkgxNjdsLTI5LjgtMjUzLjR6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMTY3djUxMkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzQ1IDBoMTY3djUxMkgzNDV6IiAvPjwvZz48L3N2Zz4=" /></span></td>
<td class="gt_row gt_left" headers="Europe stub-1 gini_market__age_total"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjE5Ljk5OTk5OTk5OTk5OTk4NiIgeT0iMTguNSIgd2lkdGg9IjE3Mi45OTI3MDA3Mjk5MjcwNCIgaGVpZ2h0PSIzLjAiIHJ4PSIyIiBmaWxsPSJncmV5IiAvPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSIxOTIuOTkyNzAwNzI5OTI3IiBjeT0iMjAuMCIgcj0iMy43NSIgZmlsbD0iI2UwYjE2NSI+PC9jaXJjbGU+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE5Ljk5OTk5OTk5OTk5OTk4NiIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiMxMDZlYTAiPjwvY2lyY2xlPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiNlMGIxNjUiIHg9IjE5Mi45OTI3MDA3Mjk5MjciIHk9IjE0LjQ1Ij4wLjUyPC90ZXh0Pjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMxMDZlYTAiIHg9IjE5Ljk5OTk5OTk5OTk5OTk4NiIgeT0iMTQuNDUiPjAuMjg8L3RleHQ+PC9zdmc+" />
</div></td>
<td class="gt_row gt_left" headers="Europe stub-1 pop_icons"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 65,905,226 </span>

</div></td>
<td class="gt_row gt_left" headers="Europe stub-1 gini_pct_change"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMjAwLjBweCIgaGVpZ2h0PSIxNXB4IiBmaWxsPSIjOTYzZDRjIiAvPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjkuMCIgZmlsbD0iYmxhY2siIHg9IjE5Ni4wcHgiIHk9IjE1LjBweCI+PC90ZXh0PjxsaW5lIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIzMHB4Ij48L2xpbmU+PC9zdmc+" />
</div></td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Germany</td>
<td class="gt_row gt_left gt_striped" headers="Europe stub-2 Code"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iR2VybWFueSIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5HZXJtYW55PC90aXRsZT48bWFzayBpZD0iQ29kZS0xLWEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNDb2RlLTEtYSkiPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Im0wIDM0NSAyNTYuNy0yNS41TDUxMiAzNDV2MTY3SDB6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Im0wIDE2NyAyNTUtMjMgMjU3IDIzdjE3OEgweiIgLz48cGF0aCBmaWxsPSIjMzMzIiBkPSJNMCAwaDUxMnYxNjdIMHoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left gt_striped" headers="Europe stub-2 gini_market__age_total"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjM4LjI0ODE3NTE4MjQ4MTcxIiB5PSIxOC41IiB3aWR0aD0iMTQwLjg3NTkxMjQwODc1OTE1IiBoZWlnaHQ9IjMuMCIgcng9IjIiIGZpbGw9ImdyZXkiIC8+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE3OS4xMjQwODc1OTEyNDA4NSIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiNlMGIxNjUiPjwvY2lyY2xlPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSIzOC4yNDgxNzUxODI0ODE3MSIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiMxMDZlYTAiPjwvY2lyY2xlPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiNlMGIxNjUiIHg9IjE3OS4xMjQwODc1OTEyNDA4NSIgeT0iMTQuNDUiPjAuNTwvdGV4dD48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjMTA2ZWEwIiB4PSIzOC4yNDgxNzUxODI0ODE3MSIgeT0iMTQuNDUiPjAuMzwvdGV4dD48L3N2Zz4=" />
</div></td>
<td class="gt_row gt_left gt_striped" headers="Europe stub-2 pop_icons"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 83,628,661 </span>

</div></td>
<td class="gt_row gt_left gt_striped" headers="Europe stub-2 gini_pct_change"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTY5LjEwMDM5MTEzNDI4OTRweCIgaGVpZ2h0PSIxNXB4IiBmaWxsPSIjOTYzZDRjIiAvPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjkuMCIgZmlsbD0iYmxhY2siIHg9IjE2NS43MTgzODMzMTE2MDM2MnB4IiB5PSIxNS4wcHgiPjwvdGV4dD48bGluZSBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjMuMHB4IiB4MT0iMCIgeTE9IjAiIHgyPSIwIiB5Mj0iMzBweCI+PC9saW5lPjxsaW5lIHN0cm9rZT0iIzNEM0QzRCIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjE3Ni41MzU2MzY2Nzk3MDQ0OHB4IiB5MT0iMCIgeDI9IjE3Ni41MzU2MzY2Nzk3MDQ0OHB4IiB5Mj0iMzBweCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Spain</td>
<td class="gt_row gt_left" headers="Europe stub-4 Code"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU3BhaW4iIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U3BhaW48L3RpdGxlPjxtYXNrIGlkPSJDb2RlLTMtYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI0NvZGUtMy1hKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTAgMTI4IDI1Ni0zMiAyNTYgMzJ2MjU2bC0yNTYgMzJMMCAzODRaIiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0wIDBoNTEydjEyOEgwem0wIDM4NGg1MTJ2MTI4SDB6IiAvPjxnIGZpbGw9IiNlZWUiPjxwYXRoIGQ9Ik0xNDQgMzA0aC0xNnYtODBoMTZ6bTEyOCAwaDE2di04MGgtMTZ6IiAvPjxlbGxpcHNlIGN4PSIyMDgiIGN5PSIyOTYiIHJ4PSI0OCIgcnk9IjMyIj48L2VsbGlwc2U+PC9nPjxnIGZpbGw9IiNkODAwMjciPjxyZWN0IHdpZHRoPSIxNiIgaGVpZ2h0PSIyNCIgeD0iMTI4IiB5PSIxOTIiIHJ4PSI4IiAvPjxyZWN0IHdpZHRoPSIxNiIgaGVpZ2h0PSIyNCIgeD0iMjcyIiB5PSIxOTIiIHJ4PSI4IiAvPjxwYXRoIGQ9Ik0yMDggMjcydjI0YTI0IDI0IDAgMCAwIDI0IDI0IDI0IDI0IDAgMCAwIDI0LTI0di0yNGgtMjR6IiAvPjwvZz48cmVjdCB3aWR0aD0iMzIiIGhlaWdodD0iMTYiIHg9IjEyMCIgeT0iMjA4IiBmaWxsPSIjZmY5ODExIiByeT0iOCIgLz48cmVjdCB3aWR0aD0iMzIiIGhlaWdodD0iMTYiIHg9IjI2NCIgeT0iMjA4IiBmaWxsPSIjZmY5ODExIiByeT0iOCIgLz48cmVjdCB3aWR0aD0iMzIiIGhlaWdodD0iMTYiIHg9IjEyMCIgeT0iMzA0IiBmaWxsPSIjZmY5ODExIiByeD0iOCIgLz48cmVjdCB3aWR0aD0iMzIiIGhlaWdodD0iMTYiIHg9IjI2NCIgeT0iMzA0IiBmaWxsPSIjZmY5ODExIiByeD0iOCIgLz48cGF0aCBmaWxsPSIjZmY5ODExIiBkPSJNMTYwIDI3MnYyNGMwIDggNCAxNCA5IDE5bDUtNiA1IDEwYTIxIDIxIDAgMCAwIDEwIDBsNS0xMCA1IDZjNi01IDktMTEgOS0xOXYtMjRoLTlsLTUgOC01LThoLTEwbC01IDgtNS04eiIgLz48cGF0aCBkPSJNMTIyIDI1MmgxNzJtLTE3MiAyNGgyOG0xMTYgMGgyOCIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMTIyIDI0OGE0IDQgMCAwIDAtNCA0IDQgNCAwIDAgMCA0IDRoMTcyYTQgNCAwIDAgMCA0LTQgNCA0IDAgMCAwLTQtNHptMCAyNGE0IDQgMCAwIDAtNCA0IDQgNCAwIDAgMCA0IDRoMjhhNCA0IDAgMCAwIDQtNCA0IDQgMCAwIDAtNC00em0xNDQgMGE0IDQgMCAwIDAtNCA0IDQgNCAwIDAgMCA0IDRoMjhhNCA0IDAgMCAwIDQtNCA0IDQgMCAwIDAtNC00eiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTk2IDE2OGMtNyAwLTEzIDUtMTUgMTFsLTUtMWMtOSAwLTE2IDctMTYgMTZzNyAxNiAxNiAxNmM3IDAgMTMtNCAxNS0xMWExNiAxNiAwIDAgMCAxNy00IDE2IDE2IDAgMCAwIDE3IDQgMTYgMTYgMCAxIDAgMTAtMjAgMTYgMTYgMCAwIDAtMjctNWMtMy00LTctNi0xMi02em0wIDhjNSAwIDggNCA4IDggMCA1LTMgOC04IDgtNCAwLTgtMy04LTggMC00IDQtOCA4LTh6bTI0IDBjNSAwIDggNCA4IDggMCA1LTMgOC04IDgtNCAwLTgtMy04LTggMC00IDQtOCA4LTh6bS00NCAxMCA0IDEgNCA4YzAgNC00IDctOCA3cy04LTMtOC04YzAtNCA0LTggOC04em02NCAwYzUgMCA4IDQgOCA4IDAgNS0zIDgtOCA4LTQgMC04LTMtOC03bDQtOHoiIC8+PHBhdGggZmlsbD0ibm9uZSIgZD0iTTIyMCAyODR2MTJjMCA3IDUgMTIgMTIgMTJzMTItNSAxMi0xMnYtMTJ6IiAvPjxwYXRoIGZpbGw9IiNmZjk4MTEiIGQ9Ik0yMDAgMTYwaDE2djMyaC0xNnoiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTIwOCAyMjRoNDh2NDhoLTQ4eiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJtMjQ4IDIwOC04IDhoLTY0bC04LThjMC0xMyAxOC0yNCA0MC0yNHM0MCAxMSA0MCAyNHptLTg4IDE2aDQ4djQ4aC00OHoiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjMyIiB4PSIyMjIiIHk9IjIzMiIgZmlsbD0iI2Q4MDAyNyIgcng9IjEwIiByeT0iMTAiIC8+PHBhdGggZmlsbD0iI2ZmOTgxMSIgZD0iTTE2OCAyMzJ2OGg4djE2aC04djhoMzJ2LThoLTh2LTE2aDh2LTh6bTgtMTZoNjR2OGgtNjR6IiAvPjxnIGZpbGw9IiNmZmRhNDQiPjxjaXJjbGUgY3g9IjE4NiIgY3k9IjIwMiIgcj0iNiI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjA4IiBjeT0iMjAyIiByPSI2Ij48L2NpcmNsZT48Y2lyY2xlIGN4PSIyMzAiIGN5PSIyMDIiIHI9IjYiPjwvY2lyY2xlPjwvZz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMTY5IDI3MnY0M2EyNCAyNCAwIDAgMCAxMCA0di00N2gtMTB6bTIwIDB2NDdhMjQgMjQgMCAwIDAgMTAtNHYtNDNoLTEweiIgLz48ZyBmaWxsPSIjMzM4YWYzIj48Y2lyY2xlIGN4PSIyMDgiIGN5PSIyNzIiIHI9IjE2Ij48L2NpcmNsZT48cmVjdCB3aWR0aD0iMzIiIGhlaWdodD0iMTYiIHg9IjI2NCIgeT0iMzIwIiByeT0iOCIgLz48cmVjdCB3aWR0aD0iMzIiIGhlaWdodD0iMTYiIHg9IjEyMCIgeT0iMzIwIiByeT0iOCIgLz48L2c+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left" headers="Europe stub-4 gini_market__age_total"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjU3LjIyNjI3NzM3MjI2Mjc2IiB5PSIxOC41IiB3aWR0aD0iMTM1Ljc2NjQyMzM1NzY2NDI1IiBoZWlnaHQ9IjMuMCIgcng9IjIiIGZpbGw9ImdyZXkiIC8+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE5Mi45OTI3MDA3Mjk5MjciIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjZTBiMTY1Ij48L2NpcmNsZT48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iNTcuMjI2Mjc3MzcyMjYyNzYiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIxOTIuOTkyNzAwNzI5OTI3IiB5PSIxNC40NSI+MC41MjwvdGV4dD48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjMTA2ZWEwIiB4PSI1Ny4yMjYyNzczNzIyNjI3NiIgeT0iMTQuNDUiPjAuMzM8L3RleHQ+PC9zdmc+" />
</div></td>
<td class="gt_row gt_left" headers="Europe stub-4 pop_icons"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 47,679,437 </span>

</div></td>
<td class="gt_row gt_left" headers="Europe stub-4 gini_pct_change"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTU2Ljk3NTIyODE2MTY2ODhweCIgaGVpZ2h0PSIxNXB4IiBmaWxsPSIjOTYzZDRjIiAvPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjkuMCIgZmlsbD0iYmxhY2siIHg9IjE1My44MzU3MjM1OTg0MzU0NHB4IiB5PSIxNS4wcHgiPjwvdGV4dD48bGluZSBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjMuMHB4IiB4MT0iMCIgeTE9IjAiIHgyPSIwIiB5Mj0iMzBweCI+PC9saW5lPjxsaW5lIHN0cm9rZT0iIzNEM0QzRCIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjE0OS43MDM4MjQ0MjQxNjMzN3B4IiB5MT0iMCIgeDI9IjE0OS43MDM4MjQ0MjQxNjMzN3B4IiB5Mj0iMzBweCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Italy</td>
<td class="gt_row gt_left gt_striped" headers="Europe stub-5 Code"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iSXRhbHkiIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+SXRhbHk8L3RpdGxlPjxtYXNrIGlkPSJDb2RlLTQtYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI0NvZGUtNC1hKSI+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTE2NyAwaDE3OGwyNS45IDI1Mi4zTDM0NSA1MTJIMTY3bC0yOS44LTI1My40eiIgLz48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMCAwaDE2N3Y1MTJIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTM0NSAwaDE2N3Y1MTJIMzQ1eiIgLz48L2c+PC9zdmc+" /></span></td>
<td class="gt_row gt_left gt_striped" headers="Europe stub-5 gini_market__age_total"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjU4LjY4NjEzMTM4Njg2MTMiIHk9IjE4LjUiIHdpZHRoPSIxNDMuMDY1NjkzNDMwNjU2OTUiIGhlaWdodD0iMy4wIiByeD0iMiIgZmlsbD0iZ3JleSIgLz48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iMjAxLjc1MTgyNDgxNzUxODI0IiBjeT0iMjAuMCIgcj0iMy43NSIgZmlsbD0iI2UwYjE2NSI+PC9jaXJjbGU+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjU4LjY4NjEzMTM4Njg2MTMiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIyMDEuNzUxODI0ODE3NTE4MjQiIHk9IjE0LjQ1Ij4wLjUzPC90ZXh0Pjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMxMDZlYTAiIHg9IjU4LjY4NjEzMTM4Njg2MTMiIHk9IjE0LjQ1Ij4wLjMzPC90ZXh0Pjwvc3ZnPg==" />
</div></td>
<td class="gt_row gt_left gt_striped" headers="Europe stub-5 pop_icons"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 59,912,714 </span>

</div></td>
<td class="gt_row gt_left gt_striped" headers="Europe stub-5 gini_pct_change"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTYxLjYyNTM4MDI2OTQ0ODA0cHgiIGhlaWdodD0iMTVweCIgZmlsbD0iIzk2M2Q0YyIgLz48dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSI5LjAiIGZpbGw9ImJsYWNrIiB4PSIxNTguMzkyODcyNjY0MDU5MDdweCIgeT0iMTUuMHB4Ij48L3RleHQ+PGxpbmUgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjMwcHgiPjwvbGluZT48bGluZSBzdHJva2U9IiMzRDNEM0QiIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSIxNTUuMzAxMzkwNjk5Njk1OHB4IiB5MT0iMCIgeDI9IjE1NS4zMDEzOTA2OTk2OTU4cHgiIHkyPSIzMHB4Ij48L2xpbmU+PC9zdmc+" />
</div></td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">United Kingdom</td>
<td class="gt_row gt_left" headers="Europe stub-6 Code"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iVW5pdGVkIEtpbmdkb20iIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+VW5pdGVkIEtpbmdkb208L3RpdGxlPjxtYXNrIGlkPSJDb2RlLTUtYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI0NvZGUtNS1hKSI+PHBhdGggZmlsbD0iI2VlZSIgZD0ibTAgMCA4IDIyLTggMjN2MjNsMzIgNTQtMzIgNTR2MzJsMzIgNDgtMzIgNDh2MzJsMzIgNTQtMzIgNTR2NjhsMjItOCAyMyA4aDIzbDU0LTMyIDU0IDMyaDMybDQ4LTMyIDQ4IDMyaDMybDU0LTMyIDU0IDMyaDY4bC04LTIyIDgtMjN2LTIzbC0zMi01NCAzMi01NHYtMzJsLTMyLTQ4IDMyLTQ4di0zMmwtMzItNTQgMzItNTRWMGwtMjIgOC0yMy04aC0yM2wtNTQgMzItNTQtMzJoLTMybC00OCAzMi00OC0zMmgtMzJsLTU0IDMyTDY4IDBIMHoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTMzNiAwdjEwOEw0NDQgMFptMTc2IDY4TDQwNCAxNzZoMTA4ek0wIDE3NmgxMDhMMCA2OFpNNjggMGwxMDggMTA4VjBabTEwOCA1MTJWNDA0TDY4IDUxMlpNMCA0NDRsMTA4LTEwOEgwWm01MTItMTA4SDQwNGwxMDggMTA4Wm0tNjggMTc2TDMzNiA0MDR2MTA4eiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMCAwdjQ1bDEzMSAxMzFoNDVMMCAwem0yMDggMHYyMDhIMHY5NmgyMDh2MjA4aDk2VjMwNGgyMDh2LTk2SDMwNFYwaC05NnptMjU5IDBMMzM2IDEzMXY0NUw1MTIgMGgtNDV6TTE3NiAzMzYgMCA1MTJoNDVsMTMxLTEzMXYtNDV6bTE2MCAwIDE3NiAxNzZ2LTQ1TDM4MSAzMzZoLTQ1eiIgLz48L2c+PC9zdmc+" /></span></td>
<td class="gt_row gt_left" headers="Europe stub-6 gini_market__age_total"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9Ijc2LjIwNDM3OTU2MjA0Mzc1IiB5PSIxOC41IiB3aWR0aD0iMTEwLjk0ODkwNTEwOTQ4OTA2IiBoZWlnaHQ9IjMuMCIgcng9IjIiIGZpbGw9ImdyZXkiIC8+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE4Ny4xNTMyODQ2NzE1MzI4MiIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiNlMGIxNjUiPjwvY2lyY2xlPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSI3Ni4yMDQzNzk1NjIwNDM3NSIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiMxMDZlYTAiPjwvY2lyY2xlPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiNlMGIxNjUiIHg9IjE4Ny4xNTMyODQ2NzE1MzI4MiIgeT0iMTQuNDUiPjAuNTE8L3RleHQ+PHRleHQgZG9taW5hbnQtYmFzZWxpbmU9Imxvd2VyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzEwNmVhMCIgeD0iNzYuMjA0Mzc5NTYyMDQzNzUiIHk9IjE0LjQ1Ij4wLjM1PC90ZXh0Pjwvc3ZnPg==" />
</div></td>
<td class="gt_row gt_left" headers="Europe stub-6 pop_icons"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 67,351,806 </span>

</div></td>
<td class="gt_row gt_left" headers="Europe stub-6 gini_pct_change"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTMwLjI5MTE3Nzc0ODgwNDg0cHgiIGhlaWdodD0iMTVweCIgZmlsbD0iIzk2M2Q0YyIgLz48dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSI5LjAiIGZpbGw9ImJsYWNrIiB4PSIxMjcuNjg1MzU0MTkzODI4NzRweCIgeT0iMTUuMHB4Ij48L3RleHQ+PGxpbmUgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjMwcHgiPjwvbGluZT48bGluZSBzdHJva2U9IiMzRDNEM0QiIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSIxMjUuOTc1MDEwODY0ODQxMzdweCIgeTE9IjAiIHgyPSIxMjUuOTc1MDEwODY0ODQxMzdweCIgeTI9IjMwcHgiPjwvbGluZT48L3N2Zz4=" />
</div></td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" id="Asia" class="gt_group_heading" scope="colgroup">Asia</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">South Korea</td>
<td class="gt_row gt_left gt_striped" headers="Asia stub-3 Code"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iS29yZWEsIFJlcC4iIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+S29yZWEsIFJlcC48L3RpdGxlPjxtYXNrIGlkPSJDb2RlLTItYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI0NvZGUtMi1hKSI+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTAgMGg1MTJ2NTEySDBaIiAvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Im0zNTAgMzM1IDI0LTI0IDE2IDE2LTI0IDIzem0tMzkgMzkgMjQtMjQgMTUgMTYtMjMgMjR6bTg3IDggMjMtMjQgMTYgMTYtMjQgMjR6bS00MCAzOSAyNC0yMyAxNiAxNS0yNCAyNFptMTYtNjMgMjQtMjMgMTUgMTUtMjMgMjR6bS0zOSA0MCAyMy0yNCAxNiAxNi0yNCAyM3ptNjMtMjIxLTYzLTYzIDE1LTE1IDY0IDYzem0tNjMtMTUtMjQtMjQgMTYtMTYgMjMgMjR6bTM5IDM5LTI0LTI0IDE2LTE1IDI0IDIzem04LTg3LTI0LTIzIDE2LTE2IDI0IDI0Wm0zOSA0MC0yMy0yNCAxNS0xNiAyNCAyNFpNOTEgMzU4bDYzIDYzLTE2IDE2LTYzLTYzem02MyAxNiAyMyAyNC0xNSAxNS0yNC0yM3ptLTQwLTM5IDI0IDIzLTE2IDE2LTIzLTI0em0yNC0yNCA2MyA2My0xNiAxNi02My02M3ptMTYtMjIwLTYzIDYzLTE2LTE2IDYzLTYzem0yMyAyMy02MyA2My0xNS0xNiA2My02M3ptMjQgMjQtNjMgNjMtMTYtMTYgNjMtNjN6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0zMTkgMzE5IDE5MyAxOTNhODkgODkgMCAxIDEgMTI2IDEyNnoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTMxOSAzMTlhODkgODkgMCAxIDEtMTI2LTEyNnoiIC8+PGNpcmNsZSBjeD0iMjI0LjUiIGN5PSIyMjQuNSIgcj0iNDQuNSIgZmlsbD0iI2Q4MDAyNyI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjg3LjUiIGN5PSIyODcuNSIgcj0iNDQuNSIgZmlsbD0iIzAwNTJiNCI+PC9jaXJjbGU+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left gt_striped" headers="Asia stub-3 gini_market__age_total"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjU2LjQ5NjM1MDM2NDk2MzQ4IiB5PSIxOC41IiB3aWR0aD0iNTYuMjA0Mzc5NTYyMDQzODIiIGhlaWdodD0iMy4wIiByeD0iMiIgZmlsbD0iZ3JleSIgLz48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iMTEyLjcwMDcyOTkyNzAwNzMiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjZTBiMTY1Ij48L2NpcmNsZT48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iNTYuNDk2MzUwMzY0OTYzNDgiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIxMTIuNzAwNzI5OTI3MDA3MyIgeT0iMTQuNDUiPjAuNDE8L3RleHQ+PHRleHQgZG9taW5hbnQtYmFzZWxpbmU9Imxvd2VyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzEwNmVhMCIgeD0iNTYuNDk2MzUwMzY0OTYzNDgiIHk9IjE0LjQ1Ij4wLjMzPC90ZXh0Pjwvc3ZnPg==" />
</div></td>
<td class="gt_row gt_left gt_striped" headers="Asia stub-3 pop_icons"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 51,858,440 </span>

</div></td>
<td class="gt_row gt_left gt_striped" headers="Asia stub-3 gini_pct_change"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iODIuNjE2MjUzODAyNjk0NDlweCIgaGVpZ2h0PSIxNXB4IiBmaWxsPSIjOTYzZDRjIiAvPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjkuMCIgZmlsbD0iYmxhY2siIHg9IjgwLjk2MzkyODcyNjY0MDZweCIgeT0iMTUuMHB4Ij48L3RleHQ+PGxpbmUgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjMwcHgiPjwvbGluZT48bGluZSBzdHJva2U9IiMzRDNEM0QiIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSI2Mi42Mjg2Mzk3MjE4NjAwNTRweCIgeTE9IjAiIHgyPSI2Mi42Mjg2Mzk3MjE4NjAwNTRweCIgeTI9IjMwcHgiPjwvbGluZT48L3N2Zz4=" />
</div></td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">Turkey</td>
<td class="gt_row gt_left" headers="Asia stub-8 Code"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iVHVya2l5ZSIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5UdXJraXllPC90aXRsZT48bWFzayBpZD0iQ29kZS03LWEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNDb2RlLTctYSkiPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0wIDBoNTEydjUxMkgweiIgLz48ZyBmaWxsPSIjZWVlIj48cGF0aCBkPSJtMjQ1LjUgMjA5LjIgMjEgMjkgMzQtMTEuMS0yMSAyOSAyMSAyOC45LTM0LTExLjEtMjEgMjlWMjY3bC0zNC0xMS4xIDM0LTExeiIgLz48cGF0aCBkPSJNMTg4LjIgMzI4LjNhNzIuMyA3Mi4zIDAgMSAxIDM0LjQtMTM2IDg5IDg5IDAgMSAwIDAgMTI3LjMgNzIgNzIgMCAwIDEtMzQuNCA4Ljd6IiAvPjwvZz48L2c+PC9zdmc+" /></span></td>
<td class="gt_row gt_left" headers="Asia stub-8 gini_market__age_total"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjExMS4yNDA4NzU5MTI0MDg3NSIgeT0iMTguNSIgd2lkdGg9IjczLjcyMjYyNzczNzIyNjI2IiBoZWlnaHQ9IjMuMCIgcng9IjIiIGZpbGw9ImdyZXkiIC8+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE4NC45NjM1MDM2NDk2MzUwMiIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiNlMGIxNjUiPjwvY2lyY2xlPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSIxMTEuMjQwODc1OTEyNDA4NzUiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIxODQuOTYzNTAzNjQ5NjM1MDIiIHk9IjE0LjQ1Ij4wLjU8L3RleHQ+PHRleHQgZG9taW5hbnQtYmFzZWxpbmU9Imxvd2VyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzEwNmVhMCIgeD0iMTExLjI0MDg3NTkxMjQwODc1IiB5PSIxNC40NSI+MC40PC90ZXh0Pjwvc3ZnPg==" />
</div></td>
<td class="gt_row gt_left" headers="Asia stub-8 pop_icons"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 86,091,644 </span>

</div></td>
<td class="gt_row gt_left" headers="Asia stub-8 gini_pct_change"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iODcuMDkyNTY4NDQ4NTAwNjRweCIgaGVpZ2h0PSIxNXB4IiBmaWxsPSIjOTYzZDRjIiAvPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjkuMCIgZmlsbD0iYmxhY2siIHg9Ijg1LjM1MDcxNzA3OTUzMDYzcHgiIHk9IjE1LjBweCI+PC90ZXh0PjxsaW5lIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIzMHB4Ij48L2xpbmU+PGxpbmUgc3Ryb2tlPSIjM0QzRDNEIiBzdHJva2Utd2lkdGg9IjMuMHB4IiB4MT0iNjguOTM4OTM5NTkxNDgxOTVweCIgeTE9IjAiIHgyPSI2OC45Mzg5Mzk1OTE0ODE5NXB4IiB5Mj0iMzBweCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" id="North-America" class="gt_group_heading" scope="colgroup">North America</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">United States</td>
<td class="gt_row gt_left gt_striped" headers="North-America stub-7 Code"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iVW5pdGVkIFN0YXRlcyIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5Vbml0ZWQgU3RhdGVzPC90aXRsZT48bWFzayBpZD0iQ29kZS02LWEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNDb2RlLTYtYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0yNTYgMGgyNTZ2NjRsLTMyIDMyIDMyIDMydjY0bC0zMiAzMiAzMiAzMnY2NGwtMzIgMzIgMzIgMzJ2NjRsLTI1NiAzMkwwIDQ0OHYtNjRsMzItMzItMzItMzJ2LTY0eiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMjI0IDY0aDI4OHY2NEgyMjRabTAgMTI4aDI4OHY2NEgyNTZaTTAgMzIwaDUxMnY2NEgwWm0wIDEyOGg1MTJ2NjRIMFoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTAgMGgyNTZ2MjU2SDBaIiAvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Im0xODcgMjQzIDU3LTQxaC03MGw1NyA0MS0yMi02N3ptLTgxIDAgNTctNDFIOTNsNTcgNDEtMjItNjd6bS04MSAwIDU3LTQxSDEybDU3IDQxLTIyLTY3em0xNjItODEgNTctNDFoLTcwbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUg5M2w1NyA0MS0yMi02N3ptLTgxIDAgNTctNDFIMTJsNTcgNDEtMjItNjdabTE2Mi04MiA1Ny00MWgtNzBsNTcgNDEtMjItNjdabS04MSAwIDU3LTQxSDkzbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUgxMmw1NyA0MS0yMi02N1oiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left gt_striped" headers="North-America stub-7 gini_market__age_total"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjkyLjI2Mjc3MzcyMjYyNzciIHk9IjE4LjUiIHdpZHRoPSIxMDUuMTA5NDg5MDUxMDk0OTQiIGhlaWdodD0iMy4wIiByeD0iMiIgZmlsbD0iZ3JleSIgLz48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iMTk3LjM3MjI2Mjc3MzcyMjY0IiBjeT0iMjAuMCIgcj0iMy43NSIgZmlsbD0iI2UwYjE2NSI+PC9jaXJjbGU+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjkyLjI2Mjc3MzcyMjYyNzciIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIxOTcuMzcyMjYyNzczNzIyNjQiIHk9IjE0LjQ1Ij4wLjUyPC90ZXh0Pjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMxMDZlYTAiIHg9IjkyLjI2Mjc3MzcyMjYyNzciIHk9IjE0LjQ1Ij4wLjM4PC90ZXh0Pjwvc3ZnPg==" />
</div></td>
<td class="gt_row gt_left gt_striped" headers="North-America stub-7 pop_icons"><div>

My0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> </span>

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 339,436,106 </span>

</div></td>
<td class="gt_row gt_left gt_striped" headers="North-America stub-7 gini_pct_change"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTIwLjEyMTY4NjIyMzM4MTEzcHgiIGhlaWdodD0iMTVweCIgZmlsbD0iIzk2M2Q0YyIgLz48dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSI5LjAiIGZpbGw9ImJsYWNrIiB4PSIxMTcuNzE5MjUyNDk4OTEzNXB4IiB5PSIxNS4wcHgiPjwvdGV4dD48bGluZSBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjMuMHB4IiB4MT0iMCIgeTE9IjAiIHgyPSIwIiB5Mj0iMzBweCI+PC9saW5lPjxsaW5lIHN0cm9rZT0iIzNEM0QzRCIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjEwMC41NDI1OTAxNzgxODM0cHgiIHkxPSIwIiB4Mj0iMTAwLjU0MjU5MDE3ODE4MzRweCIgeTI9IjMwcHgiPjwvbGluZT48L3N2Zz4=" />
</div></td>
</tr>
<tr>
<td id="stub-9" class="gt_row gt_left gt_stub" scope="row">Mexico</td>
<td class="gt_row gt_left" headers="North-America stub-9 Code"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iTWV4aWNvIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld2JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5O2hlaWdodDoxZW07d2lkdGg6MWVtOyI+PHRpdGxlPk1leGljbzwvdGl0bGU+PG1hc2sgaWQ9IkNvZGUtOC1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjQ29kZS04LWEpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTQ0IDBoMjIzbDMzIDI1Ni0zMyAyNTZIMTQ0bC0zMi0yNTZ6IiAvPjxwYXRoIGZpbGw9IiM0OTZlMmQiIGQ9Ik0wIDBoMTQ0djUxMkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzY4IDBoMTQ0djUxMkgzNjh6IiAvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Ik0yNTYgMjc3djEwaDEybDEwLTIyeiIgLz48cGF0aCBmaWxsPSIjNDk2ZTJkIiBkPSJNMTYwIDI0MmE5NiA5NiAwIDAgMCAxOTIgMGgtMTFhODUgODUgMCAwIDEtMTcwIDB6bTM5IDE3LTQgMmMtMiAyLTIgNiAxIDggMTUgMTQgMzQgMjIgNTQgMjR2MTdoMTJ2LTE3YzIwLTIgMzktMTAgNTQtMjQgMy0yIDMtNiAxLThzLTYtMi04IDBhNzggNzggMCAwIDEtNTMgMjFjLTE5IDAtMzgtOC01My0yMXoiIC8+PHBhdGggZmlsbD0iIzMzOGFmMyIgZD0iTTI1NiAzMTZjLTE0IDAtMjgtNS00MC0xM2w2LTljMjAgMTMgNDggMTMgNjggMGw3IDljLTEyIDgtMjYgMTMtNDEgMTN6IiAvPjxwYXRoIGZpbGw9IiM3NTFhNDYiIGQ9Ik0yNTYgMTc0YzIyIDExIDEyIDMzIDExIDM0bC0yLTRjLTUtMTEtMTgtMTgtMzEtMTh2MTFjNiAwIDExIDUgMTEgMTEtNyA3LTkgMTctNCAyNmw0IDgtMTMgMjMgMjktNyAxOCAxOHYtMTFsMTEgMTEgMjMtMTEtMzUtMjEtNS0yMSAyOCAxNmM0IDExIDEyIDIxIDIzIDI2IDktODMtNDItOTEtNjEtOTF6IiAvPjxwYXRoIGZpbGw9IiM2ZGE1NDQiIGQ9Ik0yMjIgMjcxYy0xNSAwLTMzLTEyLTM4LTQwbDExLTJjNCAyMyAxOCAzMSAyNyAzMSAzIDAgNS0xIDYtMyAwLTIgMC0zLTYtNS0zLTEtNy0yLTEwLTUtMTAtMTIgNC0yNCAxMS0zMCAxLTEgMi0yIDEtMyAwIDAtMi0yLTUtMi03IDAtMTItNC0xNC0xMS0yLTYgMi0xMyA4LTE3bDUgMTFjLTIgMC0yIDItMiA0IDAgMCAxIDIgMyAyIDcgMCAxNCA0IDE2IDkgMSAzIDIgOS01IDE1LTcgNy0xMSAxMi05IDE1bDUgMWM1IDIgMTQgNSAxMyAxNy0xIDgtOCAxMy0xNyAxM2gtMXoiIC8+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTIzNCAxODYtMTIgMTF2MTFsMTgtOWMzLTEgMy01IDEtN3oiIC8+PGNpcmNsZSBjeD0iMTcyIiBjeT0iMjc1IiByPSI4IiBmaWxsPSIjZmZkYTQ0Ij48L2NpcmNsZT48Y2lyY2xlIGN4PSIxODkiIGN5PSIzMDIiIHI9IjgiIGZpbGw9IiNmZmRhNDQiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjIxNiIgY3k9IjMyMyIgcj0iOCIgZmlsbD0iI2ZmZGE0NCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjk3IiBjeT0iMzIzIiByPSI4IiBmaWxsPSIjZmZkYTQ0Ij48L2NpcmNsZT48Y2lyY2xlIGN4PSIzMjQiIGN5PSIzMDIiIHI9IjgiIGZpbGw9IiNmZmRhNDQiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjM0MSIgY3k9IjI3NSIgcj0iOCIgZmlsbD0iI2ZmZGE0NCI+PC9jaXJjbGU+PHJlY3Qgd2lkdGg9IjM0IiBoZWlnaHQ9IjIyIiB4PSIyMzkiIHk9IjI5OSIgZmlsbD0iI2ZmOTgxMSIgcng9IjExIiByeT0iMTEiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left" headers="North-America stub-9 gini_market__age_total"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjEyMy42NDk2MzUwMzY0OTYzMiIgeT0iMTguNSIgd2lkdGg9IjEwLjk0ODkwNTEwOTQ4OTA3NSIgaGVpZ2h0PSIzLjAiIHJ4PSIyIiBmaWxsPSJncmV5IiAvPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSIxMzQuNTk4NTQwMTQ1OTg1NCIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiNlMGIxNjUiPjwvY2lyY2xlPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSIxMjMuNjQ5NjM1MDM2NDk2MzIiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIxMzQuNTk4NTQwMTQ1OTg1NCIgeT0iMTQuNDUiPjAuNDM8L3RleHQ+PHRleHQgZG9taW5hbnQtYmFzZWxpbmU9Imxvd2VyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzEwNmVhMCIgeD0iMTIzLjY0OTYzNTAzNjQ5NjMyIiB5PSIxNC40NSI+MC40MjwvdGV4dD48L3N2Zz4=" />
</div></td>
<td class="gt_row gt_left" headers="North-America stub-9 pop_icons"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 126,798,998 </span>

</div></td>
<td class="gt_row gt_left" headers="North-America stub-9 gini_pct_change"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTQuOTkzNDgxMDk1MTc2MDA4cHgiIGhlaWdodD0iMTVweCIgZmlsbD0iIzk2M2Q0YyIgLz48dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSI5LjAiIGZpbGw9ImJsYWNrIiB4PSIxNC42OTM2MTE0NzMyNzI0ODlweCIgeT0iMTUuMHB4Ij48L3RleHQ+PGxpbmUgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjMwcHgiPjwvbGluZT48bGluZSBzdHJva2U9IiMzRDNEM0QiIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSIxMy4wNTg4ODc0NDAyNDMzNzNweCIgeTE9IjAiIHgyPSIxMy4wNTg4ODc0NDAyNDMzNzNweCIgeTI9IjMwcHgiPjwvbGluZT48L3N2Zz4=" />
</div></td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" id="South-America" class="gt_group_heading" scope="colgroup">South America</td>
</tr>
<tr>
<td id="stub-10" class="gt_row gt_left gt_stub" scope="row">Brazil</td>
<td class="gt_row gt_left gt_striped" headers="South-America stub-10 Code"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iQnJhemlsIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld2JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5O2hlaWdodDoxZW07d2lkdGg6MWVtOyI+PHRpdGxlPkJyYXppbDwvdGl0bGU+PG1hc2sgaWQ9IkNvZGUtOS1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjQ29kZS05LWEpIj48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMCAwaDUxMnY1MTJIMHoiIC8+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0iTTI1NiAxMDAuMiA0NjcuNSAyNTYgMjU2IDQxMS44IDQ0LjUgMjU2eiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTc0LjIgMjIxYTg3IDg3IDAgMCAwLTcuMiAzNi4zbDE2MiA0OS44YTg4LjUgODguNSAwIDAgMCAxNC40LTM0Yy00MC42LTY1LjMtMTE5LjctODAuMy0xNjkuMS01MnoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTI1NS43IDE2N2E4OSA4OSAwIDAgMC00MS45IDEwLjYgODkgODkgMCAwIDAtMzkuNiA0My40IDE4MS43IDE4MS43IDAgMCAxIDE2OS4xIDUyLjIgODkgODkgMCAwIDAtOS01OS40IDg5IDg5IDAgMCAwLTc4LjYtNDYuOHpNMjEyIDI1MC41YTE0OSAxNDkgMCAwIDAtNDUgNi44IDg5IDg5IDAgMCAwIDEwLjUgNDAuOSA4OSA4OSAwIDAgMCAxMjAuNiAzNi4yIDg5IDg5IDAgMCAwIDMwLjctMjcuM0ExNTEgMTUxIDAgMCAwIDIxMiAyNTAuNXoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left gt_striped" headers="South-America stub-10 gini_market__age_total"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjE0NC4wODc1OTEyNDA4NzU5IiB5PSIxOC41IiB3aWR0aD0iNzUuOTEyNDA4NzU5MTI0MTMiIGhlaWdodD0iMy4wIiByeD0iMiIgZmlsbD0iZ3JleSIgLz48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iMjIwLjAwMDAwMDAwMDAwMDAzIiBjeT0iMjAuMCIgcj0iMy43NSIgZmlsbD0iI2UwYjE2NSI+PC9jaXJjbGU+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE0NC4wODc1OTEyNDA4NzU5IiBjeT0iMjAuMCIgcj0iMy43NSIgZmlsbD0iIzEwNmVhMCI+PC9jaXJjbGU+PHRleHQgZG9taW5hbnQtYmFzZWxpbmU9Imxvd2VyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iI2UwYjE2NSIgeD0iMjIwLjAwMDAwMDAwMDAwMDAzIiB5PSIxNC40NSI+MC41NTwvdGV4dD48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjMTA2ZWEwIiB4PSIxNDQuMDg3NTkxMjQwODc1OSIgeT0iMTQuNDUiPjAuNDU8L3RleHQ+PC9zdmc+" />
</div></td>
<td class="gt_row gt_left gt_striped" headers="South-America stub-10 pop_icons"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 208,660,785 </span>

</div></td>
<td class="gt_row gt_left gt_striped" headers="South-America stub-10 gini_pct_change"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iODEuODc3NDQ0NTg5MzA5cHgiIGhlaWdodD0iMTVweCIgZmlsbD0iIzk2M2Q0YyIgLz48dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSI5LjAiIGZpbGw9ImJsYWNrIiB4PSI4MC4yMzk4OTU2OTc1MjI4MXB4IiB5PSIxNS4wcHgiPjwvdGV4dD48bGluZSBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjMuMHB4IiB4MT0iMCIgeTE9IjAiIHgyPSIwIiB5Mj0iMzBweCI+PC9saW5lPjxsaW5lIHN0cm9rZT0iIzNEM0QzRCIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjUzLjA4NDk2MzA1OTUzOTMzcHgiIHkxPSIwIiB4Mj0iNTMuMDg0OTYzMDU5NTM5MzNweCIgeTI9IjMwcHgiPjwvbGluZT48L3N2Zz4=" />
</div></td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="5" class="gt_sourcenote" style="border-bottom: 1px hidden #000000"> 

<strong>Source:</strong> Data from [#TidyTuesday](https://github.com/rfordatascience/tidytuesday) (2025-08-05).<br />


<strong>Dumbbell plot:</strong> <span style="color:#106ea0;">Blue:</span> post-tax Gini coefficient <span style="color:#e0b165;">Gold:</span> pre-tax Gini coefficient<br />


<strong>Bullet plot:</strong> Percent reduction in Gini after taxes for each country, compared to its 5-year average benchmark.
</div></td>
</tr>
</tfoot>

</table>
