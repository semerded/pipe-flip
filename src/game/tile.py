import pygame
from src import data
from src.core.utils.rect import Rect
from src.core.handler.scaling import Scaling
from src.color import Color

class Tile:
    def __init__(self, x: int, y: int):
        self.tile_x = x
        self.tile_y = y
        
        self.size = data.TILE_SIZE
        self.rect = Rect(Scaling.tile_to_screenunit(self.tile_x), Scaling.tile_to_screenunit(self.tile_y), self.size, self.size)
        
        
    def cycle(self):
        
        pass
    
    def draw(self):
        pygame.draw.rect(data.window, Color.PINK, self.rect.pack())