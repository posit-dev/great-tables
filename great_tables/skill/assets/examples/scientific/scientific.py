"""Scientific archetype — distilled reference example.

Data: data/reactions.csv  (1,683 atmospheric reactions; rate constants
      of trace gases with OH and three other oxidants, with
      uncertainties)
Story: OH rate constants at 298 K for ten common trace gases, with
       units in the headers, scientific notation, and percent
       uncertainty.

No Big Color here: the rate constant spans five orders of magnitude by
deliberate curated-subset design, so a LINEAR data_color domain over it would
paint nearly every cell the same faint shade (only the fastest reaction or two
would stand out) — a technically-qualifying gradient that would actively
mislead rather than inform. The scientific-notation formatting already
carries the magnitude story; the heading band is this table's only branding
surface, by design, not an oversight.
"""
import pandas as pd
from great_tables import GT, html, loc, style

df = pd.read_csv("data/reactions.csv")

# Curated subset spanning the full reactivity range (10⁻¹⁵ → 10⁻¹⁰), sorted
# slow → fast so the eye walks reactivity in a natural reading order.
picks = ["methane", "benzene", "ethanol", "methanol", "toluene",
         "formaldehyde", "ethene", "acetaldehyde", "propene", "isoprene"]
sub = (
    df[df["cmpd_name"].isin(picks)]
      .loc[:, ["cmpd_name", "cmpd_formula", "cmpd_mwt", "OH_k298", "OH_uncert"]]
      .sort_values("OH_k298")
      .reset_index(drop=True)
)
sub["cmpd_name"] = sub["cmpd_name"].str.capitalize()

fastest = sub.loc[sub["OH_k298"].idxmax(), "cmpd_name"]
slowest = sub.loc[sub["OH_k298"].idxmin(), "cmpd_name"]
ratio = sub["OH_k298"].max() / sub["OH_k298"].min()

gt = (
    GT(sub, rowname_col="cmpd_name")
    .tab_header(
        title="OH reaction rate constants at 298 K",
        # Units declared once in the subtitle, not on every cell. Standard
        # convention for scientific tables — keeps cells readable.
        subtitle=html(
            "Selected trace gases. k in cm<sup>3</sup>&nbsp;molecule<sup>&minus;1</sup>&nbsp;s<sup>&minus;1</sup>."
        ),
    )
    .cols_label(
        cmpd_formula="Formula",
        cmpd_mwt=html("M<sub>w</sub> (g mol<sup>&minus;1</sup>)"),
        OH_k298=html("k(298 K)"),
        OH_uncert="Rel. uncert.",
    )
    # fmt_scientific on rate constants — fmt_number(decimals=4) would round
    # 6.36e-15 to 0.0000 and destroy the data. n_sigfig=3 matches source
    # compilation precision.
    .fmt_scientific(columns=["OH_k298"], n_sigfig=3)
    .fmt_number(columns=["cmpd_mwt"], decimals=2)
    # Uncertainty stored as fraction (0.10), shown as percent (10%) — matches
    # the convention of the source compilation.
    .fmt_percent(columns=["OH_uncert"], decimals=0)
    .sub_missing(columns=["OH_uncert"], missing_text="—")
    .cols_align(align="left", columns=["cmpd_formula"])
    .cols_align(align="right", columns=["cmpd_mwt", "OH_k298", "OH_uncert"])
    # Heading band — fixed branding navy, bold labels, white text, every
    # table, regardless of whether the body itself heatmaps.
    .tab_options(
        column_labels_background_color="#08306B",
        column_labels_font_weight="bold",
        column_labels_border_bottom_color="#CCCCCC",
        column_labels_border_bottom_width="2px",
    )
    .tab_style(style=style.text(color="white"), locations=loc.column_labels())
    # Stub tint — fixed branding hex, unconditional whenever a stub exists.
    .tab_style(style=style.fill(color="#EAF0F6"), locations=loc.stub())
    # Row striping — default on every table; nothing here is color-filled.
    .opt_row_striping()
    .tab_options(
        row_striping_background_color="#F6F6F6",
        table_body_hlines_style="solid",
        table_body_hlines_color="#E8E8E8",
        table_body_hlines_width="1px",
        table_border_top_style="solid", table_border_top_color="#CCCCCC", table_border_top_width="1px",
        table_border_bottom_style="solid", table_border_bottom_color="#CCCCCC", table_border_bottom_width="1px",
        table_border_left_style="solid", table_border_left_color="#CCCCCC", table_border_left_width="1px",
        table_border_right_style="solid", table_border_right_color="#CCCCCC", table_border_right_width="1px",
    )
    .cols_width(cases={
        "cmpd_name": "130px", "cmpd_formula": "90px", "cmpd_mwt": "110px",
        "OH_k298": "110px", "OH_uncert": "100px",
    })
    .tab_options(
        heading_padding="6px",
        column_labels_padding="6px",
        column_labels_padding_horizontal="8px",
        data_row_padding="5px",
        data_row_padding_horizontal="8px",
        source_notes_padding="6px",
    )
    .tab_source_note(
        source_note=html(
            f"{fastest} reacts with OH roughly {ratio:,.0f}&times; faster than {slowest} in this set."
        )
    )
    .tab_source_note(
        source_note=html(
            "Source: IUPAC Task Group on Atmospheric Chemical Kinetic Data Evaluation, "
            "compiled in the <code>reactions</code> dataset (Posit / great_tables sample data)."
        )
    )
)

gt.gtsave("scientific.png", zoom=2.0, expand=15)
