# Football Goal Location Analysis
A project showcasing Data Collection, Analytic and Visualisation Skills. Data is collected via web scraping/API and then utilising this data we create Visualisations showcasing Goal Graphics and have them be split by team, player.


## Data Collection Method

   The data used in this project and visualisations are collected from one website which is [UnderStat.com](https://understat.com/). From here you can utilise an API package from pypi which neatly has packaged functions to obtain data from the site.

   1. The pypi package understatapi I create a client and then using the client call to the players data endpoint which can take variables for both league and season. The returned response is a pandas DataFrame with all players data for that league and season.

   2. To showcase web_scraping skills I have written a python script also that scrapes the [UnderStat.com](https://understat.com/) site. This also returns a DataFrame containing player data which is only from the latest season but the league variable is still.

