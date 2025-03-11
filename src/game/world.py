import pygame
from src import data
from src.core.utils.screenunit import *
from src.core.utils.rect import Rect
from src.color import Color

top_rect = Rect(0, 0, vw(100), vh(50))
bottom_rect = Rect(0, vh(50), vw(100), vh(50))

def draw_world():
    pygame.draw.rect(data.window, Color.RED, top_rect.pack())
    pygame.draw.rect(data.window, Color.BLUE, bottom_rect.pack())
    