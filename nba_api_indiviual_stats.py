import sys

import numpy as np
import pandas as pd

# nba_api
import matplotlib.pyplot as plt
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog

def get_player_stats(player_name, fundamental, season_all):
        
    player_dict = players.get_players()

    player_df = [player for player in player_dict if player['full_name'] == player_name][0]
    player_id = player_df['id']

    if season_all == True:
        gamelog_player_all = playergamelog.PlayerGameLog(player_id=player_id, season = SeasonAll.all)
    else:
        gamelog_player_all = playergamelog.PlayerGameLog(player_id=player_id, season = SeasonAll.current_season)

    gamelog_player_all_df = gamelog_player_all.get_data_frames()[0]

    return gamelog_player_all_df[fundamental].mean().round(decimals=1)



def get_player_stats_detail_all(player_name):
    pts_all = get_player_stats(player_name, 'PTS', True) 
    reb_all = get_player_stats(player_name, 'REB', True) 
    ast_all = get_player_stats(player_name, 'AST', True) 

    df_all = {'Pts':pts_all, 'Reb':reb_all, 'Ast':ast_all}
    player_stats_df = pd.DataFrame(data=df_all, index=[''])
    return player_stats_df  

def get_player_stats_detail(player_name):
    pts = get_player_stats(player_name, 'PTS', False) 
    reb = get_player_stats(player_name, 'REB', False)
    ast = get_player_stats(player_name, 'AST', False) 

    df = {'Pts':pts, 'Reb':reb, 'Ast':ast}
    player_stats_df = pd.DataFrame(data=df, index=[''])
    return player_stats_df