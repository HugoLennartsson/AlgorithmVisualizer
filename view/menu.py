import pygame

ALGORITHMS = [
    {
        "name": "Insertion Sort",
        "class": "InsertionSort",
        "complexity": "O(n\u00b2)",
        "difficulty": "Easy",
    },
    {
        "name": "Bubble Sort",
        "class": "BubbleSort",
        "complexity": "O(n\u00b2)",
        "difficulty": "Easy",
    },
    {
        "name": "Selection Sort",
        "class": "SelectionSort",
        "complexity": "O(n\u00b2)",
        "difficulty": "Easy",
    },
    {
        "name": "Quick Sort",
        "class": "QuickSort",
        "complexity": "O(n log n)",
        "difficulty": "Medium",
    },
]

DIFFICULTY_COLORS = {
    "Easy": (46, 204, 113),
    "Medium": (255, 165, 0),
    "Hard": (231, 76, 60),
}

class MenuCard:
    def __init__(self, rect, algorithm_data):
        self.rect = rect
        self.algorithm_data = algorithm_data
        self.hovered = False

    def draw(self, surface):
        bg_color = (50, 50, 50) if not self.hovered else (70, 70, 70)
        border_color = (100, 100, 100) if not self.hovered else (100, 180, 255)

        pygame.draw.rect(surface, bg_color, self.rect, border_radius=8)
        pygame.draw.rect(surface, border_color, self.rect, width=2, border_radius=8)

        title_font = pygame.font.SysFont(None, 28)
        detail_font = pygame.font.SysFont(None, 22)
        stat_font = pygame.font.SysFont(None, 20)

        title_surface = title_font.render(self.algorithm_data["name"], True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.rect.centerx, self.rect.top + 35))

        complexity_surface = detail_font.render(self.algorithm_data["complexity"], True, (200, 200, 200))
        complexity_rect = complexity_surface.get_rect(center=(self.rect.centerx, self.rect.top + 75))

        difficulty_color = DIFFICULTY_COLORS.get(self.algorithm_data["difficulty"], (255, 255, 255))
        diff_surface = stat_font.render(self.algorithm_data["difficulty"], True, difficulty_color)
        diff_rect = diff_surface.get_rect(center=(self.rect.centerx, self.rect.top + 105))

        surface.blit(title_surface, title_rect)
        surface.blit(complexity_surface, complexity_rect)
        surface.blit(diff_surface, diff_rect)

    def contains(self, pos):
        return self.rect.collidepoint(pos)


class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cards = []
        self.hovered_index = -1
        self._build_cards()

    def _build_cards(self):
        card_width = 180
        card_height = 140
        cols = 2
        rows = 2
        start_x = (self.width - cols * card_width - (cols - 1) * 30) // 2
        start_y = 150
        gap_x = 30
        gap_y = 30

        self.cards = []
        for i, algo in enumerate(ALGORITHMS):
            row = i // cols
            col = i % cols
            x = start_x + col * (card_width + gap_x)
            y = start_y + row * (card_height + gap_y)
            rect = pygame.Rect(x, y, card_width, card_height)
            self.cards.append(MenuCard(rect, algo))

    def handle_mouse_move(self, pos):
        for i, card in enumerate(self.cards):
            card.hovered = card.contains(pos)
            if card.hovered:
                self.hovered_index = i
            else:
                if self.hovered_index == i:
                    self.hovered_index = -1

    def handle_click(self, pos):
        for i, card in enumerate(self.cards):
            if card.contains(pos):
                return ALGORITHMS[i]
        return None

    def draw(self, surface):
        surface.fill((30, 30, 30))

        title_font = pygame.font.SysFont(None, 48)
        title = title_font.render("Algorithm Visualizer", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.width // 2, 60))
        surface.blit(title, title_rect)

        subtitle_font = pygame.font.SysFont(None, 24)
        subtitle = subtitle_font.render("Select an algorithm to visualize", True, (150, 150, 150))
        subtitle_rect = subtitle.get_rect(center=(self.width // 2, 95))
        surface.blit(subtitle, subtitle_rect)

        for card in self.cards:
            card.draw(surface)

        hint_font = pygame.font.SysFont(None, 22)
        hint = hint_font.render("Click a card to start", True, (100, 100, 100))
        hint_rect = hint.get_rect(center=(self.width // 2, self.height - 40))
        surface.blit(hint, hint_rect)

        pygame.display.flip()
