import pandas as pd
from understatapi import UnderstatClient

understat = UnderstatClient()



def get_player_data(league: str, season: str):

    player_data = understat.league(league).get_player_data(season)

    player_shot_data = []
    for player in player_data:
        player_id = player['id']
        player_name = player['player_name']
        player_team = player['team_title']
        player_minutes_played = player['time']
        player_games_played = player['games']

        # Append the filtered data for each player to the list
        player_shot_data.append({
            'Player ID': player_id,
            'Player Name': player_name,
            'Minutes Played': player_minutes_played,
            'Games Played': player_games_played
        })

    player_df = pd.DataFrame(player_shot_data)

    return player_df


def get_all_shots_data(df, season):

    player_df = df

    all_shots_data = []

    for index, row in player_df.iterrows():
        player_id = row['Player ID']
        player_name = row['Player Name']
        shot_data = understat.player(player=player_id).get_shot_data()
        for shot in shot_data:
            if shot.get('season', None) == season:
                shot_x = shot.get('X', None)
                shot_y = shot.get('Y', None)
                is_goal = shot.get('result', None) == 'Goal'  # Check if the shot resulted in a goal
                result = shot.get('result', None)
                shot_minute = shot.get('minute', None)
                # Append shot info along with player details to the list
                all_shots_data.append({
                    'Player ID': player_id,
                    'Player Name': player_name,
                    'Shot X': shot_x,
                    'Shot Y': shot_y,
                    'Is Goal': is_goal,
                    'Result': result,
                    'Shot Minute': shot_minute
                })
    
    shots_df = pd.DataFrame(all_shots_data)
    print(shots_df.head())
    return shots_df
          


def download_data(league: str, season: str):
    player_data = get_player_data(league, season)
    shots_data = get_all_shots_data(player_data, season)

    # Specify the file path using format strings for league and season
    file_path = f'./data/shots_data_{league}_{season}.csv'

    # Write the DataFrame to the file path
    shots_data.to_csv(file_path, index=False)
    print(f'Data successfully downloaded to {file_path}')



download_data('EPL', '2024')