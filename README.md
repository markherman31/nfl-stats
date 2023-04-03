# nfl-stats
# NFL Webscraper

This is a basic Python package which can be used to pull NFL gamelog data into structured DataFrames which uses https://www.pro-football-reference.com/ data. This repository is only for educational purposes.


## Installing

This package) is build with [Poetry](https://python-poetry.org/). To install this package, install Poetry, pull this repository, and run `make install`.

## Basic Usage

Once the package is installed, you can use it to scrape NFL sports data from the web.

```
from nfl_stats.gamelog import get_gamelog_df


# retrieve a gamelog DataFrame for the San Francisco 49ers
df = get_gamelog_df(team="sfo", year=2022)
````

The result is a Polars DataFrame with the complete list of columns below:

```
'week_num',
'game_day_of_week',
'game_date',
'boxscore_word',
'game_outcome',
'overtime',
'game_location',
'opp',
'pts_off',
'pts_def',
'pass_cmp',
'pass_att',
'pass_yds',
'pass_td',
'pass_int',
'pass_sacked',
'pass_sacked_yds',
'pass_yds_per_att',
'pass_net_yds_per_att',
'pass_cmp_perc',
'pass_rating',
'rush_att',
'rush_yds',
'rush_yds_per_att',
'rush_td',
'fgm',
'fga',
'xpm',
'xpa',
'punt',
'punt_yds',
'third_down_success',
'third_down_att',
'fourth_down_success',
'fourth_down_att',
'time_of_poss',
```
