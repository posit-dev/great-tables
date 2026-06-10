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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_title gt_font_normal" style="color: #005689; font-size: 22px; font-weight: bold">Income Inequality Before and After Taxes in 2020</th>
</tr>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="color: #005689; font-size: 16px; font-weight: bold">As measured by the Gini coefficient, where 0 is best and 1 is worst</th>
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
<th colspan="5" class="gt_group_heading">Europe</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">France</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+RnJhbmNlPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTY3IDBoMTc4bDI1LjkgMjUyLjNMMzQ1IDUxMkgxNjdsLTI5LjgtMjUzLjR6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMTY3djUxMkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzQ1IDBoMTY3djUxMkgzNDV6IiAvPjwvZz48L3N2Zz4=" /></span></td>
<td class="gt_row gt_left"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjE5Ljk5OTk5OTk5OTk5OTk4NiIgeT0iMTguNSIgd2lkdGg9IjE3Mi45OTI3MDA3Mjk5MjcwNCIgaGVpZ2h0PSIzLjAiIHJ4PSIyIiBmaWxsPSJncmV5IiAvPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSIxOTIuOTkyNzAwNzI5OTI3IiBjeT0iMjAuMCIgcj0iMy43NSIgZmlsbD0iI2UwYjE2NSI+PC9jaXJjbGU+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE5Ljk5OTk5OTk5OTk5OTk4NiIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiMxMDZlYTAiPjwvY2lyY2xlPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiNlMGIxNjUiIHg9IjE5Mi45OTI3MDA3Mjk5MjciIHk9IjE0LjQ1Ij4wLjUyPC90ZXh0Pjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMxMDZlYTAiIHg9IjE5Ljk5OTk5OTk5OTk5OTk4NiIgeT0iMTQuNDUiPjAuMjg8L3RleHQ+PC9zdmc+" />
</div></td>
<td class="gt_row gt_left"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 65,905,226 </span>

</div></td>
<td class="gt_row gt_left"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMjAwLjBweCIgaGVpZ2h0PSIxNXB4IiBmaWxsPSIjOTYzZDRjIiAvPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjkuMCIgZmlsbD0iYmxhY2siIHg9IjE5Ni4wcHgiIHk9IjE1LjBweCI+PC90ZXh0PjxsaW5lIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIzMHB4Ij48L2xpbmU+PC9zdmc+" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Germany</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+R2VybWFueTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTAgMzQ1IDI1Ni43LTI1LjVMNTEyIDM0NXYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0ibTAgMTY3IDI1NS0yMyAyNTcgMjN2MTc4SDB6IiAvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Ik0wIDBoNTEydjE2N0gweiIgLz48L2c+PC9zdmc+" /></span></td>
<td class="gt_row gt_left gt_striped"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjM4LjI0ODE3NTE4MjQ4MTcxIiB5PSIxOC41IiB3aWR0aD0iMTQwLjg3NTkxMjQwODc1OTE1IiBoZWlnaHQ9IjMuMCIgcng9IjIiIGZpbGw9ImdyZXkiIC8+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE3OS4xMjQwODc1OTEyNDA4NSIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiNlMGIxNjUiPjwvY2lyY2xlPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSIzOC4yNDgxNzUxODI0ODE3MSIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiMxMDZlYTAiPjwvY2lyY2xlPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiNlMGIxNjUiIHg9IjE3OS4xMjQwODc1OTEyNDA4NSIgeT0iMTQuNDUiPjAuNTwvdGV4dD48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjMTA2ZWEwIiB4PSIzOC4yNDgxNzUxODI0ODE3MSIgeT0iMTQuNDUiPjAuMzwvdGV4dD48L3N2Zz4=" />
</div></td>
<td class="gt_row gt_left gt_striped"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 83,628,661 </span>

</div></td>
<td class="gt_row gt_left gt_striped"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTY5LjEwMDM5MTEzNDI4OTRweCIgaGVpZ2h0PSIxNXB4IiBmaWxsPSIjOTYzZDRjIiAvPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjkuMCIgZmlsbD0iYmxhY2siIHg9IjE2NS43MTgzODMzMTE2MDM2MnB4IiB5PSIxNS4wcHgiPjwvdGV4dD48bGluZSBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjMuMHB4IiB4MT0iMCIgeTE9IjAiIHgyPSIwIiB5Mj0iMzBweCI+PC9saW5lPjxsaW5lIHN0cm9rZT0iIzNEM0QzRCIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjE3Ni41MzU2MzY2Nzk3MDQ0OHB4IiB5MT0iMCIgeDI9IjE3Ni41MzU2MzY2Nzk3MDQ0OHB4IiB5Mj0iMzBweCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Spain</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U3BhaW48L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Im0wIDEyOCAyNTYtMzIgMjU2IDMydjI1NmwtMjU2IDMyTDAgMzg0WiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMCAwaDUxMnYxMjhIMHptMCAzODRoNTEydjEyOEgweiIgLz48ZyBmaWxsPSIjZWVlIj48cGF0aCBkPSJNMTQ0IDMwNGgtMTZ2LTgwaDE2em0xMjggMGgxNnYtODBoLTE2eiIgLz48ZWxsaXBzZSBjeD0iMjA4IiBjeT0iMjk2IiByeD0iNDgiIHJ5PSIzMiI+PC9lbGxpcHNlPjwvZz48ZyBmaWxsPSIjZDgwMDI3Ij48cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMjQiIHg9IjEyOCIgeT0iMTkyIiByeD0iOCIgLz48cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMjQiIHg9IjI3MiIgeT0iMTkyIiByeD0iOCIgLz48cGF0aCBkPSJNMjA4IDI3MnYyNGEyNCAyNCAwIDAgMCAyNCAyNCAyNCAyNCAwIDAgMCAyNC0yNHYtMjRoLTI0eiIgLz48L2c+PHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjE2IiB4PSIxMjAiIHk9IjIwOCIgZmlsbD0iI2ZmOTgxMSIgcnk9IjgiIC8+PHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjE2IiB4PSIyNjQiIHk9IjIwOCIgZmlsbD0iI2ZmOTgxMSIgcnk9IjgiIC8+PHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjE2IiB4PSIxMjAiIHk9IjMwNCIgZmlsbD0iI2ZmOTgxMSIgcng9IjgiIC8+PHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjE2IiB4PSIyNjQiIHk9IjMwNCIgZmlsbD0iI2ZmOTgxMSIgcng9IjgiIC8+PHBhdGggZmlsbD0iI2ZmOTgxMSIgZD0iTTE2MCAyNzJ2MjRjMCA4IDQgMTQgOSAxOWw1LTYgNSAxMGEyMSAyMSAwIDAgMCAxMCAwbDUtMTAgNSA2YzYtNSA5LTExIDktMTl2LTI0aC05bC01IDgtNS04aC0xMGwtNSA4LTUtOHoiIC8+PHBhdGggZD0iTTEyMiAyNTJoMTcybS0xNzIgMjRoMjhtMTE2IDBoMjgiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTEyMiAyNDhhNCA0IDAgMCAwLTQgNCA0IDQgMCAwIDAgNCA0aDE3MmE0IDQgMCAwIDAgNC00IDQgNCAwIDAgMC00LTR6bTAgMjRhNCA0IDAgMCAwLTQgNCA0IDQgMCAwIDAgNCA0aDI4YTQgNCAwIDAgMCA0LTQgNCA0IDAgMCAwLTQtNHptMTQ0IDBhNCA0IDAgMCAwLTQgNCA0IDQgMCAwIDAgNCA0aDI4YTQgNCAwIDAgMCA0LTQgNCA0IDAgMCAwLTQtNHoiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTE5NiAxNjhjLTcgMC0xMyA1LTE1IDExbC01LTFjLTkgMC0xNiA3LTE2IDE2czcgMTYgMTYgMTZjNyAwIDEzLTQgMTUtMTFhMTYgMTYgMCAwIDAgMTctNCAxNiAxNiAwIDAgMCAxNyA0IDE2IDE2IDAgMSAwIDEwLTIwIDE2IDE2IDAgMCAwLTI3LTVjLTMtNC03LTYtMTItNnptMCA4YzUgMCA4IDQgOCA4IDAgNS0zIDgtOCA4LTQgMC04LTMtOC04IDAtNCA0LTggOC04em0yNCAwYzUgMCA4IDQgOCA4IDAgNS0zIDgtOCA4LTQgMC04LTMtOC04IDAtNCA0LTggOC04em0tNDQgMTAgNCAxIDQgOGMwIDQtNCA3LTggN3MtOC0zLTgtOGMwLTQgNC04IDgtOHptNjQgMGM1IDAgOCA0IDggOCAwIDUtMyA4LTggOC00IDAtOC0zLTgtN2w0LTh6IiAvPjxwYXRoIGZpbGw9Im5vbmUiIGQ9Ik0yMjAgMjg0djEyYzAgNyA1IDEyIDEyIDEyczEyLTUgMTItMTJ2LTEyeiIgLz48cGF0aCBmaWxsPSIjZmY5ODExIiBkPSJNMjAwIDE2MGgxNnYzMmgtMTZ6IiAvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0yMDggMjI0aDQ4djQ4aC00OHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0ibTI0OCAyMDgtOCA4aC02NGwtOC04YzAtMTMgMTgtMjQgNDAtMjRzNDAgMTEgNDAgMjR6bS04OCAxNmg0OHY0OGgtNDh6IiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIzMiIgeD0iMjIyIiB5PSIyMzIiIGZpbGw9IiNkODAwMjciIHJ4PSIxMCIgcnk9IjEwIiAvPjxwYXRoIGZpbGw9IiNmZjk4MTEiIGQ9Ik0xNjggMjMydjhoOHYxNmgtOHY4aDMydi04aC04di0xNmg4di04em04LTE2aDY0djhoLTY0eiIgLz48ZyBmaWxsPSIjZmZkYTQ0Ij48Y2lyY2xlIGN4PSIxODYiIGN5PSIyMDIiIHI9IjYiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjIwOCIgY3k9IjIwMiIgcj0iNiI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjMwIiBjeT0iMjAyIiByPSI2Ij48L2NpcmNsZT48L2c+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTE2OSAyNzJ2NDNhMjQgMjQgMCAwIDAgMTAgNHYtNDdoLTEwem0yMCAwdjQ3YTI0IDI0IDAgMCAwIDEwLTR2LTQzaC0xMHoiIC8+PGcgZmlsbD0iIzMzOGFmMyI+PGNpcmNsZSBjeD0iMjA4IiBjeT0iMjcyIiByPSIxNiI+PC9jaXJjbGU+PHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjE2IiB4PSIyNjQiIHk9IjMyMCIgcnk9IjgiIC8+PHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjE2IiB4PSIxMjAiIHk9IjMyMCIgcnk9IjgiIC8+PC9nPjwvZz48L3N2Zz4=" /></span></td>
<td class="gt_row gt_left"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjU3LjIyNjI3NzM3MjI2Mjc2IiB5PSIxOC41IiB3aWR0aD0iMTM1Ljc2NjQyMzM1NzY2NDI1IiBoZWlnaHQ9IjMuMCIgcng9IjIiIGZpbGw9ImdyZXkiIC8+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE5Mi45OTI3MDA3Mjk5MjciIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjZTBiMTY1Ij48L2NpcmNsZT48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iNTcuMjI2Mjc3MzcyMjYyNzYiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIxOTIuOTkyNzAwNzI5OTI3IiB5PSIxNC40NSI+MC41MjwvdGV4dD48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjMTA2ZWEwIiB4PSI1Ny4yMjYyNzczNzIyNjI3NiIgeT0iMTQuNDUiPjAuMzM8L3RleHQ+PC9zdmc+" />
</div></td>
<td class="gt_row gt_left"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 47,679,437 </span>

</div></td>
<td class="gt_row gt_left"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTU2Ljk3NTIyODE2MTY2ODhweCIgaGVpZ2h0PSIxNXB4IiBmaWxsPSIjOTYzZDRjIiAvPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjkuMCIgZmlsbD0iYmxhY2siIHg9IjE1My44MzU3MjM1OTg0MzU0NHB4IiB5PSIxNS4wcHgiPjwvdGV4dD48bGluZSBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjMuMHB4IiB4MT0iMCIgeTE9IjAiIHgyPSIwIiB5Mj0iMzBweCI+PC9saW5lPjxsaW5lIHN0cm9rZT0iIzNEM0QzRCIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjE0OS43MDM4MjQ0MjQxNjMzN3B4IiB5MT0iMCIgeDI9IjE0OS43MDM4MjQ0MjQxNjMzN3B4IiB5Mj0iMzBweCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Italy</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+SXRhbHk8L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0xNjcgMGgxNzhsMjUuOSAyNTIuM0wzNDUgNTEySDE2N2wtMjkuOC0yNTMuNHoiIC8+PHBhdGggZmlsbD0iIzZkYTU0NCIgZD0iTTAgMGgxNjd2NTEySDB6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0zNDUgMGgxNjd2NTEySDM0NXoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left gt_striped"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjU4LjY4NjEzMTM4Njg2MTMiIHk9IjE4LjUiIHdpZHRoPSIxNDMuMDY1NjkzNDMwNjU2OTUiIGhlaWdodD0iMy4wIiByeD0iMiIgZmlsbD0iZ3JleSIgLz48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iMjAxLjc1MTgyNDgxNzUxODI0IiBjeT0iMjAuMCIgcj0iMy43NSIgZmlsbD0iI2UwYjE2NSI+PC9jaXJjbGU+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjU4LjY4NjEzMTM4Njg2MTMiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIyMDEuNzUxODI0ODE3NTE4MjQiIHk9IjE0LjQ1Ij4wLjUzPC90ZXh0Pjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMxMDZlYTAiIHg9IjU4LjY4NjEzMTM4Njg2MTMiIHk9IjE0LjQ1Ij4wLjMzPC90ZXh0Pjwvc3ZnPg==" />
</div></td>
<td class="gt_row gt_left gt_striped"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 59,912,714 </span>

</div></td>
<td class="gt_row gt_left gt_striped"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTYxLjYyNTM4MDI2OTQ0ODA0cHgiIGhlaWdodD0iMTVweCIgZmlsbD0iIzk2M2Q0YyIgLz48dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSI5LjAiIGZpbGw9ImJsYWNrIiB4PSIxNTguMzkyODcyNjY0MDU5MDdweCIgeT0iMTUuMHB4Ij48L3RleHQ+PGxpbmUgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjMwcHgiPjwvbGluZT48bGluZSBzdHJva2U9IiMzRDNEM0QiIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSIxNTUuMzAxMzkwNjk5Njk1OHB4IiB5MT0iMCIgeDI9IjE1NS4zMDEzOTA2OTk2OTU4cHgiIHkyPSIzMHB4Ij48L2xpbmU+PC9zdmc+" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">United Kingdom</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+VW5pdGVkIEtpbmdkb208L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Im0wIDAgOCAyMi04IDIzdjIzbDMyIDU0LTMyIDU0djMybDMyIDQ4LTMyIDQ4djMybDMyIDU0LTMyIDU0djY4bDIyLTggMjMgOGgyM2w1NC0zMiA1NCAzMmgzMmw0OC0zMiA0OCAzMmgzMmw1NC0zMiA1NCAzMmg2OGwtOC0yMiA4LTIzdi0yM2wtMzItNTQgMzItNTR2LTMybC0zMi00OCAzMi00OHYtMzJsLTMyLTU0IDMyLTU0VjBsLTIyIDgtMjMtOGgtMjNsLTU0IDMyLTU0LTMyaC0zMmwtNDggMzItNDgtMzJoLTMybC01NCAzMkw2OCAwSDB6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0zMzYgMHYxMDhMNDQ0IDBabTE3NiA2OEw0MDQgMTc2aDEwOHpNMCAxNzZoMTA4TDAgNjhaTTY4IDBsMTA4IDEwOFYwWm0xMDggNTEyVjQwNEw2OCA1MTJaTTAgNDQ0bDEwOC0xMDhIMFptNTEyLTEwOEg0MDRsMTA4IDEwOFptLTY4IDE3NkwzMzYgNDA0djEwOHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMHY0NWwxMzEgMTMxaDQ1TDAgMHptMjA4IDB2MjA4SDB2OTZoMjA4djIwOGg5NlYzMDRoMjA4di05NkgzMDRWMGgtOTZ6bTI1OSAwTDMzNiAxMzF2NDVMNTEyIDBoLTQ1ek0xNzYgMzM2IDAgNTEyaDQ1bDEzMS0xMzF2LTQ1em0xNjAgMCAxNzYgMTc2di00NUwzODEgMzM2aC00NXoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9Ijc2LjIwNDM3OTU2MjA0Mzc1IiB5PSIxOC41IiB3aWR0aD0iMTEwLjk0ODkwNTEwOTQ4OTA2IiBoZWlnaHQ9IjMuMCIgcng9IjIiIGZpbGw9ImdyZXkiIC8+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE4Ny4xNTMyODQ2NzE1MzI4MiIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiNlMGIxNjUiPjwvY2lyY2xlPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSI3Ni4yMDQzNzk1NjIwNDM3NSIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiMxMDZlYTAiPjwvY2lyY2xlPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiNlMGIxNjUiIHg9IjE4Ny4xNTMyODQ2NzE1MzI4MiIgeT0iMTQuNDUiPjAuNTE8L3RleHQ+PHRleHQgZG9taW5hbnQtYmFzZWxpbmU9Imxvd2VyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzEwNmVhMCIgeD0iNzYuMjA0Mzc5NTYyMDQzNzUiIHk9IjE0LjQ1Ij4wLjM1PC90ZXh0Pjwvc3ZnPg==" />
</div></td>
<td class="gt_row gt_left"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 67,351,806 </span>

</div></td>
<td class="gt_row gt_left"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTMwLjI5MTE3Nzc0ODgwNDg0cHgiIGhlaWdodD0iMTVweCIgZmlsbD0iIzk2M2Q0YyIgLz48dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSI5LjAiIGZpbGw9ImJsYWNrIiB4PSIxMjcuNjg1MzU0MTkzODI4NzRweCIgeT0iMTUuMHB4Ij48L3RleHQ+PGxpbmUgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjMwcHgiPjwvbGluZT48bGluZSBzdHJva2U9IiMzRDNEM0QiIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSIxMjUuOTc1MDEwODY0ODQxMzdweCIgeTE9IjAiIHgyPSIxMjUuOTc1MDEwODY0ODQxMzdweCIgeTI9IjMwcHgiPjwvbGluZT48L3N2Zz4=" />
</div></td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">Asia</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">South Korea</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+S29yZWEsIFJlcC48L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDBoNTEydjUxMkgwWiIgLz48cGF0aCBmaWxsPSIjMzMzIiBkPSJtMzUwIDMzNSAyNC0yNCAxNiAxNi0yNCAyM3ptLTM5IDM5IDI0LTI0IDE1IDE2LTIzIDI0em04NyA4IDIzLTI0IDE2IDE2LTI0IDI0em0tNDAgMzkgMjQtMjMgMTYgMTUtMjQgMjRabTE2LTYzIDI0LTIzIDE1IDE1LTIzIDI0em0tMzkgNDAgMjMtMjQgMTYgMTYtMjQgMjN6bTYzLTIyMS02My02MyAxNS0xNSA2NCA2M3ptLTYzLTE1LTI0LTI0IDE2LTE2IDIzIDI0em0zOSAzOS0yNC0yNCAxNi0xNSAyNCAyM3ptOC04Ny0yNC0yMyAxNi0xNiAyNCAyNFptMzkgNDAtMjMtMjQgMTUtMTYgMjQgMjRaTTkxIDM1OGw2MyA2My0xNiAxNi02My02M3ptNjMgMTYgMjMgMjQtMTUgMTUtMjQtMjN6bS00MC0zOSAyNCAyMy0xNiAxNi0yMy0yNHptMjQtMjQgNjMgNjMtMTYgMTYtNjMtNjN6bTE2LTIyMC02MyA2My0xNi0xNiA2My02M3ptMjMgMjMtNjMgNjMtMTUtMTYgNjMtNjN6bTI0IDI0LTYzIDYzLTE2LTE2IDYzLTYzeiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzE5IDMxOSAxOTMgMTkzYTg5IDg5IDAgMSAxIDEyNiAxMjZ6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0zMTkgMzE5YTg5IDg5IDAgMSAxLTEyNi0xMjZ6IiAvPjxjaXJjbGUgY3g9IjIyNC41IiBjeT0iMjI0LjUiIHI9IjQ0LjUiIGZpbGw9IiNkODAwMjciPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjI4Ny41IiBjeT0iMjg3LjUiIHI9IjQ0LjUiIGZpbGw9IiMwMDUyYjQiPjwvY2lyY2xlPjwvZz48L3N2Zz4=" /></span></td>
<td class="gt_row gt_left gt_striped"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjU2LjQ5NjM1MDM2NDk2MzQ4IiB5PSIxOC41IiB3aWR0aD0iNTYuMjA0Mzc5NTYyMDQzODIiIGhlaWdodD0iMy4wIiByeD0iMiIgZmlsbD0iZ3JleSIgLz48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iMTEyLjcwMDcyOTkyNzAwNzMiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjZTBiMTY1Ij48L2NpcmNsZT48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iNTYuNDk2MzUwMzY0OTYzNDgiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIxMTIuNzAwNzI5OTI3MDA3MyIgeT0iMTQuNDUiPjAuNDE8L3RleHQ+PHRleHQgZG9taW5hbnQtYmFzZWxpbmU9Imxvd2VyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzEwNmVhMCIgeD0iNTYuNDk2MzUwMzY0OTYzNDgiIHk9IjE0LjQ1Ij4wLjMzPC90ZXh0Pjwvc3ZnPg==" />
</div></td>
<td class="gt_row gt_left gt_striped"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 51,858,440 </span>

</div></td>
<td class="gt_row gt_left gt_striped"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iODIuNjE2MjUzODAyNjk0NDlweCIgaGVpZ2h0PSIxNXB4IiBmaWxsPSIjOTYzZDRjIiAvPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjkuMCIgZmlsbD0iYmxhY2siIHg9IjgwLjk2MzkyODcyNjY0MDZweCIgeT0iMTUuMHB4Ij48L3RleHQ+PGxpbmUgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjMwcHgiPjwvbGluZT48bGluZSBzdHJva2U9IiMzRDNEM0QiIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSI2Mi42Mjg2Mzk3MjE4NjAwNTRweCIgeTE9IjAiIHgyPSI2Mi42Mjg2Mzk3MjE4NjAwNTRweCIgeTI9IjMwcHgiPjwvbGluZT48L3N2Zz4=" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Turkey</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+VHVya2l5ZTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2NTEySDB6IiAvPjxnIGZpbGw9IiNlZWUiPjxwYXRoIGQ9Im0yNDUuNSAyMDkuMiAyMSAyOSAzNC0xMS4xLTIxIDI5IDIxIDI4LjktMzQtMTEuMS0yMSAyOVYyNjdsLTM0LTExLjEgMzQtMTF6IiAvPjxwYXRoIGQ9Ik0xODguMiAzMjguM2E3Mi4zIDcyLjMgMCAxIDEgMzQuNC0xMzYgODkgODkgMCAxIDAgMCAxMjcuMyA3MiA3MiAwIDAgMS0zNC40IDguN3oiIC8+PC9nPjwvZz48L3N2Zz4=" /></span></td>
<td class="gt_row gt_left"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjExMS4yNDA4NzU5MTI0MDg3NSIgeT0iMTguNSIgd2lkdGg9IjczLjcyMjYyNzczNzIyNjI2IiBoZWlnaHQ9IjMuMCIgcng9IjIiIGZpbGw9ImdyZXkiIC8+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE4NC45NjM1MDM2NDk2MzUwMiIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiNlMGIxNjUiPjwvY2lyY2xlPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSIxMTEuMjQwODc1OTEyNDA4NzUiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIxODQuOTYzNTAzNjQ5NjM1MDIiIHk9IjE0LjQ1Ij4wLjU8L3RleHQ+PHRleHQgZG9taW5hbnQtYmFzZWxpbmU9Imxvd2VyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzEwNmVhMCIgeD0iMTExLjI0MDg3NTkxMjQwODc1IiB5PSIxNC40NSI+MC40PC90ZXh0Pjwvc3ZnPg==" />
</div></td>
<td class="gt_row gt_left"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 86,091,644 </span>

</div></td>
<td class="gt_row gt_left"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iODcuMDkyNTY4NDQ4NTAwNjRweCIgaGVpZ2h0PSIxNXB4IiBmaWxsPSIjOTYzZDRjIiAvPjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjkuMCIgZmlsbD0iYmxhY2siIHg9Ijg1LjM1MDcxNzA3OTUzMDYzcHgiIHk9IjE1LjBweCI+PC90ZXh0PjxsaW5lIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIzMHB4Ij48L2xpbmU+PGxpbmUgc3Ryb2tlPSIjM0QzRDNEIiBzdHJva2Utd2lkdGg9IjMuMHB4IiB4MT0iNjguOTM4OTM5NTkxNDgxOTVweCIgeTE9IjAiIHgyPSI2OC45Mzg5Mzk1OTE0ODE5NXB4IiB5Mj0iMzBweCI+PC9saW5lPjwvc3ZnPg==" />
</div></td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">North America</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">United States</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+VW5pdGVkIFN0YXRlczwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTI1NiAwaDI1NnY2NGwtMzIgMzIgMzIgMzJ2NjRsLTMyIDMyIDMyIDMydjY0bC0zMiAzMiAzMiAzMnY2NGwtMjU2IDMyTDAgNDQ4di02NGwzMi0zMi0zMi0zMnYtNjR6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0yMjQgNjRoMjg4djY0SDIyNFptMCAxMjhoMjg4djY0SDI1NlpNMCAzMjBoNTEydjY0SDBabTAgMTI4aDUxMnY2NEgwWiIgLz48cGF0aCBmaWxsPSIjMDA1MmI0IiBkPSJNMCAwaDI1NnYyNTZIMFoiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0ibTE4NyAyNDMgNTctNDFoLTcwbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUg5M2w1NyA0MS0yMi02N3ptLTgxIDAgNTctNDFIMTJsNTcgNDEtMjItNjd6bTE2Mi04MSA1Ny00MWgtNzBsNTcgNDEtMjItNjd6bS04MSAwIDU3LTQxSDkzbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUgxMmw1NyA0MS0yMi02N1ptMTYyLTgyIDU3LTQxaC03MGw1NyA0MS0yMi02N1ptLTgxIDAgNTctNDFIOTNsNTcgNDEtMjItNjd6bS04MSAwIDU3LTQxSDEybDU3IDQxLTIyLTY3WiIgLz48L2c+PC9zdmc+" /></span></td>
<td class="gt_row gt_left gt_striped"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjkyLjI2Mjc3MzcyMjYyNzciIHk9IjE4LjUiIHdpZHRoPSIxMDUuMTA5NDg5MDUxMDk0OTQiIGhlaWdodD0iMy4wIiByeD0iMiIgZmlsbD0iZ3JleSIgLz48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iMTk3LjM3MjI2Mjc3MzcyMjY0IiBjeT0iMjAuMCIgcj0iMy43NSIgZmlsbD0iI2UwYjE2NSI+PC9jaXJjbGU+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjkyLjI2Mjc3MzcyMjYyNzciIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIxOTcuMzcyMjYyNzczNzIyNjQiIHk9IjE0LjQ1Ij4wLjUyPC90ZXh0Pjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJsb3dlciIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMxMDZlYTAiIHg9IjkyLjI2Mjc3MzcyMjYyNzciIHk9IjE0LjQ1Ij4wLjM4PC90ZXh0Pjwvc3ZnPg==" />
</div></td>
<td class="gt_row gt_left gt_striped"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 339,436,106 </span>

</div></td>
<td class="gt_row gt_left gt_striped"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTIwLjEyMTY4NjIyMzM4MTEzcHgiIGhlaWdodD0iMTVweCIgZmlsbD0iIzk2M2Q0YyIgLz48dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSI5LjAiIGZpbGw9ImJsYWNrIiB4PSIxMTcuNzE5MjUyNDk4OTEzNXB4IiB5PSIxNS4wcHgiPjwvdGV4dD48bGluZSBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjMuMHB4IiB4MT0iMCIgeTE9IjAiIHgyPSIwIiB5Mj0iMzBweCI+PC9saW5lPjxsaW5lIHN0cm9rZT0iIzNEM0QzRCIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjEwMC41NDI1OTAxNzgxODM0cHgiIHkxPSIwIiB4Mj0iMTAwLjU0MjU5MDE3ODE4MzRweCIgeTI9IjMwcHgiPjwvbGluZT48L3N2Zz4=" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Mexico</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+TWV4aWNvPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTQ0IDBoMjIzbDMzIDI1Ni0zMyAyNTZIMTQ0bC0zMi0yNTZ6IiAvPjxwYXRoIGZpbGw9IiM0OTZlMmQiIGQ9Ik0wIDBoMTQ0djUxMkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzY4IDBoMTQ0djUxMkgzNjh6IiAvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Ik0yNTYgMjc3djEwaDEybDEwLTIyeiIgLz48cGF0aCBmaWxsPSIjNDk2ZTJkIiBkPSJNMTYwIDI0MmE5NiA5NiAwIDAgMCAxOTIgMGgtMTFhODUgODUgMCAwIDEtMTcwIDB6bTM5IDE3LTQgMmMtMiAyLTIgNiAxIDggMTUgMTQgMzQgMjIgNTQgMjR2MTdoMTJ2LTE3YzIwLTIgMzktMTAgNTQtMjQgMy0yIDMtNiAxLThzLTYtMi04IDBhNzggNzggMCAwIDEtNTMgMjFjLTE5IDAtMzgtOC01My0yMXoiIC8+PHBhdGggZmlsbD0iIzMzOGFmMyIgZD0iTTI1NiAzMTZjLTE0IDAtMjgtNS00MC0xM2w2LTljMjAgMTMgNDggMTMgNjggMGw3IDljLTEyIDgtMjYgMTMtNDEgMTN6IiAvPjxwYXRoIGZpbGw9IiM3NTFhNDYiIGQ9Ik0yNTYgMTc0YzIyIDExIDEyIDMzIDExIDM0bC0yLTRjLTUtMTEtMTgtMTgtMzEtMTh2MTFjNiAwIDExIDUgMTEgMTEtNyA3LTkgMTctNCAyNmw0IDgtMTMgMjMgMjktNyAxOCAxOHYtMTFsMTEgMTEgMjMtMTEtMzUtMjEtNS0yMSAyOCAxNmM0IDExIDEyIDIxIDIzIDI2IDktODMtNDItOTEtNjEtOTF6IiAvPjxwYXRoIGZpbGw9IiM2ZGE1NDQiIGQ9Ik0yMjIgMjcxYy0xNSAwLTMzLTEyLTM4LTQwbDExLTJjNCAyMyAxOCAzMSAyNyAzMSAzIDAgNS0xIDYtMyAwLTIgMC0zLTYtNS0zLTEtNy0yLTEwLTUtMTAtMTIgNC0yNCAxMS0zMCAxLTEgMi0yIDEtMyAwIDAtMi0yLTUtMi03IDAtMTItNC0xNC0xMS0yLTYgMi0xMyA4LTE3bDUgMTFjLTIgMC0yIDItMiA0IDAgMCAxIDIgMyAyIDcgMCAxNCA0IDE2IDkgMSAzIDIgOS01IDE1LTcgNy0xMSAxMi05IDE1bDUgMWM1IDIgMTQgNSAxMyAxNy0xIDgtOCAxMy0xNyAxM2gtMXoiIC8+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTIzNCAxODYtMTIgMTF2MTFsMTgtOWMzLTEgMy01IDEtN3oiIC8+PGNpcmNsZSBjeD0iMTcyIiBjeT0iMjc1IiByPSI4IiBmaWxsPSIjZmZkYTQ0Ij48L2NpcmNsZT48Y2lyY2xlIGN4PSIxODkiIGN5PSIzMDIiIHI9IjgiIGZpbGw9IiNmZmRhNDQiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjIxNiIgY3k9IjMyMyIgcj0iOCIgZmlsbD0iI2ZmZGE0NCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMjk3IiBjeT0iMzIzIiByPSI4IiBmaWxsPSIjZmZkYTQ0Ij48L2NpcmNsZT48Y2lyY2xlIGN4PSIzMjQiIGN5PSIzMDIiIHI9IjgiIGZpbGw9IiNmZmRhNDQiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjM0MSIgY3k9IjI3NSIgcj0iOCIgZmlsbD0iI2ZmZGE0NCI+PC9jaXJjbGU+PHJlY3Qgd2lkdGg9IjM0IiBoZWlnaHQ9IjIyIiB4PSIyMzkiIHk9IjI5OSIgZmlsbD0iI2ZmOTgxMSIgcng9IjExIiByeT0iMTEiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjEyMy42NDk2MzUwMzY0OTYzMiIgeT0iMTguNSIgd2lkdGg9IjEwLjk0ODkwNTEwOTQ4OTA3NSIgaGVpZ2h0PSIzLjAiIHJ4PSIyIiBmaWxsPSJncmV5IiAvPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSIxMzQuNTk4NTQwMTQ1OTg1NCIgY3k9IjIwLjAiIHI9IjMuNzUiIGZpbGw9IiNlMGIxNjUiPjwvY2lyY2xlPjxjaXJjbGUgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGN4PSIxMjMuNjQ5NjM1MDM2NDk2MzIiIGN5PSIyMC4wIiByPSIzLjc1IiBmaWxsPSIjMTA2ZWEwIj48L2NpcmNsZT48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjZTBiMTY1IiB4PSIxMzQuNTk4NTQwMTQ1OTg1NCIgeT0iMTQuNDUiPjAuNDM8L3RleHQ+PHRleHQgZG9taW5hbnQtYmFzZWxpbmU9Imxvd2VyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzEwNmVhMCIgeD0iMTIzLjY0OTYzNTAzNjQ5NjMyIiB5PSIxNC40NSI+MC40MjwvdGV4dD48L3N2Zz4=" />
</div></td>
<td class="gt_row gt_left"><div>

 <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> 

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 126,798,998 </span>

</div></td>
<td class="gt_row gt_left"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjAiIHk9IjcuNXB4IiB3aWR0aD0iMTQuOTkzNDgxMDk1MTc2MDA4cHgiIGhlaWdodD0iMTVweCIgZmlsbD0iIzk2M2Q0YyIgLz48dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSI5LjAiIGZpbGw9ImJsYWNrIiB4PSIxNC42OTM2MTE0NzMyNzI0ODlweCIgeT0iMTUuMHB4Ij48L3RleHQ+PGxpbmUgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzLjBweCIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjMwcHgiPjwvbGluZT48bGluZSBzdHJva2U9IiMzRDNEM0QiIHN0cm9rZS13aWR0aD0iMy4wcHgiIHgxPSIxMy4wNTg4ODc0NDAyNDMzNzNweCIgeTE9IjAiIHgyPSIxMy4wNTg4ODc0NDAyNDMzNzNweCIgeTI9IjMwcHgiPjwvbGluZT48L3N2Zz4=" />
</div></td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading">South America</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Brazil</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+QnJhemlsPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMCAwaDUxMnY1MTJIMHoiIC8+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0iTTI1NiAxMDAuMiA0NjcuNSAyNTYgMjU2IDQxMS44IDQ0LjUgMjU2eiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTc0LjIgMjIxYTg3IDg3IDAgMCAwLTcuMiAzNi4zbDE2MiA0OS44YTg4LjUgODguNSAwIDAgMCAxNC40LTM0Yy00MC42LTY1LjMtMTE5LjctODAuMy0xNjkuMS01MnoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTI1NS43IDE2N2E4OSA4OSAwIDAgMC00MS45IDEwLjYgODkgODkgMCAwIDAtMzkuNiA0My40IDE4MS43IDE4MS43IDAgMCAxIDE2OS4xIDUyLjIgODkgODkgMCAwIDAtOS01OS40IDg5IDg5IDAgMCAwLTc4LjYtNDYuOHpNMjEyIDI1MC41YTE0OSAxNDkgMCAwIDAtNDUgNi44IDg5IDg5IDAgMCAwIDEwLjUgNDAuOSA4OSA4OSAwIDAgMCAxMjAuNiAzNi4yIDg5IDg5IDAgMCAwIDMwLjctMjcuM0ExNTEgMTUxIDAgMCAwIDIxMiAyNTAuNXoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left gt_striped"><div style="display: flex;">
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDAiIGhlaWdodD0iMzAiPjxyZWN0IHg9IjE0NC4wODc1OTEyNDA4NzU5IiB5PSIxOC41IiB3aWR0aD0iNzUuOTEyNDA4NzU5MTI0MTMiIGhlaWdodD0iMy4wIiByeD0iMiIgZmlsbD0iZ3JleSIgLz48Y2lyY2xlIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMS41IiBjeD0iMjIwLjAwMDAwMDAwMDAwMDAzIiBjeT0iMjAuMCIgcj0iMy43NSIgZmlsbD0iI2UwYjE2NSI+PC9jaXJjbGU+PGNpcmNsZSBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEuNSIgY3g9IjE0NC4wODc1OTEyNDA4NzU5IiBjeT0iMjAuMCIgcj0iMy43NSIgZmlsbD0iIzEwNmVhMCI+PC9jaXJjbGU+PHRleHQgZG9taW5hbnQtYmFzZWxpbmU9Imxvd2VyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iI2UwYjE2NSIgeD0iMjIwLjAwMDAwMDAwMDAwMDAzIiB5PSIxNC40NSI+MC41NTwvdGV4dD48dGV4dCBkb21pbmFudC1iYXNlbGluZT0ibG93ZXIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjMTA2ZWEwIiB4PSIxNDQuMDg3NTkxMjQwODc1OSIgeT0iMTQuNDUiPjAuNDU8L3RleHQ+PC9zdmc+" />
</div></td>
<td class="gt_row gt_left gt_striped"><div>

0OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzIwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpibGFjaztmaWxsLW9wYWNpdHk6MTtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC42MmVtO21hcmdpbi1sZWZ0OmF1dG87bWFyZ2luLXJpZ2h0OjAuMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMDggNDhjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDhzMjEuNS00OCA0OC00OHM0OCAyMS41IDQ4IDQ4ek0xNTIgMzUyVjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYyNTYuOUw1OS40IDMwNC41Yy05LjEgMTUuMS0yOC44IDIwLTQzLjkgMTAuOXMtMjAtMjguOC0xMC45LTQzLjlsNTguMy05N2MxNy40LTI4LjkgNDguNi00Ni42IDgyLjMtNDYuNmgyOS43YzMzLjcgMCA2NC45IDE3LjcgODIuMyA0Ni42bDU4LjMgOTdjOS4xIDE1LjEgNC4yIDM0LjgtMTAuOSA0My45cy0zNC44IDQuMi00My45LTEwLjlMMjMyIDI1Ni45VjQ4MGMwIDE3LjctMTQuMyAzMi0zMiAzMnMtMzItMTQuMy0zMi0zMlYzNTJIMTUyeiIgLz48L3N2Zz4=" class="fa" /> </span>

<span style="
                font-weight:normal;
                color:grey;
                font-size:10px;
            "> 208,660,785 </span>

</div></td>
<td class="gt_row gt_left gt_striped"><div style="display: flex;">
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
