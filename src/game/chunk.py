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
        
        
    def _load_textures(self):
        pass
        # pygame.image.load(self.TEXTURE_PATH_BASE + "0" + self.player.color_blind_type.value + ".png")
        
    def draw(self, color):
        pygame.draw.rect(data.window, color, self.rect.pack())
        
        self.player.move()
        self.player.draw()
        
    def update(self):
        pygame.display.update(self.rect)