import os
from typing import Union

import bs4
import polars as pl
import requests

from nfl_stats.constants import BASE_URL

def get_gamelog_url(team: str, year: int) -> str:
    """Returns a sports-reference url for a given teams gamelog"""
    return os.path.join(BASE_URL, "teams", team, str(year), "gamelog")


def get_gamelog_soup(team: str, year: int) -> bs4.BeautifulSoup:
    """Returns parseable html soup"""
    url = get_gamelog_url(team=team, year=year)
    response = requests.get(url)
    return bs4.BeautifulSoup(response.text, "html.parser")
  
  
def get_gamelog_df(team: str, year: int) -> pl.DataFrame:
    """Get the gamelog for an NFL team in a given year"""
    soup = get_gamelog_soup(team=team, year=year)
    table = soup.find(id=f"gamelog{year}").find("tbody")
    parsed_rows = [parse_gamelog_row(row) for row in table.find_all("tr")]

    return pl.from_dicts(parsed_rows).with_columns([
        # integer columns
        (pl.col("week_num").cast(pl.Int64)),
        (pl.col("pts_off").cast(pl.Int64)),
        (pl.col("pts_def").cast(pl.Int64)),
        (pl.col("pass_cmp").cast(pl.Int64)),
        (pl.col("pass_att").cast(pl.Int64)),
        (pl.col("pass_yds").cast(pl.Int64)),
        (pl.col("pass_td").cast(pl.Int64)),
        (pl.col("pass_int").cast(pl.Int64)),
        (pl.col("pass_sacked").cast(pl.Int64)),
        (pl.col("pass_sacked_yds").cast(pl.Int64)),
        (pl.col("rush_att").cast(pl.Int64)),
        (pl.col("rush_yds").cast(pl.Int64)),
        (pl.col("rush_td").cast(pl.Int64)),
        (pl.col("fgm").cast(pl.Int64)),
        (pl.col("fga").cast(pl.Int64)),
        (pl.col("xpm").cast(pl.Int64)),
        (pl.col("xpa").cast(pl.Int64)),
        (pl.col("punt").cast(pl.Int64)),
        (pl.col("punt_yds").cast(pl.Int64)),
        (pl.col("third_down_success").cast(pl.Int64)),
        (pl.col("third_down_att").cast(pl.Int64)),
        (pl.col("fourth_down_success").cast(pl.Int64)),
        (pl.col("fourth_down_att").cast(pl.Int64)),
        # float columns
        (pl.col("pass_yds_per_att").cast(pl.Float64)),
        (pl.col("pass_net_yds_per_att").cast(pl.Float64)),
        (pl.col("pass_cmp_perc").cast(pl.Float64)),
        (pl.col("pass_rating").cast(pl.Float64)),
        (pl.col("rush_yds_per_att").cast(pl.Float64)),
    ])
  
  
  def parse_gamelog_row(row: bs4.element.Tag) -> dict[str, Union[int, float, str]]:
    """ Parse a gamelog table row into a dictionary """
    return {elem["data-stat"]: elem.text for elem in row}
