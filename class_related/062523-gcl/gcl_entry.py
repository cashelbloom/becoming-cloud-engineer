import json
from player import Player
from team import Team

PLAYER_PATH = "./data_for_gcl/player_names.json"
TEAM_PATH = "./data_for_gcl/team_names.json"
TEAMS = [] #TEAMS IS A LIST OF TEAM OBJECTS

def build_teams(player_path, team_path):
    with open(player_path) as player_names:
        player_names_list = [player_name for player_name in json.load(player_names)['players']]
    #
    with open(team_path) as team_names:
        team_names_list = [team_name for team_name in json.load(team_names)['teamNames']]
    #
    start = 0
    end = 6
    for team in team_names_list:
        players = []
        team_object = Team(team['name'], team['abbr'], players)
        # team_object.add_player(player_names_list)
        for i in range(start, end):
            player = player_names_list[i]
            player_object = Player(player['name'], player['category'])
            players.append(player_object)
        start += 6
        end += 6
        TEAMS.append(team_object)


def main():
    build_teams(PLAYER_PATH, TEAM_PATH)
    print(f'The number of teams in the TEAMS list is: {len(TEAMS)}')
    for team in TEAMS:
        print(f'\nTeam Name: {team.name}, Team Abbreviation: {team.abbr}')
        for player in team.players:
            print(player)

if __name__ == "__main__":
    main()

