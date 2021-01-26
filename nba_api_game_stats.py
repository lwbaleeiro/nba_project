import sys

import numpy as np
import pandas as pd

# nba_api
import matplotlib.pyplot as plt
from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog

def get_player_stats_detail(player_name):
        
    player_dict = players.get_players()

    player_df = [player for player in player_dict if player['full_name'] == player_name][0]
    player_id = player_df['id']

    gamelog_player_all = playergamelog.PlayerGameLog(player_id=player_id, season = SeasonAll.all)
    gamelog_player_all_df = gamelog_player_all.get_data_frames()[0]

    gamelog_player_all_df = gamelog_player_all_df[['GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS']]
    gamelog_player_all_df = gamelog_player_all_df.rename(columns = {'GAME_DATE':'Game Date', 'FG_PCT' : 'FG %', 'FG3_PCT':'FG3 %', 'FT_PCT':'FT %'})
    gamelog_player_all_df['FG %'] = pd.Series(["{0:.2f}%".format(val * 100) for val in gamelog_player_all_df['FG %']], index = gamelog_player_all_df.index)
    gamelog_player_all_df['FG3 %'] = pd.Series(["{0:.2f}%".format(val * 100) for val in gamelog_player_all_df['FG3 %']], index = gamelog_player_all_df.index)
    gamelog_player_all_df['FT %'] = pd.Series(["{0:.2f}%".format(val * 100) for val in gamelog_player_all_df['FT %']], index = gamelog_player_all_df.index)

    return gamelog_player_all_df

def show_graph(player_name):
    player_dict = players.get_players()

    player_df = [player for player in player_dict if player['full_name'] == player_name][0]
    player_id = player_df['id']

    gamelog_player_all = playergamelog.PlayerGameLog(player_id=player_id, season = SeasonAll.all)
    gamelog_player_all_df = gamelog_player_all.get_data_frames()[0]

    fig, ax = plt.subplots()
    ax.scatter(gamelog_player_all_df['FG3A'], gamelog_player_all_df['FG3M'], c='blue', alpha=0.5)
    
    return fig

# To Do Tirar os [''] da lista de times.
def get_teams():
    team_dict = teams.get_teams()
    get_teams_df = pd.DataFrame(team_dict, columns=['abbreviation'])
    get_teams_list = get_teams_df.values.tolist()

    return get_teams_list