import json
from player import Player
from team import Team

PLAYER_PATH = "./data_for_gcl/player_names.json"
TEAM_PATH = "./data_for_gcl/team_names.json"
#TEAMS IS A LIST OF TEAM OBJECTS
TEAMS = []

def build_teams(player_path, team_path):
    with open(player_path) as player_names:
        player_names_list = [player_name for player_name in json.load(player_names)['players']]
    #
    with open(team_path) as team_names:
        team_names_list = [team_name for team_name in json.load(team_names)['teamNames']]
    #
    for team in team_names_list:
        players = []
        team_object = Team(team['name'], team['abbr'], players)
        for player in player_names_list:
            player_object = Player(player['name'], player['category'])
            players.append(player_object)
        TEAMS.append(team_object)


def main():
    build_teams(PLAYER_PATH, TEAM_PATH)
    print(f'The number of teams in the TEAMS list is: {len(TEAMS)}')


if __name__ == "__main__":
    main()


#############################################################
    # with open() as player_names:
    #     player_names_list = [player_name for player_name in json.load(player_names)['players']]
    #     # for item in player_names_list:
    #     #     print(f'Name: {item["name"]} and the category is: {item["category"]}')
    #     # print(f'just the player name printed individually: {}')
    #     # print(f'Players List: {player_names_list}')
    # #
    #
    #     print(f'Teams List: {team_names_list}')
    # #     # print(for name in team_names_list)












# player_names_dict = json.load(player_names)
# player_names_list = [player_name for player_name in player_names_dict['players']]