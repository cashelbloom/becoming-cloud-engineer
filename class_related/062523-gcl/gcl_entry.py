import json
from player import Player
from team import Team
from randomint import RandIntGen
from match import Match

PLAYER_PATH = "./data_for_gcl/player_names.json"
TEAM_PATH = "./data_for_gcl/team_names.json"
TEAMS = []


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
        players_coll = []
        team_object = Team(team['name'], team['abbr'],players_coll)
        for i in range(start, end):
            player = player_names_list[i]
            player_object = Player(player['name'], player['category'])
            players_coll.append(player_object)
        team_object.players = players_coll
        TEAMS.append(team_object)
        start += 6
        end += 6


def create_match():
    my_rand_int_gen = RandIntGen(0, 6)
    random_team_list = []
    are_teams_same = True
    while are_teams_same:
        random_team_list = my_rand_int_gen.generate_rand_int(2)
        if random_team_list[0] == random_team_list[1]:
            continue
        else:
            are_teams_same = False
    the_first_team = TEAMS[random_team_list[0]]
    the_second_team = TEAMS[random_team_list[1]]
    the_new_match = Match([the_first_team, the_second_team])
    print(f'The first team is: {the_first_team} and the second team is: {the_second_team}')
    return the_new_match


def main():
    build_teams(PLAYER_PATH, TEAM_PATH)
    the_match = create_match()
    for team in the_match.teams:
        print(f'The color for {team.name} is {team.match_color}')
    the_match.display_match_pairings()
    the_match.declare_match_winner()


if __name__ == "__main__":
    main()

