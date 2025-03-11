import pygame
from src import data
from src.core.utils.screenunit import *
from src.core.utils.rect import Rect
from src.color import Color
from src.game.chunk import Chunk
from src.game.player import Player


class World:
    def __init__(self, player1: Player, player2: Player):
        self.overworld_rect = Rect(0, 0, vw(100), vh(50))
        self.underworld_rect = Rect(0, vh(50), vw(100), vh(50))
        
        self.player1 = player1
        self.player2 = player2
        
        self.overworld = Chunk(player1, self.overworld_rect)
        self.underworld = Chunk(player2, self.underworld_rect)

    def draw(self):
        # pygame.draw.rect(data.window, Color.RED, self.overworld_rect.pack())
        # pygame.draw.rect(data.window, Color.BLUE, self.underworld_rect.pack())
        
        self.overworld.draw(Color.BLUE)
        self.underworld.draw(Color.RED)
    
    def switch_players(self):
        self.player1.change_chunk()
        self.player2.change_chunk()
        
        if self.player1.upside_down:
            self.overworld.player = self.player2
            self.underworld.player = self.player1
        else:
            self.overworld.player = self.player1
            self.underworld.player = self.player2