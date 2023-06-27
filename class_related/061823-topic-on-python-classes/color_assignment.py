class ColorAssignment:
    def __init__(self, teams):
        self.teams = teams


    def assign_color(self):
        self.teams[0] = 'white'
        self.teams[1] = 'black'


# new_color_assignment = ColorAssignment()