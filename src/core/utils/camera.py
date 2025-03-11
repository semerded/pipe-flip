import pygame
from src import data

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Adjust entity's position to match the camera's offset
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # Center the camera on the target (e.g., the player)
        x = -target.rect.centerx + data.window_width // 2
        y = -target.rect.centery + data.window_height // 2

        # Clamp the camera within the game world boundaries
        x = max(-(self.width - data.window_width), min(0, x))
        y = max(-(self.height - data.window_height), min(0, y))

        self.camera = pygame.Rect(x, y, self.width, self.height)
