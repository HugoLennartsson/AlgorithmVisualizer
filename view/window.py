import pygame
import sys
from view.barChart import BarChart
from view.menu import Menu, ALGORITHMS
from model.random_values import RandomValues
from model.insertion_sort import InsertionSort
from model.bubble_sort import BubbleSort
from model.selection_sort import SelectionSort
from model.quick_sort import QuickSort

ALGORITHM_MAP = {
    "InsertionSort": InsertionSort,
    "BubbleSort": BubbleSort,
    "SelectionSort": SelectionSort,
    "QuickSort": QuickSort,
}

class Window:
    STATE_MENU = "MENU"
    STATE_VISUALIZING = "VISUALIZING"

    def __init__(self):
        pygame.init()

        # Setup Display
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        # Menu
        self.menu = Menu(self.width, self.height)
        self.state = self.STATE_MENU

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
        self.bar_chart.sweep_indices.clear()
        self.bar_chart.sweeping = False
        self.bar_chart.pivot_index = -1
        self.bar_chart.swap_indices.clear()
        self.sorter = sorter_class(new_data)
        self.update_caption()

    def start_visualization(self, algorithm_data):
        sorter_class = ALGORITHM_MAP[algorithm_data["class"]]
        self.change_strategy(sorter_class)
        self.state = self.STATE_VISUALIZING

    def return_to_menu(self):
        self.state = self.STATE_MENU
        self.menu = Menu(self.width, self.height)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEMOTION:
                if self.state == self.STATE_MENU:
                    self.menu.handle_mouse_move(event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.state == self.STATE_MENU:
                        algo = self.menu.handle_click(event.pos)
                        if algo:
                            self.start_visualization(algo)

            if event.type == pygame.KEYDOWN:
                if self.state == self.STATE_MENU:
                    pass
                else:
                    if event.key == pygame.K_1:
                        self.change_strategy(InsertionSort)
                    elif event.key == pygame.K_2:
                        self.change_strategy(BubbleSort)
                    elif event.key == pygame.K_3:
                        self.change_strategy(SelectionSort)
                    elif event.key == pygame.K_4:
                        self.change_strategy(QuickSort)
                    elif event.key == pygame.K_r:
                        self.change_strategy(self.sorter.__class__)
                    elif event.key == pygame.K_ESCAPE:
                        self.return_to_menu()

    def update_sort(self):
        if self.state != self.STATE_VISUALIZING:
            return

        if not self.sorter.finished:
            self.sorter.step()
            self.bar_chart.active_indices = self.sorter.active_indices
            self.bar_chart.swap_indices = self.sorter.swap_indices
            self.bar_chart.pivot_index = self.sorter.pivot_index

            if self.sorter.finished:
                self.bar_chart.final_sweep()
                self.update_caption()
        elif self.bar_chart.sweeping:
            done = self.bar_chart.update_sweep()
            if done:
                pass

    def draw(self):
        self.screen.fill((30, 30, 30))
        if self.state == self.STATE_MENU:
            self.menu.draw(self.screen)
        else:
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