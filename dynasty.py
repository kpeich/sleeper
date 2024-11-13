import requests
import json
import pandas as pd
import datetime as datetime
import SleeperAPI

#api_url = "https://api.sleeper.app/v1"
#sports 'nfl'
#uids = { 'kyle' : 655623333638914048 }
#leagueid = { 'dynasty' : 1120875192726683648 }

class FFLeague:
    def __init__(self, league_id, start_year, dynasty=False):
        self.league_id = league_id
        self.dynsaty = dynsaty
        self.seasons = [year for year in range(start_year, datetime.today().year)] if dynsaty else start_year
        self.sport = 'nfl'

    def get_rosters(self):
        pass

    def get_draft(self, year):
        pass

    def get_transactions(self):
        pass

if __name__ == '__main__':
    api = SleeperAPI()

    print('done')
