import random

class RandIntGen:
    # def __init__(self, start_num, stop_num, seq=None):
    def __init__(self, start_num, stop_num, seq=1):
        self.start = start_num
        self.stop = stop_num
        self.seq = seq
    #
    def generate_rand_int(self, number_of_rand_numbers):
        rand_num_list = []
        for i in range(0, number_of_rand_numbers):
            rand_num_list.append(random.randrange(self.start, self.stop, self.seq))
            # print(f'the {i + 1} random integer generated is: {float(random.randrange(self.start, self.stop, self.seq))}')
            # print(f'the {i + 1} random integer generated is: {random.randrange(self.start, self.stop)}')
        return rand_num_list

    def display_const_args(self):
        print(f'start: {self.start} stop: {self.stop} seq: {self.seq}')
        # print(f'start: {self.start} stop: {self.stop}')

my_rand_int_gen = RandIntGen(0,2)
random_num_list = []
are_numbers_distinct = True
while are_numbers_distinct:
    random_num_list = [random_num for random_num in my_rand_int_gen.generate_rand_int(2)]
    if random_num_list[0] == random_num_list[1]:
        continue
    else:
        are_numbers_distinct = False

print(f'The two numbers are: {random_num_list}')

