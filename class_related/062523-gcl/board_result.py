from player import Player
from randomint import RandIntGen

class BoardResult:
    def __init__(self, board_number: int):
        self.board_number = board_number


    def declare_board_result(self):
        my_rand_int_gen = RandIntGen(0, 3)
        random_team_list = []
        are_numbers_zero = True
        while are_numbers_zero:
            random_team_list = my_rand_int_gen.generate_rand_int(2)
            if random_team_list[0] == 0 and random_team_list[1] == 0:
                continue
            elif random_team_list[0] == 1 and random_team_list[1] == 1:
                continue
            elif (random_team_list[0] == 0 and random_team_list[1] == 2) or (random_team_list[0] == 1 and random_team_list[1] == 2):
                continue
            elif (random_team_list[0] == 2 and random_team_list[1] == 0) or (
                        random_team_list[0] == 2 and random_team_list[1] == 1):
                continue
            else:
                are_numbers_zero = False
        print(f'result list values: {random_team_list}')
        return {'boardNumber': self.board_number, 'result': random_team_list}
