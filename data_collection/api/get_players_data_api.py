import pandas as pd
from understatapi import UnderstatClient

understat = UnderstatClient()



def get_player_data(league: str, season: str):

    player_data = understat.league(league).get_player_data(season)

    df = pd.DataFrame(player_data)
    return df



