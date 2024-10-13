import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

# Function to get shot data for a specific match
def get_shot_data(league):
    url = f'https://understat.com/league/{league}'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    scripts = soup.find_all('script')
    shot_data = None
    
    for script in scripts:
        if 'playerData' in script.text:
            json_text = script.text.split('= ')[1].strip().rstrip(';')
            shot_data = json.loads(json_text)
            break
    
    df = pd.DataFrame(shot_data)
    return shot_data

## Main function to get shots for all matches in a season
#def get_all_shots():
#    all_shots = []
#    
#    for match_id in match_ids:
#        shot_data = get_shot_data(match_id)
#        
#        for shot in shot_data:
#            all_shots.append({
#                'match_id': match_id,
#                'player': shot['player'],
#                'team': shot['h_team'] if shot['h_a'] == 'h' else shot['a_team'],
#                'minute': shot['minute'],
#                'xG': shot['xG'],
#                'result': shot['result'],
#                'x': shot['X'],
#                'y': shot['Y']
#            })
#    
#    return pd.DataFrame(all_shots)

# Example: Get all shots for the 2023/2024 EPL season


get_shot_data('EPL')