import pygame
import sys
from view.barChart import BarChart
from model.random_values import RandomValues
from model.insertion_sort import InsertionSort

class Window:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Algorithm Visualizer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.sort_index = 1
        self.sorting = True
       

        self.BarChart = BarChart(
            values= RandomValues.generate_array(20),
            x=50,
            y=50,
            width=700,
            height = 600
        )
        self.insertionSorter = InsertionSort(self.BarChart.values)
    
         

    def run(self):
        while self.running:
            self.handle_events()
            self.update_sort()
            self.draw()
            self.clock.tick(10)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def draw(self):
        self.screen.fill((30,30,30))
        self.BarChart.draw(self.screen)
        pygame.display.flip()

    def update_sort(self):
        if self.insertionSorter and not self.insertionSorter.finished:
            self.insertionSorter.step()
            self.BarChart.active_indices = self.insertionSorter.active_indices
