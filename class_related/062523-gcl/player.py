
class Player:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f'Player Name is: {self.name}, Player Category is: {self.category}'
