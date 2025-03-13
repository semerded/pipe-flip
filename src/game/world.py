import pygame
from src import data
from src.core.utils.screenunit import *
from src.core.utils.rect import Rect
from src.color import Color
from src.game.chunk import Chunk
from src.game.player import Player
from src.game.load_and_save import load_level
from src.game.tile import Tile


class World:
    def __init__(self, player1: Player, player2: Player):
        self.overworld_rect = Rect(0, 0, vw(100), vh(50))
        self.underworld_rect = Rect(0, vh(50), vw(100), vh(50))
        
        self.player1 = player1
        self.player2 = player2
        
        self.overworld = Chunk(player1, self.overworld_rect, False)
        self.underworld = Chunk(player2, self.underworld_rect, True)
        
        self.load_level()
        
    def cycle(self):
        self.overworld.cycle()
        self.underworld.cycle()
        
    def load_level(self):
        level_data = load_level()
        for tile in level_data["overworld"]:
            self.overworld.tiles.append(Tile(tile[0], tile[1], tile[2], False))
        for tile in level_data["underworld"]:
            self.underworld.tiles.append(Tile(tile[0], tile[1], tile[2], True))
        

    def draw(self):
        self.overworld.draw()
        self.underworld.draw()
        
    def update(self):
        self.draw()
        data.rect_update_list = []
        data.rect_update_list.append(self.overworld_rect.union(self.underworld_rect))
    
    def switch_players(self):
        self.player1.change_chunk()
        self.player2.change_chunk()
        
        if self.player1.upside_down:
            self.overworld.player = self.player2
            self.underworld.player = self.player1
        else:
            self.overworld.player = self.player1
            self.underworld.player = self.player2