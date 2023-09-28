from cricket_player import *


def declare_player_selection(player) -> bool:
    can_bowl_fast = player.perform_pace_bowling()
    can_bowl_spin = player.perform_spin_bowling()
    return True if can_bowl_spin and can_bowl_fast else False
    # return True if can_bowl_spin else False
    # return True if can_bowl_fast else False


player_for_selection = CricketPlayer('Raj', 175, 150, 105, 91, 4, 200, 90, 13)
print(f'the data type of player_for_selection is: {type(player_for_selection)}')
selection_result = declare_player_selection(player_for_selection)
print(f'Selection Result is {"Selected" if selection_result == True else "Not Selected"}')
player_for_selection.my_own_method()
# player_for_selection.calling_non_abstract_method()
CricketPlayer.non_abstract_method()