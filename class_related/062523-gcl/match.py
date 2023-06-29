from randomint import RandIntGen
from team import Team

class Match:
    def __init__(self,teams):
        self.teams = teams


    def assign_color_to_teams(self):
        my_rand_int_gen = RandIntGen(0, 2)
        random_num_list = []
        are_numbers_distinct = True
        while are_numbers_distinct:
            random_num_list = [random_num for random_num in my_rand_int_gen.generate_rand_int(2)]
            print(f'The first number is: {random_num_list[0]} and the second number is {random_num_list[1]}')
            if random_num_list[0] == random_num_list[1]:
                continue
            else:
                are_numbers_distinct = False
        self.teams[0] = random_num_list[0]
        self.teams[1] = random_num_list[1]
        if random_num_list[0] == 1:
            print('The first color is White')
        else:
            print('The first color is Black')

