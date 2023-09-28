from abc import abstractmethod
from bowler import Bowler
from batter import Batter


class Player(Bowler, Batter):
    @abstractmethod
    def display_physical_fitness(self):
        pass

    @staticmethod
    def non_abstract_method():
        print('I am printing from non-abstract method')
