from model.sorter import Sorter

class SelectionSort(Sorter):
    def __init__(self, values):
        super().__init__(values)
        self.i = 0  
        self.j = 1  
        self.min_idx = 0
        self._name = "Selection Sort"

    @property
    def name(self): return self._name

    def step(self):
        n = len(self.values)

        if self.i >= n - 1:
            self.finished = True
            self.active_indices.clear()
            return

        self.active_indices = {self.i, self.j, self.min_idx}
        self.comparisons += 1

        if self.values[self.j] < self.values[self.min_idx]:
            self.min_idx = self.j

        self.j += 1

      
        if self.j >= n:
       
            self.values[self.i], self.values[self.min_idx] = (
                self.values[self.min_idx],
                self.values[self.i],
            )
            self.swaps += 1
            
      
            self.i += 1
            self.j = self.i + 1
            self.min_idx = self.i