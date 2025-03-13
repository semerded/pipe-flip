import pygame
from src.game.player import Player
from src.core.utils.rect import Rect
from src.core.utils.screenunit import *
from src.color import Color
from src import data
from src.game.tile import Tile


class Chunk:
    def __init__(self, player: Player, rect: Rect):
        self.player = player
        self.rect = rect
        self.TEXTURE_PATH_BASE = "assets/textures/chunks/"
        self.textures = []
        self.stage_update = True
        
        self.tiles = []
        
        
        #testing
        self.tiles.append(Tile(3, 8))
        self.tiles.append( Tile(3, 6))
        self.tiles.append(Tile(4, 8))
        self.tiles.append( Tile(5, 8))
        self.tiles.append(Tile(5, 7))
        
        
        
    def _load_textures(self):
        pass
        # pygame.image.load(self.TEXTURE_PATH_BASE + "0" + self.player.color_blind_type.value + ".png")
    
    def cycle(self, color):
        if self.player.cycle(self.tiles):
            self.draw(color)
            
        
    def draw(self, color):
        pygame.draw.rect(data.window, color, self.rect.pack())
        tile: Tile
        for tile in self.tiles:
            tile.draw()
        self.player.draw()

        
    def update(self):        
        self.player.draw()
        pygame.display.update(self.rect)