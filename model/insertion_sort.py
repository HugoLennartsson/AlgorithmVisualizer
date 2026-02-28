from model.sorter import Sorter

class InsertionSort(Sorter):
    def __init__(self, values):
        super().__init__(values)
        self.i = 1  
        self.finished = False
        self.active_indices = set()
        self._name = "Insertion Sort"

    @property
    def name(self): return self._name

    def step(self):
        self.active_indices.clear()

        if self.finished:
            return

        if self.i >= len(self.values):
            self.finished = True
            return

        self.active_indices.update({self.i, self.i-1})
        
        if self.i > 0 and self.values[self.i] < self.values[self.i - 1]:
            self.values[self.i], self.values[self.i - 1] = (
                self.values[self.i - 1],
                self.values[self.i],
            )
            self.i -= 1
        else:
            self.i += 1