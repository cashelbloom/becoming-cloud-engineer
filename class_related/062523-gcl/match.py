from randomint import RandIntGen
from board_result import BoardResult


class Match:
    def __init__(self, teams):
        self.teams = teams
        self.assign_color_to_teams()

    def assign_color_to_teams(self):
        color = ''
        my_rand_int_gen = RandIntGen(0, 2)
        random_num_list = []
        are_numbers_same = True
        while are_numbers_same:
            random_num_list = [random_num for random_num in my_rand_int_gen.generate_rand_int(2)]
            if random_num_list[0] == random_num_list[1]:
                continue
            else:
                are_numbers_same = False
        self.teams[0].match_color = 'White' if random_num_list[0] == 1 else 'Black'
        self.teams[1].match_color = 'White' if random_num_list[1] == 1 else 'Black'


    def display_match_pairings(self):
        t = 0
        for i in range(0, 6):
            print(f'{self.teams[t].players[i].name} vs {self.teams[t+1].players[i].name}')

    def assign_game_points(self, result_list):
        if result_list[0] == 2 and result_list[1] == 2:
            self.teams[0].game_points += 1
            self.teams[1].game_points += 1
            return
        if self.teams[0].match_color == 'White' and result_list[0] == 1:
            self.teams[0].game_points += 3
            self.teams[1].game_points += 0
            return
        elif self.teams[0].match_color == 'Black' and result_list[0] == 1:
            self.teams[0].game_points += 4
            self.teams[1].game_points += 0
            return
        elif self.teams[0].match_color == 'White' and result_list[0] == 0:
            self.teams[0].game_points += 0
            self.teams[1].game_points += 4
            return
        elif self.teams[0].match_color == 'Black' and result_list[0] == 0:
            self.teams[0].game_points += 0
            self.teams[1].game_points += 3
            return

    def declare_match_board_results(self):
        # print(f'The teams are: {self.teams}')
        t = 0
        for i in range(0, 2):
            print(f'This is team number {i}: {self.teams[i].name}')
        for i in range(0, 6):
            board_result = BoardResult(i).declare_board_result()['result']
            # print(f'For board number {i} the result is {board_result}')
            self.assign_game_points(board_result)
        print(f'The Game points of the first team is: {self.teams[0].game_points}')
        print(f'The Game points of the second team is: {self.teams[1].game_points}')
        return {self.teams[0].name: self.teams[0].game_points, self.teams[1].name: self.teams[1].game_points}

    def declare_match_winner(self):
        board_results = self.declare_match_board_results()
        if board_results[self.teams[0].name] > board_results[self.teams[1].name]:
            print(f'The winner is: {self.teams[0].name}')
        elif board_results[self.teams[0].name] < board_results[self.teams[1].name]:
            print(f'The winner is: {self.teams[1].name}')
        else:
            print(f'The match between {self.teams[0].name} and {self.teams[1].name} ended in Draw')
