lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = [
    {
        'name': 'Ramya',
        'numbers': {1,2,3,4,5}
    },
    {
        'name': 'Saanya',
        'numbers': {13, 21, 22, 5, 8}
    }
]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

player_1 = players[0]['numbers'].intersection(lottery_numbers)
player_1_match = len(player_1)
print(f'Player {players[0]["name"]} got {player_1_match}')

player_2 = players[1]['numbers'].intersection(lottery_numbers)
player_2_match = len(player_2)
print(f'Player {players[1]["name"]} got {player_2_match}')
