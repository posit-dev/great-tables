# Using Polars to Win at Super Bowl Squares

The Super Bowl is upon us, and with it the glittering squares of chance. Maybe you've seen Super Bowl Squares at your work. Maybe you've played it with your pals. Or maybe you have no idea what it is.

Whether you're a Squares-head or not, this post will help you win with data.


# What is Super Bowl Squares?

Super Bowl Squares is a betting game, where you bet on the final digits of each team in a game.

For example, here are some scores with the final digit bolded:

- Home team score: 1**4**
- Away team score: **7**

So the final digits would be:

- Home team digit: 4
- Away team digit: 7

Let's say you choose the digits above, and write this as 4/7--meaning a final digit of 4 for home and 7 for away. You would mark yourself on this square:


Code

``` python
df = (
    pl.DataFrame({"x": list(range(10))})
    .join(pl.DataFrame({"y": list(range(10)), "z": "_._"}), how="cross")
    .with_columns(
        z=pl.when((pl.col("x") == 7) & (pl.col("y") == 4)).then(pl.lit("4/7")).otherwise("z")
    )
    .pivot(index="x", values="z", on="y")
    .with_row_index()
)

(
    GT(df, rowname_col="x")
    .tab_header("Example Superbowl Square")
    .tab_spanner("Home", cs.all())
    .tab_style(style.fill("green"), loc.body(columns="4", rows=pl.col("index") == 7))
    .tab_style(style.text(color="#FFFFFF", weight="bold"), loc.body())
    .cols_hide("index")
    .tab_stubhead("Away")
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="11" class="gt_heading gt_title gt_font_normal">Example Superbowl Square</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Away" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Away</th>
<th colspan="10" id="Home" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Home</th>
</tr>
<tr class="gt_col_headings">
<th id="0" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">0</th>
<th id="1" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">1</th>
<th id="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">2</th>
<th id="3" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">3</th>
<th id="4" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">4</th>
<th id="5" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">5</th>
<th id="6" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">6</th>
<th id="7" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">7</th>
<th id="8" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">8</th>
<th id="9" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">9</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">0</th>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">1</th>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">2</th>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">3</th>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">4</th>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">5</th>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">6</th>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">7</th>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="background-color: green; color: #FFFFFF; font-weight: bold">4/7</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">8</th>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">9</th>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
</tbody>
</table>


If the final score ends up being Home 4, Away 7--ding ding ding, big winner--you win the pool, and hopefully take home some combination of money and glory. For more details on playing, see [this WikiHow article](https://www.wikihow.com/Play-Football-Squares).


# Why analyze squares?

Not all options in a Super Bowl Squares are created equal. This is because there are specific point values you can add to your score. For example, touchdowns often to result in 7 points, and its common to score 3 points via a field goal. This means that ending up with a final digit of 5 is uncommon.

Analyzing the chance of each square winning let's you pick the best ones. (In some versions of Super Bowl Squares, the squares get randomly assigned to people. In that case, knowing the chance of winning tells you whether you got a bum deal or not ;).


# What squares are most likely to win?

We looked back at games for the KC Chiefs (away), and games for the San Francisco 49ers (home), and calculated the proportion of the time each team ended with a specific digit. Putting this together for the two teams, here is the chance of winning on a given square:


Code

``` python
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
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="11" class="gt_heading gt_title gt_font_normal">Super Bowl Squares | Final Score Probabilities</th>
</tr>
<tr class="gt_heading">
<th colspan="11" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Based on all NFL regular season and playoff games (2015-2023)</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="KC-Chiefs" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">KC Chiefs</th>
<th colspan="10" id="San-Francisco-49ers" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">San Francisco 49ers</th>
</tr>
<tr class="gt_col_headings">
<th id="0" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">0</th>
<th id="1" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1</th>
<th id="2" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2</th>
<th id="3" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">3</th>
<th id="4" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">4</th>
<th id="5" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">5</th>
<th id="6" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">6</th>
<th id="7" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">7</th>
<th id="8" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">8</th>
<th id="9" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">9</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #ff0000">0</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #a2a2c8">2.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ce8e8e">1.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #9898cb">2.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c8a2a2">1.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #4c4ce5">3.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #de5f5f">1</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4abab">1.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c1b4b4">1.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d57c7c">1.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #8585d2">2.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #bebebe">2</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #cb9898">1.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #FFFFFF; background-color: #5f5fde">3</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #c8a2a2">1.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4abab">1.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d57c7c">1.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #8e8ece">2.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #FFFFFF; background-color: #0000ff">4</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4abab">1.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c1b4b4">1.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d57c7c">1.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #8585d2">2.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">5</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">6</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d28585">1.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">7</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #a2a2c8">2.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ce8e8e">1.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #9898cb">2.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c8a2a2">1.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #3939ec">3.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">8</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">9</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ce8e8e">1.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="11" class="gt_sourcenote"><span style="float: right;">Source data: [Lee Sharpe, nflverse](https://github.com/nflverse/nfldata)</span></td>
</tr>
</tfoot>

</table>


Notice how much higher the chance of winning on any score involving 7 is. This shows up in two places on the table:

- Across the 7 row (i.e. KC Chiefs end with a 7)
- Down the 7 column (i.e. S.F. 49ers ends with a 7)

Moreover, the 7/7 square has the highest chance (3.4%). Some other good squares are 7/0 (or 0/7), and 0/0.


# Go forth and win the respect of your coworkers

We hope this square will make you the envy of your coworkers. Here at Great Tables, we're not just interested in the beautiful display of tables, but your success in defeating the person in the cubicle next to you.

As a final shout out, we used the python data analysis tool Polars for all the data analysis. Using Polars with Great Tables was a total delight. To learn more about how we analyzed the data, along with the code, see the appendix below!

> **Note: Appendix: analysis and code**
