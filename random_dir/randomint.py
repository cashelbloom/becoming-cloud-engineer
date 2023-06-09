import random

class RandIntGen:
    def __init__(self, start_num, stop_num, seq=1):
        self.start = start_num
        self.stop = stop_num
        self.seq = seq
    #
    def generate_rand_int(self, number_of_rand_numbers):
        for i in range(0, number_of_rand_numbers):
            print(f'the {i + 1} random integer generated is: {random.randrange(self.start, self.stop, self.seq)}')

    def display_const_args(self):
        print(f'start: {self.start} stop: {self.stop} seq: {self.seq}')

#
# my_rand_int_gen = RandIntGen(1, 5, 1)
# my_rand_int_gen.generate_rand_int(1)
# my_rand_int_gen.display_const_args()