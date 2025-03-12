import pygame
from src.game.player import Player
from src.core.utils.rect import Rect
from src.core.utils.screenunit import *
from src.color import Color
from src import data


class Chunk:
    def __init__(self, player: Player, rect: Rect):
        self.player = player
        self.rect = rect
        self.TEXTURE_PATH_BASE = "assets/textures/chunks/"
        self.textures = []
        self.stage_update = True
        
        
        
    def _load_textures(self):
        pass
        # pygame.image.load(self.TEXTURE_PATH_BASE + "0" + self.player.color_blind_type.value + ".png")
    
    def cycle(self, color):
        if self.player.cycle():
            pygame.draw.rect(data.window, color, self.rect.pack())
            self.player.draw()
            
        
    def draw(self, color):
        pygame.draw.rect(data.window, color, self.rect.pack())
        self.player.draw()
        
    def update(self):        
        self.player.draw()
        pygame.display.update(self.rect)