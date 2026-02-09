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
        active_color=(200, 50, 50),
        spacing =2 
    ):
        self.values = values
        self.rect = pygame.Rect(x, y, width, height)
        self.bar_color = bar_color
        self.active_color = active_color

        self.spacing = spacing
        self.active_indices = set()
    
    def draw(self, surface):
        if not self.values:
            return
        
        max_value = max(self.values)
        bar_width = self.rect.width // len(self.values)

        for i, value in enumerate(self.values):
            bar_height = int((value/max_value)* self.rect.height)

            x = self.rect.x + i * bar_width
            y = self.rect.y + self.rect.height - bar_height
            color = (
                self.active_color
                if i in self.active_indices
                else self.bar_color
            )
            pygame.draw.rect(
                surface,
                color,
                (x, y, bar_width - 2, bar_height)
            )
        
    
    