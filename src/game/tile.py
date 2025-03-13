import pygame
from src import data
from src.core.utils.rect import Rect
from src.core.handler.scaling import Scaling
from src.color import Color

class Tile:
    def __init__(self, x: int, y: int, type: str, upside_down: bool = False):
        self.upside_down = upside_down
        self.size = data.TILE_SIZE
        self.tile_x = x
        if not self.upside_down:
            self.tile_y = y
        else:
            self.tile_y = data.TILE_COUNT_Y - y - 1
            
        self.rect = Rect(Scaling.tile_to_screenunit(self.tile_x), Scaling.tile_to_screenunit(self.tile_y), self.size, self.size)
        self.type = type
        
        if upside_down:
            self.texture = data.tile_texture_cache[self.type]["underworld"][0]
            self.texture = pygame.transform.flip(self.texture, False, True)
        else:
            self.texture = data.tile_texture_cache[self.type]["overworld"][0]
        
    def cycle(self):
        
        pass
    
    def draw(self):
        data.window.blit(self.texture, self.rect)
