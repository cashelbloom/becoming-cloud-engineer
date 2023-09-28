from abc import ABC, abstractmethod

class Bowler(ABC):

    @abstractmethod
    def perform_spin_bowling(self):
        pass

    @abstractmethod
    def perform_pace_bowling(self):
        pass





