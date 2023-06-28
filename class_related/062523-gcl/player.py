import json

class Player:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f'Player Name is: {self.name}, Player Category is: {self.category} '



















# my_player = Player('Vishy Anand', 'icon')
# print(my_player)

# with open("./data_for_gcl/player_names.json") as player_names:
#     player_names_list = [player_name for player_name in json.load(player_names)['players']]
#     players = []
#     for member in player_names_list:
#         player = Player(member['name'], member['category'])
#         print(player)
#         players.append(player)


#
