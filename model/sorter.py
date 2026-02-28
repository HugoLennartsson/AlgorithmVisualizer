from abc import ABC, abstractmethod

class Sorter(ABC):
    def __init__(self, values):
        self.values = values
        self.finished = False
        self.active_indices = set()
        self.comparisons = 0
        self.swaps = 0

    @abstractmethod
    def step(self) -> None:
        """Perform one atomic step of the algorithm."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the algorithm."""
        pass