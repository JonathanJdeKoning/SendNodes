import pygame

class Node:
    def __init__(self, x, y, radius=30, color=(200, 200, 200)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.selected = False
        self.hover = False

    def draw(self, screen):
        color = self.color
        if self.hover:
            color = (255, 255, 0)  # Highlight on hover
        if self.selected:
            color = (0, 255, 0)  # Green when selected
        
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        return ((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2) <= self.radius ** 2

    def move(self, dx, dy):
        self.x += dx
        self.y += dy