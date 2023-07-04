from player import Player

class Team:

    def __init__(self, name, abbr, players, game_points=0, match_points=0):
        self.name = name
        self.abbr = abbr
        self.players = players
        self.game_points = game_points
        self.match_points = match_points
        self.match_color = ''
        # self.add_player(self.players)

    def __str__(self):
        return f'Team Name is: {self.name} and the Abbreviation is: {self.abbr}'

    def list_team_players(self):
        for player in self.players:
            print(player)

    def add_player(self, players_from_outside):
        for player in players_from_outside:
            self.players.append(player)
