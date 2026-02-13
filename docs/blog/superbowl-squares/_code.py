import polars as pl
import polars.selectors as cs
from great_tables import GT, md


# Utilities -----


def calc_n(df: pl.DataFrame, colname: str):
    """Count the number of final digits observed across games."""

    return df.select(final_digit=pl.col(colname).mod(10)).group_by("final_digit").agg(n=pl.len())


def team_final_digits(game: pl.DataFrame, team_code: str) -> pl.DataFrame:
    """Calculate a team's proportion of digits across games (both home and away)."""

    home_n = calc_n(game.filter(pl.col("home_team") == team_code), "home_score")
    away_n = calc_n(game.filter(pl.col("away_team") == team_code), "away_score")

    joined = (
        home_n.join(away_n, "final_digit")
        .select("final_digit", n=pl.col("n") + pl.col("n_right"))
        .with_columns(prop=pl.col("n") / pl.col("n").sum())
    )

    return joined


# Analysis -----

games = pl.read_csv("./games.csv").filter(
    pl.col("game_id") != "2023_22_SF_KC",
    pl.col("season") >= 2015,
)

# Individual probabilities of final digits per team
home = team_final_digits(games, "KC")
away = team_final_digits(games, "SF")

# Cross and multiply p(digit | team=KC)p(digit | team=SF) to get
# the joint probability p(digit_KC, digit_SF | KC, SF)
joint = (
    home.join(away, how="cross")
    .with_columns(joint=pl.col("prop") * pl.col("prop_right"))
    .sort("final_digit", "final_digit_right")
    .pivot(values="joint", on="final_digit_right", index="final_digit")
    .with_columns((cs.exclude("final_digit") * 100).round(1))
)

# Display -----

(
    GT(joint, rowname_col="final_digit")
    .data_color(domain=[0, 4], palette=["red", "grey", "blue"])
    .tab_header(
        "Super Bowl Squares | Final Score Probabilities",
        "Based on all NFL regular season and playoff games (2015-2023)",
    )
    .tab_stubhead("")
    .tab_spanner("San Francisco 49ers", cs.all())
    .tab_stubhead("KC Chiefs")
    .tab_source_note(
        md(
            '<span style="float: right;">Source data: [Lee Sharpe, nflverse](https://github.com/nflverse/nfldata)</span>'
        )
    )
)
