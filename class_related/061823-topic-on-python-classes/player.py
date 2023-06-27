class Player:
    def __init__(self, name, gender, country):
        self.name = name
        self.gender = gender
        self.country = country

    def __str__(self):
        return self.name + ' ' + self.gender + ' ' + self.country

    def play_game(self):
        pass