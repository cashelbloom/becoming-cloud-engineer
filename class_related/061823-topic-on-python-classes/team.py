from player import Player

class Team:
    def __init__(self, team_name, team_lead, players, matches_played, points_accumulated ):
        self.team_name = team_name
        self.team_lead = team_lead
        self.players = players
        self.matches_played = matches_played
        self.points_accumulated = points_accumulated

    def __str__(self):
        return self.team_name + ' ' + str(self.points_accumulated)

    def assign_team_member(self, player):
        self.players.append(player)

    def play_match(self):
        pass

    def list_team_players(self):
        for i in self.players:
            print(f'Player is: {i}')


players_name = ['Vish', 'x', 'y', 'z', 'a', 'b']
players_country = ['Ind', 'Chn', 'Bds', 'Srl', 'Nep', 'Phi']
players_gener = ['M', 'M', 'F', 'F', 'M', 'F']
anand_players = []

# for i in range(0,6):
#     anand_players.append(Player(players_name[i], players_country[i], players_gener[i]))
#
# anand_team = Team('Anand Team', 'Vish Anand', anand_players, 0, 0)
# print(anand_team)

obj = Team('Anand Team', 'Vish', [], 0, 0)

for i in range(0,6):
    obj.assign_team_member(Player(players_name[i], players_country[i], players_gener[i]))

print(obj)

obj.list_team_players()








