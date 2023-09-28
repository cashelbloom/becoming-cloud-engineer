from abc import ABC, abstractmethod


class Batter(ABC):
    @abstractmethod
    def perform_batting(self):
        pass
