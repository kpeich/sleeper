import requests
import json
from datetime import datetime

class SleeperAPI:
    def __init__(self):
        self.base = 'https://api.sleeper.app'
        self.version = 'v1'

    def get_user(self, uid):
        url = f"{self.base}/{self.version}/user/{uid}"
        return requests.get(url)


    def get_league(self, uid):
        """
        Get league by ID
        """
        url = f"{self.base}/{self.version}/league/{uid}"
        return requests.get(url)

    def get_rosters(self, uid):
        """
        Get current rosters for a league
        """
        url = f"{self.base}/{self.version}/league/{uid}/rosters"
        return requests.get(url)

    def get_draft(self, uid):
        """
        Get draft by ID
        """
        url = f"{self.base}/{self.version}/draft/{draft_id}"
        return requests.get(url)

    def get_picks(self, uid):
        """
        Get picks in draft
        PARAMS:
            draft_id : id of draft
        RETURNS:
            picks : list of dicts for each pick in draft
        """
        url = f"{self.base}/{self.version}/draft/{uid}/picks"
        picks = requests.get(url)

        return picks
