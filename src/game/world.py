import pygame
from src import data
from src.core.utils.screenunit import *
from src.core.utils.rect import Rect
from src.color import Color


class World:
    def __init__(self):
        self.top_rect = Rect(0, 0, vw(100), vh(50))
        self.bottom_rect = Rect(0, vh(50), vw(100), vh(50))

    def draw(self):
        pygame.draw.rect(data.window, Color.RED, self.top_rect.pack())
        pygame.draw.rect(data.window, Color.BLUE, self.bottom_rect.pack())
    