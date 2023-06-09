'''



'''
class Lawn:
    def __init__(self, *, my_length, my_width):
        self.length = my_length
        self.width = my_width

    def absorb(self):
        print('I can help you absorb dusts in my surroundings')
        print(f'you know my size; it is {int(self.width * self.length)}')
        print(f'you know my size; it is {int(self.width) * int(self.length)}')

    def get_lawn_width(self):
        return self.width

    def get_lawn_length(self):
        return self.length

#
# manoj_lawn = Lawn(50, 40)
# manoj_lawn.absorb()
# radha_lawn = Lawn(60, 40)
# radha_lawn.absorb()
# dharani_lawn = Lawn(30, 30)
# dharani_lawn.absorb()
# raghu_lawn = Lawn(20, 20)
# raghu_lawn.absorb()
# ramya_lawn = Lawn(40, 80)
# ramya_lawn.absorb()
