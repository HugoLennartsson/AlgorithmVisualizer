import pygame
import sys
from view.barChart import BarChart
from model.random_values import RandomValues
from model.insertion_sort import InsertionSort
from model.bubble_sort import BubbleSort

class Window:
    def __init__(self):
        pygame.init()

        pygame.init()
        
        # Setup Display
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Data and View
        initial_data = RandomValues.generate_array(30)
        self.bar_chart = BarChart(
            values=initial_data,
            x=50,
            y=100, 
            width=700,
            height=450
        )

        # Strategy pointer 
        self.sorter = InsertionSort(initial_data)
        self.update_caption()
    
    def update_caption(self):
        status = "FINISHED" if self.sorter.finished else "RUNNING"
        pygame.display.set_caption(f"Algorithm Visualizer: {self.sorter.name} - {status}")

    def change_strategy(self, sorter_class):
        new_data = RandomValues.generate_array(30)
        self.bar_chart.values = new_data
        self.sorter = sorter_class(new_data)
        self.update_caption() 
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # Key listeners 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.change_strategy(InsertionSort)
                elif event.key == pygame.K_2:
                    self.change_strategy(BubbleSort)
                elif event.key == pygame.K_r:
                    # Restart 
                    self.change_strategy(self.sorter.__class__)

    def update_sort(self):
        if not self.sorter.finished:
            self.sorter.step()
            self.bar_chart.active_indices = self.sorter.active_indices
            
            if self.sorter.finished:
                self.update_caption()

    def draw(self):
        self.screen.fill((30, 30, 30)) 
        self.bar_chart.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update_sort()
            self.draw()
            self.clock.tick(20) 
            
        pygame.quit()
        sys.exit()