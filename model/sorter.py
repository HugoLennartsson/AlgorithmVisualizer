from abc import ABC, abstractmethod

class Sorter(ABC):
    def __init__(self, values):
        self.values = values
        self.finished = False

    @abstractmethod
    def step(self):
        """Perform ONE visual step of the algorithm"""
        pass