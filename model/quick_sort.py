from model.sorter import Sorter

class QuickSort(Sorter):
    def __init__(self, values):
        super().__init__(values)
        self._name = "Quick Sort"
        
        self.stack = [(0, len(values) - 1)]
        self.pivot_idx = -1
        self.partition_idx = -1
        self.i = -1 # Scanner
        self.state = "START_PARTITION" 
        self.low = 0
        self.high = 0

    @property
    def name(self): return self._name

    def step(self):
        if self.finished:
            return

        if self.state == "START_PARTITION":
            if not self.stack:
                self.finished = True
                self.active_indices.clear()
                return
            
            self.low, self.high = self.stack.pop()
            if self.low >= self.high:
                return

            self.pivot_idx = self.high
            self.i = self.low - 1
            self.partition_idx = self.low
            self.state = "PARTITIONING"
            self.active_indices = {self.pivot_idx, self.partition_idx}

        elif self.state == "PARTITIONING":
            self.active_indices = {self.pivot_idx, self.partition_idx, self.i}
            self.comparisons += 1

            if self.partition_idx < self.high:
                if self.values[self.partition_idx] < self.values[self.pivot_idx]:
                    self.i += 1
                    self.values[self.i], self.values[self.partition_idx] = (
                        self.values[self.partition_idx],
                        self.values[self.i],
                    )
                    self.swaps += 1
                self.partition_idx += 1
            else:
                self.values[self.i + 1], self.values[self.high] = (
                    self.values[self.high],
                    self.values[self.i + 1],
                )
                self.swaps += 1
                
                pi = self.i + 1
                self.stack.append((self.low, pi - 1))
                self.stack.append((pi + 1, self.high))
                self.state = "START_PARTITION"