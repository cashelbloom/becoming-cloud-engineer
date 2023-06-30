from randomint import RandIntGen
from team import Team

class Match:
    def __init__(self,teams):
        self.teams = teams
        self.assign_color_to_teams()


    def assign_color_to_teams(self):
        color = ''
        my_rand_int_gen = RandIntGen(0, 2)
        random_num_list = []
        are_numbers_same = True
        while are_numbers_same:
            random_num_list = [random_num for random_num in my_rand_int_gen.generate_rand_int(2)]
            # print(f'The first number is: {random_num_list[0]} and the second number is {random_num_list[1]}')
            if random_num_list[0] == random_num_list[1]:
                continue
            else:
                are_numbers_same = False
        first_team_color = 'White' if random_num_list[0] == 1 else 'Black'
        second_team_color = 'White' if random_num_list[1] == 1 else 'Black'
        self.teams[0].match_color = first_team_color
        self.teams[1].match_color = second_team_color


# team_gg = Team('Ganges Grandmasters', 'GG')
# team_tck = Team('Triveni Continental Kings', 'TCK')
# print(f'The color assigned to team GG is: {team_gg.match_color}')
# print(f'The color assigned to team TCK is: {team_tck.match_color}')
# teams = [team_gg, team_tck]
# new_match = Match(teams)
# print(f'The color assigned to team GG is: {new_match.teams[0].match_color}')
# print(f'The color assigned to team TCK is: {new_match.teams[1].match_color}')
