import json
import datetime
from player import Player
from team import Team
from randomint import RandIntGen
from match import Match

class MatchScheduler:
    MATCH_START_DATE = '07/02/23'

    def __init__(self, teams):
        self.teams = teams

    def schedule_matches(self):
        first_round_color = 'White'
        
