import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

# Function to get shot data for a specific match
def get_player_data(league):
    url = f'https://understat.com/league/{league}'
    res = requests.get(url)
    if res.status_code != 200:
        print(f'Failed to return data, Response Code: {res.status_code}')

    soup = BeautifulSoup(res.content, 'html.parser')
    
    scripts = soup.find_all('script')
    shot_data = None
    
    for script in scripts:
        if 'playersData' in script.text:
            text = script.string.split('JSON.parse(\'')[1].rsplit('\');', 1)[0]
            decoded_text = text.encode('utf8').decode('unicode_escape')
            players_data = json.loads(decoded_text)
            break

    df = pd.DataFrame(players_data)
    return df




get_player_data('EPL')