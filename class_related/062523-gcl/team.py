import json
from player import Player


class Team:
    def __init__(self, name, abbr, game_points=0, match_points=0):
        self.name = name
        self.abbr = abbr
        self.players = []
        self.game_points = game_points
        self.match_points = match_points
        self.match_color = ''

    def __str__(self):
        return f'Team Name is: {self.name} and the Abbreviation is: {self.abbr}'

    def list_team_players(self):
        for player in self.players:
            print(player)

    def add_player(self, players_from_outside):
        for player in players_from_outside:
            self.players.append(player)




# with open("./data_for_gcl/player_names.json") as player_names:
#     player_names_list = [player_name for player_name in json.load(player_names)['players']]
#     players = []
#     for member in player_names_list:
#         player = Player(member['name'], member['category'])
#         players.append(player)
#
#
# with open("./data_for_gcl/team_names.json") as team_names:
#     team_names_list = [team_name for team_name in json.load(team_names)['teamNames']]
#     teams = []
#     start = 0
#     end = 6
#     for member in team_names_list:
#         team = Team(member['name'], member['abbr'])
#         print(team)
#         teams.append(team)



