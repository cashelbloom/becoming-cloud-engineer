'''
class Ball
 mycolor and mymaterial are parameters
color and material are attributes
'''
class Ball:
    def __init__(self, mycolor, mymaterial):
        self.color = mycolor
        self.material = mymaterial


    def can_bounce(self):
        print(f'I can bounce back and my color is {self.color} and material is {self.material}')

my_ball = Ball('red', "rubber")
my_ball.can_bounce()