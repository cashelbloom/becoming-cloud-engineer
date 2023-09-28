from player import Player
# from bowling import *


class CricketPlayer(Player):
    SELECTION_SPEED = 105

    def __init__(self, name, height, weight, pace, spin_degrees, reflexes_in_sec,
                 power_shot_dist, throws_speed, running_speed):
        self.name = name
        self.height = height
        self.weight = weight
        self.pace = pace
        self.spin_degrees = spin_degrees
        self.reflex = reflexes_in_sec
        self.power_shot_dist = power_shot_dist
        self. throws_speed = throws_speed
        self.running_speed = running_speed

    def display_physical_fitness(self):
        print(f'{self.name} runs 100 mtrs in {self.running_speed} seconds.')
        print(f'{self.name} throws cricket ball at {self.throws_speed} kmph speed')
        print(f'{self.name} shows reflexes in {self.reflex} seconds')
        print(f'{self.name} able to hit cricket ball to {self.power_shot_dist} meters.')

    def perform_pace_bowling(self) -> bool:
        print(f'{self.name} bowls at {self.pace} kmph speed')
        return True if self.pace >= 105 else False

    def perform_spin_bowling(self) -> bool:
        print(f'{self.name} bowls spinning the ball to maximm angle of {self.spin_degrees} degrees')
        return True if self.spin_degrees >= 90 else False

    def perform_batting(self):
        print('batting fine')

    def my_own_method(self):
        print(f'My name is: {self.name} and I am a bowler and batter')

    @staticmethod
    def calling_non_abstract_method():
        Player.non_abstract_method()