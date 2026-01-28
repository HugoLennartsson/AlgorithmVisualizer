import pygame
import sys
from view.barChart import BarChart
class Window:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Algorithm Visualizer")
        self.clock = pygame.time.Clock()
        self.running = True

        self.BarChart = BarChart(
            values=[10,40,25,60,80,30],
            x=50,
            y=50,
            width=700,
            height = 500
        )
    
         

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
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
