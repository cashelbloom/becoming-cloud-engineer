class Ball:

    def __init__(self, size, color):
        self.size = size
        self.color = color

    def get_description(self):
        print(f'The size of the ball is {str(self.size)}.')
        print(f'The color of the ball is {self.color}.')

my_ball = Ball(4, 'Purple')
my_ball.get_description()