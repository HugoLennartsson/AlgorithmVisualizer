import pygame

class BarChart:
    def __init__(
        self,
        values,
        x,
        y,
        width, 
        height,
        bar_color = (255,255,255),
        spacing =2 
    ):
        self.values = values
        self.rect = pygame.Rect(x, y, width, height)
        self.bar_color = bar_color
        self.spacing = spacing
    
    def draw(self, surface):
        if not self.values:
            return
        
        max_value = max(self.values)
        bar_width = self.rect.width // len(self.values)

        for i, value in enumerate(self.values):
            bar_height = int((value/max_value)* self.rect.height)

            x = self.rect.x + i * bar_width
            y = self.rect.y + self.rect.height - bar_height

            pygame.draw.rect(
                surface,
                self.bar_color,
                (x, y, bar_width - 2, bar_height)
            )