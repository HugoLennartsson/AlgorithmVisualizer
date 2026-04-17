from model.sorter import Sorter

class BubbleSort(Sorter):
    def __init__(self, values):
        super().__init__(values)
        self.i = 0
        self.j = 0
        self._name = "Bubble Sort"
    
    @property
    def name(self): return self._name

    def step(self):
        n = len(self.values)

        if self.i >= n - 1:
            self.finished = True
            return

        self.active_indices = {self.j, self.j + 1}
        self.swap_indices.clear()
        self.comparisons += 1

        if self.values[self.j] > self.values[self.j + 1]:
            self.swap_indices = {self.j, self.j + 1}
            self.values[self.j], self.values[self.j + 1] = self.values[self.j + 1], self.values[self.j]
            self.swaps += 1

        self.j += 1
        if self.j >= n - self.i - 1:
            self.j = 0
            self.i += 1