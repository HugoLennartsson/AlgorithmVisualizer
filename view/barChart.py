import pygame

class BarChart:
    def __init__(
        self,
        values,
        x,
        y,
        width,
        height,
        bar_color=(255, 255, 255),
        active_color=(200, 50, 50),
        swap_color=(255, 100, 100),
        pivot_color=(255, 200, 0),
        sorted_color=(46, 204, 113),
        spacing=2
    ):
        self.values = values
        self.rect = pygame.Rect(x, y, width, height)
        self.bar_color = bar_color
        self.active_color = active_color
        self.swap_color = swap_color
        self.pivot_color = pivot_color
        self.sorted_color = sorted_color

        self.spacing = spacing
        self.active_indices = set()
        self.swap_indices = set()
        self.pivot_index = -1
        self.sweep_indices = set()
    
    def draw(self, surface):
        if not self.values:
            return
        max_val = max(self.values) if max(self.values) > 0 else 1

        bar_width = self.rect.width // len(self.values)

        for i, value in enumerate(self.values):
            bar_height = int((value / max_val) * self.rect.height)

            x = self.rect.x + i * bar_width
            y = self.rect.y + self.rect.height - bar_height

            if i in self.sweep_indices:
                color = self.sorted_color
            elif i == self.pivot_index:
                color = self.pivot_color
            elif i in self.swap_indices:
                color = self.swap_color
            elif i in self.active_indices:
                color = self.active_color
            else:
                color = self.bar_color

            pygame.draw.rect(
                surface,
                color,
                (x, y, bar_width - 2, bar_height)
            )

    def final_sweep(self):
        """Reset and initiate a sweep that turns all bars green."""
        self.sweep_indices.clear()
        self.sweep_index = 0
        self.sweeping = True

    def update_sweep(self):
        """Advance the sweep by one position, returns True when complete."""
        if not getattr(self, 'sweeping', False):
            return False

        if self.sweep_index < len(self.values):
            self.sweep_indices.add(self.sweep_index)
            self.sweep_index += 1
            return False
        else:
            self.sweeping = False
            return True
        
    
    