import pygame

class Sidebar:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.buttons = [
            {"text": "Add Node", "rect": pygame.Rect(x + 10, y + 10, width - 20, 50)},
            {"text": "Add Edge", "rect": pygame.Rect(x + 10, y + 70, width - 20, 50)}
        ]

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), self.rect)
        font = pygame.font.Font(None, 36)
        
        for button in self.buttons:
            pygame.draw.rect(screen, (200, 200, 200), button["rect"])
            text = font.render(button["text"], True, (0, 0, 0))
            text_rect = text.get_rect(center=button["rect"].center)
            screen.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def get_button(self, pos):
        for button in self.buttons:
            if button["rect"].collidepoint(pos):
                return button["text"]
        return None